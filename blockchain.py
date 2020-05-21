from hashlib import sha256
import random
import json


# block must consist of data of transaction, hash of previous block,
class block:
    def getHash(self, data):
        return
    def __init__(self, index, transaction, prev_hash):
        self.index = index
        self.transaction = transaction
        self.hash = prev_hash
    def compute_hash(self, block):
        """
        Returns the hash of the block instance by first converting it
        into JSON string.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class blockchain:
    def initTransaction(self, amount):
        pass

    def __init__(self):
        self.chain = []

    def create_genesis_block(self):
        genesis_block = block(0, [], "0")
        self.chain.append(genesis_block)

