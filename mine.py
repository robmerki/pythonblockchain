from block import Block
import datetime as date
import time
import sync
import json
import hashlib

NUM_ZEROS = 4

def generate_header(index, prev_hash, data, timestamp):
    return str(index) + prev_hash + data + str(timestamp) + str(nonce)

def calculate_hash(index, prev_hash, data, timestamp, nonce):
    header_string = generate_header(index, prev_hash, data, timestamp, nonce)
    sha = hashlib.sha256()
    sha.update(header_string)
    return sha.hexdigest()

node_blocks = sync.sync()

def mine(last_block):
    index = int(last_block.index) + 1
    timestamp = date.datetime.now()
    data = "I am block #%s" % (int(last_block.index) + 1) #random string for now instead of money
    prev_hash = last_block.hash
    nonce = 0 

    while str(block_hash[0:NUM_ZEROS]) != '0' * NUM_ZEROS:
        nonce += 1
        block_hash = calculate_hash(index, prev_hash, data, timestamp, nonce)

    block_data = {}
    block_data['index'] = int(last_block.index) + 1
    block_data['prev_hash'] = last_block.hash
    block_data['timestamp'] = date.datetime.now()
    block_data['data'] = "I am block #%s" % (int(last_block.index) + 1)
    block_data['hash'] = block_hash
    block_data['nonce']
    return Block(block_data)

def save_block(block):
    chaindata_dir = 'chaindata'
    filename = '%s/%s.json' % (chaindata_dir, block.index)
    with open(filename, 'w') as block_file:
        print new_block.__dict__()
        json.dump(block.__dict__(), block_file)


if __name__ == '__main__':
    last_block = node_blocks[-1]
    new_block = mine(last_block)
    save_block(new_block)

