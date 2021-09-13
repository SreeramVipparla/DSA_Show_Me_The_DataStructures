import hashlib
import datetime
import time


def calc_hash(data, timestamp):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.prev = None
        self.previous_hash = previous_hash
        self.hash = calc_hash(str(data), self.timestamp)

    def __repr__(self):
        return 'The Blockchain data consists : \n Data: {} \n Hash: {} \n Time\
        stamp: {}'.format(self.data, self.hash, self.timestamp)


class Blockchain:

    def __init__(self):
        self.head = None

    def length(self):
        var_head = self.head
        length = 0

        while var_head:
            var_head = var_head.prev
            length += 1

        return length

    def append(self, data, previous_hash):

        if self.head == None:
            self.head = Block(datetime.datetime.utcnow(), data, 0)
            return
        var_head_new = Block(datetime.datetime.utcnow(), data, self.head.hash)
        var_head_new.prev = self.head
        self.head = var_head_new

    def list(self):
        if self.head is None:
            return []
        output = []

        var_head = self.head
        while var_head:
            output.append(var_head)
            var_head = var_head.prev
        return output

# Test cases

# Edge  Case 1


print("Blockchain length  :", Blockchain().length())
print("Number of stored values in the Blockchain :", Blockchain().head)
# Expected output
# Blockchain size : 0
# Number of stored values in the Blockchain : None

# Edge case 2
blockchain = Blockchain()
blockchain.append("", 0)
print("length of blockchain : ", blockchain.length())
for value in blockchain.list():
    print(value)
# Expected output
# The Blockchain data consists :
# Data:
# Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
# Time stamp: 2021-09-13 18:07:04.742438



# Test case 1

blockchain = Blockchain()
blockchain.append("abcd", 0)
print("length of blockchain : ", blockchain.length())
for value in blockchain.list():
    print(value)

# Expected output
# The Blockchain data consists :
# Data: abcd
# Hash: 88d4266fd4e6338d13b845fcf289579d209c897823b9217da3e161936f031589
# Time stamp: 2021-09-13 00:47:34.901426

# Test case 2

blockchain = Blockchain()
blockchain.append("AAAAAAADDDDDDIFFFFFFFFFRRRR", 0)
print("length of blockchain : ", blockchain.length())
for value in blockchain.list():
    print(value)
print()
# Expected output
# The Blockchain data consists :
# Data: AAAAAAADDDDDDIFFFFFFFFFRRRR
# Hash: fecf4614a24e3e8bbeebc041cb993ea9c9a6f59e042f6be48557a53440a7abb4
# Time stamp: 2021-09-13 00:50:17.356771
