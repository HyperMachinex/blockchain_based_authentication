#!/usr/bin/env python3
from client import *
import argparse
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

def deregister_identity_provider(name):
    keyfile = f'/root/.sawtooth/keys/{name}.priv'
    client = IdPClient(baseUrl='http://rest-api:8008', keyFile=keyfile)
    LOGGER.info(f"Deregistering from identity provider: {name}")
    client.deregister_identity_provider()

def main():
    #parser = argparse.ArgumentParser(description='Create a wallet')
    #parser.add_argument('wallet_name', type=str, help='Name of the wallet')
    #args = parser.parse_args()
    #deregister_identity_provider(args.wallet_name)
    return 2

if __name__ == '__main__':
    main()