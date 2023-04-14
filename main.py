# Author: CryptoLead at https://www.cryptolead.xyz
# Date: 2023-01-16
# Message: Hey there fellow coders! If you found my code helpful and want to show your support, consider buying me a coffee or two. Your donations help me keep improving the code and creating more awesome stuff for the community. Thanks for your support!
# Donation: cryptolead.eth or 0xa2c35DA418f52ed89Ba18d51DbA314EB1dc396d0


import hashlib
import datetime


class Block:
    def __init__(self, timestamp, transactions, previous_hash):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calc_hash()

    def calc_hash(self):
        block_string = (str(self.timestamp) +
                        str(self.transactions) +
                        str(self.previous_hash) +
                        str(self.nonce)).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block(datetime.datetime.now(), [], None)

    def get_latest_block(self):
        return self.chain[-1]

    def mine_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calc_hash()
        while (new_block.hash[:self.difficulty] != "0"*self.difficulty):
            #self.difficulty += 1
            new_block.nonce += 1
            new_block.hash = new_block.calc_hash()
        self.chain.append(new_block)
        self.difficulty += 1


demo_coin = Blockchain()
print(demo_coin.__dict__)

print(demo_coin.chain[0].__dict__)

txn1 = 'Peter sends 1 demo_coin to Lisa'
txn2 = 'Peter sends 30 demo_coin to Paul'
txn3 = 'Lisa sends 5 demo_coin to Peter'
my_transactions = (txn1, txn2, txn3)

block1 = Block(timestamp=datetime.datetime.now(),
               transactions=my_transactions, previous_hash=None)
print(block1.__dict__)

demo_coin.mine_block(block1)

print(demo_coin.__dict__)

print(demo_coin.chain[1].__dict__)

latest_block = demo_coin.get_latest_block()
print(latest_block.__dict__)
