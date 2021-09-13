
import os
# For coding the solution I have followed the logic given \
# in the knowledge post https://knowledge.udacity.com/questions/130481


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """
    if len(os.listdir(path)) == 0:
        return []

    if suffix == '':
        print('Please enter a valid suffix')
        return []
    all_files = [file for file in os.listdir(path)if '.' + suffix in file]
    all_folders = [file for file in os.listdir(path) if '.' not in file]

    for folder in all_folders:
        all_files .extend(find_files(suffix=suffix, path=path + '/' + folder))

    return all_files


base = os.getcwd() + '/testdir'


# Test cases

# Edge Case:
print(find_files(suffix='', path=base))
# Expected output
# []

# Normal Cases:

print(find_files(suffix='c', path=base))
# Expected output
# ['t1.c', 'a.c', 'a.c', 'b.c']

print(find_files(suffix='h', path=base))
# Expected output
# ['t1.h', 'a.h', 'a.h', 'b.h']

print(find_files(suffix='z', path=base))
# Expected output
# []
