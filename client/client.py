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

def _hash(data):
    return hashlib.sha512(data).hexdigest()