import hashlib

class PoopCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Anna sends 2 PC to Brennen"
t2 = "Brennen sends 5.3 PC to Tim"
t3 = "Lisa sends 1.9 PC to Ian"
t4 = "Ian sends 2.4 PC to Lily"
t5 = "Lily sends 0.8 PC to Bandit"
t6 = "Bandit sends 98 PC to Fattie"

initial_block = PoopCoinBlock("Initial String",[t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = PoopCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = PoopCoinBlock(second_block.block_hash, [t3, t4])

print(third_block.block_data)
print(third_block.block_hash) 