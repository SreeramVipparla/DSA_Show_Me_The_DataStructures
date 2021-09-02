#!/usr/bin/env python3

import argparse
import cmd
import datetime
import pathlib
import shlex
import sys
import time

from extract import load_neos, load_approaches
from database import NEODatabase
from filters import create_filters, limit
from write import write_to_csv, write_to_json


# Paths to the root of the project and the `data` subfolder.
PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()
DATA_ROOT = PROJECT_ROOT / 'data'

_START = time.time()


def date_fromisoformat(date_string):
    try:
        return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{date_string}'Use YYYY-MM-DD.")


def make_parser():
    parser = argparse.ArgumentParser(
        description="Explore past andfuturecloseapproachesofnear-Earthobjects."
    )
    # Add arguments for custom data files.
    parser.add_argument('--neofile', default=(DATA_ROOT / 'neos.csv'),
                        type=pathlib.Path,
                        help="Path to CSV file of near-Earth objects.")
    parser.add_argument('--cadfile', default=(DATA_ROOT / 'cad.json'),
                        type=pathlib.Path,
                        help="Path to JSON file of close approach data.")
    subparsers = parser.add_subparsers(dest='cmd')

    # Add the `inspect` subcommand parser.
    inspect = subparsers.add_parser('inspect',
                                    description="Inspect an  NEO by primary designation or by name.")
    inspect.add_argument('-v', '--verbose', action='store_true',
                         help="Additionally, print all known close approaches of this NEO.")
    inspect_id = inspect.add_mutually_exclusive_group(required=True)
    inspect_id.add_argument('-p', '--pdes',
                            help="The primary designation of the NEO to inspect (e.g. '433').")
    inspect_id.add_argument('-n', '--name',
                            help="The IAU name of the NEO to inspect (e.g. 'Halley').")

    # Add the `query` subcommand parser.
    query = subparsers.add_parser('query',
                                  description="Query for close approaches that"
                                              "match a collection of filters.")
    filters = query.add_argument_group('Filters',
                                       description="Filter close approaches bytheir attributes "
                                                   "or the attributes of theirNEOs.")
    filters.add_argument('-d', '--date', type=date_fromisoformat,
                         help="Only return close approaches on the given date,"
                              "in YYYY-MM-DD format (e.g. 2020-12-31).")
    filters.add_argument('-s', '--start-date', type=date_fromisoformat,
                         help="Only return close approaches on or after the given date, "
                              "in YYYY-MM-DD format (e.g. 2020-12-31).")
    filters.add_argument('-e', '--end-date', type=date_fromisoformat,
                         help="Only return close approaches on or before the given date, "
                              "in YYYY-MM-DD format (e.g. 2020-12-31).")
    filters.add_argument('--min-distance', dest='distance_min', type=float,
                         help="In astronomical units. Only return close approaches that "
                              "pass as far or farther away from Earth as the given distance.")
    filters.add_argument('--max-distance', dest='distance_max', type=float,
                         help="In astronomical units. Only return close approaches that "
                              "pass as near or nearer to Earth as the given distance.")
    filters.add_argument('--min-velocity', dest='velocity_min', type=float,
                         help="In kilometers per second. Only return close approaches "
                              "whose relative velocity to Earth at approach is as fast or faster "
                              "than the given velocity.")
    filters.add_argument('--max-velocity', dest='velocity_max', type=float,
                         help="In kilometers per second. Only return close approaches "
                              "whose relative velocity to Earth at approach is as slow or slower "
                              "than the given velocity.")
    filters.add_argument('--min-diameter', dest='diameter_min', type=float,
                         help="In kilometers. Only return close approaches of NEOs with "
                              "diameters as large or largerthanthegivensize.")
    filters.add_argument('--max-diameter', dest='diameter_max', type=float,
                         help="In kilometers. Only return close approaches of NEOs with "
                              "diameters as small orsmallerthanthegivensize.")
    filters.add_argument('--hazardous', dest='hazardous', default=None, action='store_true',
                         help="If specified, only return close approaches of NEOs that "
                              "are potentially hazardous.")
    filters.add_argument('--not-hazardous', dest='hazardous', default=None, action='store_false',
                         help="If specified, only return close approaches of NEOs that "
                              "are not potentially hazardous.")
    query.add_argument('-l', '--limit', type=int,
                       help="The maximum number of matches to return. "
                            "Defaults to 10 if no --outfile is given.")
    query.add_argument('-o', '--outfile', type=pathlib.Path,
                       help="File in which to save structured results. "
                            "If omitted, results areprintedtostandardoutput.")

    repl = subparsers.add_parser('interactive',
                                 description="Start an interactive command session "
                                             "to repeatedly run `interact` and `query` commands.")
    repl.add_argument('-a', '--aggressive', action='store_true',
                      help="If specified, kill the session whenever a project file is modified.")
    return parser, inspect, query
