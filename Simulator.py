from Blockchain import *

def Simulator(speed,blocks_num) : 
        my_list = list(range(1,blocks_num+1)) 
        random.shuffle(my_list)

        attacker_prev_block = blockchain.chain[-3]
        successful = 0
        for i in range (0,blocks_num) :
            value = my_list[i]

            if value <= (speed/100) * blocks_num :
                # Attack
                if not successful: 
                    previous_block = attacker_prev_block
                else: previous_block = blockchain.longest_branch()
                block = mine_block(previous_block)
                print("attacker")
                attacker_prev_block = block
                if blockchain.longest_branch() == block :
                    successful = 1
                    print('successful')
                print('\n')
            else :
                # Normal mine
                previous_block = blockchain.longest_branch()
                mine_block(previous_block)
                print("Normal miner\n")

        return successful


