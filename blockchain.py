import hashlib
import time
from datetime import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, reward):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.reward = reward
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(
            f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.reward}".encode()
        ).hexdigest()

class Blockchain:
    def __init__(self, genesis_date="2025-09-15 00:00:00"):
        self.chain = [self.create_genesis_block(genesis_date)]
        self.block_reward = 50.0
        self.halving_interval = 210_000
        self.block_time = 600  # 10 minutos
        self.blocks_mined = 1

    def create_genesis_block(self, genesis_date):
        return Block(0, "0", genesis_date, "Genesis Block - NBG", 50.0)

    def get_latest_block(self):
        return self.chain[-1]

    def mine_block(self, data=""):
        self.blocks_mined += 1
        if self.blocks_mined % self.halving_interval == 0:
            self.block_reward /= 2
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        new_block = Block(
            len(self.chain),
            self.get_latest_block().hash,
            timestamp,
            data,
            self.block_reward,
        )
        self.chain.append(new_block)
        return new_block

if __name__ == "__main__":
    blockchain = Blockchain()
    print("Genesis Block criado:", blockchain.chain[0].__dict__)
    for i in range(1, 6):
        block = blockchain.mine_block(data=f"Transação {i}")
        print(f"Bloco {block.index} minerado: {block.__dict__}")
        time.sleep(1)
