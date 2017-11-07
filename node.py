from block import Block
from flask import Flask
import sync

import os
import json

node = Flask(__name__)

node_blocks = sync.sync() #initial sync blocks

@node.route('/blockchain.json', methods=['GET'])
def blockchain():
    '''
    Spits out the blockchain, which is just a json list of hashes right now
    with the block info should be:
    - index
    - timestamp
    - data
    - hash
    - prev_hash
    '''
    node_blocks = sync.sync()
    python_blocks = []
    for block in node_blocks:
        python_blocks.append(block.__dict__())
    json_blocks = json.dumps(python_blocks)
    return json_blocks

    if __name__ == '__main__':
        node.run()
