import hashlib
import os
import json
import datetime as date


class Block(object):
    def __init__(self, dictionary):
        '''
            Look for: index, timestamp, data, prev_hash, nonce
        '''

        for k, v in dictionary.items():
            setattr(self, k, v)
        if not hasattr(self, 'hash'): #only used for inital block, delete later
            self.hash = self.create_self_hash()

    def __dict__(self):
        info = {}
        info['index'] = str(self.index)
        info['timestamp'] = str(self.timestamp)
        info['prev_hash'] = str(self.prev_hash)
        info['hash'] = str(self.hash)
        info['data'] = str(self.data)
        return info

    def __str__(self):
        return "Block<prev_hash: %s, hash: %s>" % (self.prev_hash, self.hash)
        
def create_first_block():
    # index zero and arbitratry previous hash
    block_data = {}
    block_data['index'] = 0
    block_data['timestamp'] = date.datetime.now()
    block_data['prev_hash'] = None
    block_data['data'] = 'First block data'
    block = Block(block_data)
    return block

#check if chaindata folder exists
chaindata_dir = 'chaindata'
if not os.path.exists(chaindata_dir):
    #make chaindata directory
    os.mkdir(chaindata_dir)
    #check if its empty from creation, or empty before
if os.listdir(chaindata_dir) == []:
    #create first block
    first_block = create_first_block()
    first_block.self_save()

