from hashlib import sha256
from DataStructures import LinkedList


class BlockChain:
    class Block:
        def __init__(self, timestamp, data, prev_hash):
            self.data = data
            self.timestamp = timestamp
            self.previous_hash = prev_hash
            self.__calc_hash()

        def __str__(self):
            return (
                f"Data: {self.data}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Hash: {self.hash}"
            )

        def __repr__(self): return self.__str__()

        def __calc_hash(self):
            sha = sha256()
            check = f"{self.data}{self.timestamp}{self.previous_hash}"
            sha.update(check.encode('utf-8'))
            self.hash = sha.hexdigest()

        @classmethod
        def check_hash(cls, timestamp, data, prev_hash):
            sha = sha256()
            check = f"{data}{timestamp}{prev_hash}"
            sha.update(check.encode('utf-8'))
            return sha.hexdigest()

    def __init__(self):
        self.__chain = LinkedList()

    def __len__(self):
        return self.__chain.size

    def __repr__(self):
        line = '-' * 80
        out = line + '\n'
        i = 1
        for block in self.__chain:
            out += f'{i}.\n{block}\n{line}\n'
            i += 1
        return out

    def __str__(self):
        return self.__repr__()

    def __getitem__(self, i):
        if type(i) != int:
            raise TypeError("blockchain indices must be integers")
        return self.__chain[i]

    # this is here to test the blockchain with an invalid block
    def __setitem__(self, i, block):
        self.__chain[i] = block

    @property
    def last(self):
        return self.__chain.last

    def verify(self):
        last = None
        i = 0
        for block in self.__chain:
            if last is None:
                last = block
                continue
            hash = BlockChain.Block.check_hash(
                block.timestamp, block.data, last.hash)
            if hash != block.hash:
                return i
            last = block
            i += 1
        return None

    def append(self, timestamp, data):
        last_hash = '0'
        if self.__chain.last is not None:
            last_hash = self.__chain.last.hash
        self.__chain.append(BlockChain.Block(timestamp, data, last_hash))

    def print_chain(self):
        for block in self.__chain:
            print(block)
