#!/usr/bin/python
# -*- coding:utf-8 -*-

# hash
import hashlib as hasher
# json
import json
blockchain = []


def hash(data, previous_hash):
    sha = hasher.sha256()
    sha.update("{0}{1}".format(data, previous_hash).encode("utf8"))
    return sha.hexdigest()


def make_a_block(data, previous_hash):
    block = {}
    block["data"] = data
    block["previous_hash"] = previous_hash
    block["hash"] = hash(data, previous_hash)
    return block


def add_a_block(data):

    # this is old format  but not simple
    #last_block = blockchain[len(blockchain)-1]
    # this is more  simplier
    last_block = blockchain[-1]
    #this is the last hash 
    previous_hash = last_block["hash"]

    #this is use a array to save but current environment cat; tve orivuder the enough space 
    blockchain.append(make_a_block(data, previous_hash))


def make_a_genesis_block():
    data = "this is the genesis block"
    previous_hash = 0

    blockchain.append(make_a_block(data, previous_hash))



#add a block and test 
if __name__ == '__main__':
    make_a_genesis_block()
    add_a_block("this is block 1")
    add_a_block("this is block 2")
    add_a_block("this is block 3")
    print(json.dumps(blockchain))
