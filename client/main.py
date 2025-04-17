from client import *
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


def main():
    # Create keyFile
    keyfile = '/root/.sawtooth/keys/root.priv'

    LOGGER.info("Starting smpwlt")
    client = SimpleWalletClient(baseUrl='http://rest-api:8008', keyFile=keyfile)