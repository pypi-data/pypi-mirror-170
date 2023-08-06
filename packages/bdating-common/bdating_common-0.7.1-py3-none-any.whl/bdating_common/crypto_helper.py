"""
Crypto helper.

"""
import logging
from tokenize import Number
import web3
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
# from web3.auto.infura.mainnet import w3
from web3.exceptions import TransactionNotFound
import pickle
import sys
from enum import Enum

logger = logging.getLogger(__name__)

class TxnStatusEnum(Enum):
  TXN_MISMATCHED = -2
  TXN_REVERTED = -1
  TXN_NOT_READY = 0
  TXN_CONFIRMED = 1


networks = {
  'bnb_test': {
    # 'rpc_url': 'https://data-seed-prebsc-1-s1.binance.org:8545/',
    # 'chain_id': '97',
    # 'currency': 'BNB',
    # 'explorer_url': 'https://testnet.bscscan.com',
    'w3_client': Web3(HTTPProvider('https://data-seed-prebsc-1-s1.binance.org:8545/')),
    'minimal_confirm': 2
  },
  'bnb_main': {
    # 'rpc_url': 'https://bsc-dataseed1.ninicoin.io',
    # 'chain_id': '56',
    # 'currency': 'BNB',
    # 'explorer_url': 'https://bscscan.com',
    'w3_client': Web3(HTTPProvider('https://bsc-dataseed1.ninicoin.io')),
    'minimal_confirm': 3
  },
  'eth_main': {
    # 'rpc_url': 'https://rpc.ankr.com/eth',  # https://rpc.info/
    # 'chain_id': '1',
    # 'currency': 'ETH',
    'explorer_url': 'https://rpc.ankr.com/eth',
    'w3_client': Web3(HTTPProvider('https://rpc.ankr.com/eth')),
    'minimal_confirm': 3
  },
  'eth_goerli': {
    # 'rpc_url': 'https://rpc.ankr.com/eth_goerli',
    # 'chain_id': '5',
    # 'currency': 'ETH',
    # 'explorer_url': 'https://goerli.etherscan.io',
    'w3_client': Web3(HTTPProvider('https://rpc.ankr.com/eth_goerli')),
    'minimal_confirm': 3
  }
}
for k, v in networks.items():
    if k.endswith(''):
        v['w3_client'].middleware_onion.inject(geth_poa_middleware, layer=0)

""" Depricated
def check_transactions_by_wallet(blockchain_address: str, network: str = 'bnb_main', Logger: object=None):
    # NOTE: WIP code. We are not sure when and how to use this method.
    w3 = networks[network]['w3_client']

    # request the latest block number
    ending_blocknumber = w3.eth.blockNumber

    # latest block number minus 100 blocks
    starting_blocknumber = ending_blocknumber - 1

    # create an empty dictionary we will add transaction data to
    tx_dictionary = {}

    print(
        f"Started filtering through block number {starting_blocknumber} to {ending_blocknumber} for transactions involving the address - {blockchain_address}...")
    for x in range(starting_blocknumber, ending_blocknumber):
        block = w3.eth.getBlock(x, True)
        for transaction in block.transactions:
            # print(transaction)
            if str(transaction['to'].lower()) == blockchain_address or str(transaction['from'].lower()) == blockchain_address:
                print(transaction)
                with open("transactions.pkl", "wb") as f:
                    hashStr = transaction['hash'].hex()
                    tx_dictionary[hashStr] = transaction
                    pickle.dump(tx_dictionary, f)
                f.close()
    print(f"Finished searching blocks {starting_blocknumber} through {ending_blocknumber} and found {len(tx_dictionary)} transactions")
"""

def check_transaction_status(transaction_hash: str, to_address: str, value: Number, network: str = 'bnb_main') -> TxnStatusEnum:
    w3 = networks[network]['w3_client']
    minimal_confirm = networks[network]['minimal_confirm']
    try:
        txn_status = w3.eth.get_transaction_receipt(transaction_hash)['status']
        if txn_status == 0:
          logger.warning(f"Transaction {transaction_hash} was reverted by EVM!")
          return TxnStatusEnum.TXN_REVERTED

        transaction = w3.eth.get_transaction(transaction_hash=transaction_hash)

        last_block = w3.eth.get_block_number()
        print(f"Received Tranasction, {transaction}, last_block: {last_block}")
        if last_block - transaction.get('blockNumber', sys.maxsize) >= minimal_confirm:
          #TODO: convert bnb value from its unit
          txn_value = Web3.fromWei(transaction['value'], 'ether')
          if str(transaction['to']).lower() == to_address.lower() and txn_value >= value:
            logger.info(f"Transaction {transaction_hash} is available.")
            print(f"Transaction {transaction_hash} is available.")
            return TxnStatusEnum.TXN_CONFIRMED
          else:
            logger.warning(f"Transaction {transaction_hash} has been confirmed but details mismatched!")
            return TxnStatusEnum.TXN_MISMATCHED
        else:
          logger.info(f"Transaction {transaction_hash} is available now but still needs more confirmation.")
          return TxnStatusEnum.TXN_NOT_READY
    except TransactionNotFound:
        logger.info(f"Transaction {transaction_hash} not found yet.")
        return TxnStatusEnum.TXN_NOT_READY

"""
did not check confidence block gap
"""
def check_transaction_status_v2(transaction_hash: str, to_address: str, value: Number, network: str = 'bnb_main') -> bool:
    w3 = networks[network]['w3_client']
    try:
      transaction = w3.eth.get_transaction(transaction_hash=transaction_hash)
      #TODO: convert bnb value from its unit
      txn_value = Web3.fromWei(transaction['value'], 'ether')
      txn_status = w3.eth.get_transaction_receipt(transaction_hash)['status']
      # status ==1 should be able to present the succeed of txn
      if txn_status == 1:
        if str(transaction['to']).lower() == to_address.lower() and txn_value >= value:
          logger.info(f"Transaction {transaction_hash} is available.")
          print(f"Transaction {transaction_hash} is available.")
          return True
        else:
          logger.warning(f"Transaction {transaction_hash} received but details mismatched. value={txn_value}, to_addr={transaction['to']}")
          return False
      else:
        logger.warning(f"Transaction {transaction_hash} not confidence yet or failed")
        return False


    except TransactionNotFound:
      logger.info(f"Transaction {transaction_hash} not found yet.")
      return False

if __name__ == '__main__':
    print(check_transaction_status(transaction_hash='0xc878288e8222cc472a450a44ac0674498290757ac101f54b79be05c03d023d51', 
      to_address='0x840851d656e2575a3d524af2be7249dcdbaa718c', 
      value=0.000001,
      network='eth_goerli'))


    # w3 = Web3(HTTPProvider('https://rpc.ankr.com/eth_goerli'));
    # print(w3.eth.filter('pending'))
    # print(Web3.fromWei(677262836600000, 'ether'))
