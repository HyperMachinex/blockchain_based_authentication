import base64
import random
import requests
import yaml
import hashlib
from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory
from sawtooth_signing import ParseError
from sawtooth_signing.secp256k1 import Secp256k1PrivateKey
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader, Transaction
from sawtooth_sdk.protobuf.batch_pb2 import BatchList, BatchHeader, Batch

FAMILY_NAME = 'simplewallet'

class IdPClient(object):

    def __init__(self, baseUrl, keyFile=None):
        self._baseUrl = baseUrl
        if keyFile is None:
            self._signer = None
            return

        self._load_key(keyFile)

        self._address = _hash(FAMILY_NAME.encode('utf-8'))[0:6] + \
                        _hash(self._publicKey.encode('utf-8'))[0:64]


    # provate key
    def _load_key(self, keyFile):
        try:
            with open(keyFile) as fd:
                privateKeyStr = fd.read().strip()
        except OSError as err:
            raise Exception(f'Failed to read private key {keyFile}: {str(err)}')

        try:
            privateKey = Secp256k1PrivateKey.from_hex(privateKeyStr)
        except ParseError as err:
            raise Exception(f'Failed to load private key: {str(err)}')

        self._signer = CryptoFactory(create_context('secp256k1')).new_signer(privateKey)
        self._publicKey = self._signer.get_public_key().as_hex()

def _hash(data):
    return hashlib.sha512(data).hexdigest()