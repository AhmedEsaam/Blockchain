from Blockchain import *
from Simulator import Simulator


# five initial blocks
for i in range (5) :
   previous_block = blockchain.longest_branch()
   mine_block(previous_block)
   print("initial block\n")
 

blocks_num = 20
attacker_speed = 52 # (%)
sim = Simulator(attacker_speed, blocks_num)
if sim == 0 : print("Attack Unsuccessful")
else: print("Attack Successful")



