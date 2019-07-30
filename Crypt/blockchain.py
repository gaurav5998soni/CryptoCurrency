import datetime
import hashlib
import json


class Block:
  
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()
      

    def jsonformat(self):
    	context = {
    	'Block Hash' : str(self.hash()),
    	'Block No' : str(self.blockNo),
    	'Block Data' : str(self.data),
    	'Hashes' : str(self.nonce),
        'timestamp':str(self.timestamp),
    	}
    	return json.dumps(context) 

    def __str__(self):
        return "{ BlockNo: " + str(self.blockNo) +  " , Block Data: " + str(self.data) + " , Block Hash: " + str(self.hash()) + " , Hashes: " + str(self.nonce) + "}";


class Blockchain:
    diff = 1
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    head = block

    def add(self, block):
        
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                break
            else:
                block.nonce += 1
   
BlockChain = Blockchain()

    
