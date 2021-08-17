from web3 import Web3
from get_coins import *
from csv import writer
import os, time
web3 = Web3(Web3.HTTPProvider('https://sparta-rpc.polis.tech/:8545'))
web3.isConnected()

while not os.path.exists('./stop'):
    time.sleep(5)
    new_acct = web3.eth.account.create()
    fromacc = new_acct._address
    privkey = new_acct.privateKey.hex()
    with open('Addresslist.csv', 'a', newline='') as f_object:
     writer_object = writer(f_object)
     writer_object.writerow([fromacc,privkey])  
     f_object.close()
    toacc = '0xc6dfA8ABf9FA741f853aB22060297dee0088a49f'
    nonce = web3.eth.getTransactionCount(fromacc)
    if getcoins(fromacc) == 200:
        tx = {
            'nonce': nonce,
            'to': toacc,
            'from': fromacc,
            'value': web3.eth.get_balance(fromacc) - web3.toWei(21000,'gwei'),
            'gas': 21000,
            'gasPrice': web3.toWei('1', 'gwei')
        }
        signedmsg = web3.eth.account.sign_transaction(tx, privkey)
        tx_hash = web3.eth.sendRawTransaction(signedmsg.rawTransaction)
        print('Transaction Completed to address ==>   '+web3.toHex(tx_hash))