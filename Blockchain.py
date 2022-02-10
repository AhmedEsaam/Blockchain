# Python program to create Blockchain

# For timestamp
#import datetime 
from datetime import  datetime
#import time 
# Calculating the hash
# in order to add digital
# fingerprints to the blocks
import hashlib
 
# To store data
# in our blockchain
import json
import random 
# Flask is for creating the web
# app and jsonify is for
# displaying the blockchain


 
global n
n=1

class Block:
   def __init__(self):
      self.data = {}
      self.previous_block = None



class Blockchain:
    
    # This function is created
    # to create the very first
    # block and set it's hash to "0"
    def __init__(self):
        self.chain = []

        self.create_block(proof=1, previous_hash='0')



    # This function is created
    # to add further blocks
    # into the chain
    def create_block(self, proof, previous_hash):
        block = Block()

        transactions = []
        for i in range (3):
            new_trans = {
                'sender': 'Bob',
                'recipient': 'Alice',
                'amount': random.randint(10,200)
                }
            transactions.append(new_trans)

        block.data = {'index': 0,
                 'timestamp': str(datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions': transactions}

        self.chain.append(block)
        return block



    def longest_branch(self):
        max_index = 0
        last_block = self.chain[0]
        for i in range(len(self.chain)):
            current_index = self.chain[i].data['index']
            if current_index > max_index : 
                max_index = current_index
                last_block = self.chain[i]
        return last_block


       
    # This function is created
    # to display the previous block
    def print_previous_block(self):
        return self.chain[-1]
       
    # This is the function for proof of work
    # and used to successfully mine the block
    def proof_of_work(self, previous_hash):
        nonce = 0x0000000000000000
        check_proof = False
        global n 
        while check_proof is False:
            hash_operation = hashlib.sha256(
                (str(nonce)+str(previous_hash)).encode()).hexdigest()
            if hash_operation[:n] == n * '0':
                check_proof = True
            else:
                nonce += 1
        return nonce
 
    def hash(self, block):
        encoded_block = json.dumps(block.data, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
 

blockchain = Blockchain()
 



def mine_block(previous_block):
  global n
  while(1) :  
    
    previous_hash = blockchain.hash(previous_block)
    proof = blockchain.proof_of_work(previous_hash)


    var = previous_block.data['timestamp']
    no_frag , frag = var.split('.')
    t1 = datetime.strptime(no_frag, '%Y-%m-%d %H:%M:%S')  
    t1 = t1.replace(microsecond=int(frag))
    t2 = datetime.now()
    diff =  t2 - t1 
    diff_sec = diff.total_seconds()
    
    if diff_sec >= 1 :
       block = blockchain.create_block(proof, previous_hash)
       block.previous_block = previous_block
       block.data['index'] = block.previous_block.data['index'] + 1
       response = {'message': 'A block is MINED',
                'index': block.data['index'],
                'timestamp': block.data['timestamp'],
                'proof': block.data['proof'],
                'previous_hash': block.data['previous_hash'],
                'transactions':block.data['transactions'] }
       print(response) 
       print( "n = ",n)
       print( "diffierence in sec = ",diff_sec)
       n = n-1 
       break        
    else : 
        n = n+1 
  return block
     
    



