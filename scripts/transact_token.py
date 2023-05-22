from brownie import MyToken,accounts
from web3 import Web3

def deploy_token():
    initial_supply = Web3.toWei(21_000_000,"ether")
    my_token = MyToken.deploy(accounts.load("my-new-account"),initial_supply,{"from":accounts.load("my-new-account")})
    return my_token

def get_token_balance(account_address):
    my_token = MyToken[-1]
    balance = my_token.balanceOf(account_address)
    print(f"The account {account_address} has balance {balance}")

def send_token(receiver,amount):
    my_token = MyToken[-1]
    my_token.transfer(receiver,amount)
    get_token_balance(receiver)

def main():
    print(accounts)

main()