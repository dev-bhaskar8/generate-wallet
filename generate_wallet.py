from web3 import Web3

w3 = Web3()
w3.eth.account.enable_unaudited_hdwallet_features()
_, my_mnemonic = w3.eth.account.create_with_mnemonic()
print("Seed: ",my_mnemonic,"\n")
for i in range(10):
    account = w3.eth.account.from_mnemonic(my_mnemonic, account_path=f"m/44'/60'/0'/0/{i}")
    print(i,f"m/44'/60'/0'/0/{i}",account.address,Web3.toHex(account.key))
