from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://polygon.llamarpc.com"))
from_addr = "0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3"
to_addr = "0x6783BFA9841a1252E869B8938e48AC2e51bDDb5B"
private_key = "ee9cec01ff03c0adea731d7c5a84f7b412bfd062b9ff35126520b3eb3d5ff258"
actual_gas_fee = w3.eth.gas_price * 21000
while True:
    check_balance = w3.eth.get_balance(from_addr)
    if check_balance < actual_gas_fee:
        pass
    else:
        spend = (check_balance * (90 / 100))
        got = (check_balance - spend)
        lost = float(f"{spend:.2f}")
        got_in_float = float(f"{got:.2f}")
        gas_price = int(lost // 21000)
        got_in_matic = w3.from_wei(got_in_float, "ether")
        tx = {
            "nonce": w3.eth.get_transaction_count(from_addr),
            "to": to_addr,
            "value": w3.to_wei(got_in_matic, "ether"),    
            "gas": 21000,
            "gasPrice": gas_price,
            'chainId': 137
           }
        signtx = w3.eth.account.sign_transaction(tx, private_key=private_key)
        rawtx = w3.eth.send_raw_transaction(signtx.rawTransaction)
        txhash = w3.to_hex(rawtx)
        w3.eth.wait_for_transaction_receipt(txhash)
        print("Matic Transfer Successful :", txhash)
   
