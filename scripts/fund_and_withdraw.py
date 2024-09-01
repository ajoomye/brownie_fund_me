from brownie import accounts, config, FundMe, network
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def fund():
    fundme = FundMe[-1]
    account = get_account()
    fundme.fund({"from": account, "value": 3})

def getvalue():
    fundme = FundMe[-1]
    account = get_account()
    print(fundme.addressToAmountFunded(account))

def withdraw():
    fundme = FundMe[-1]
    account = get_account()
    fundme.withdraw({"from": account})

def main():
    fund()
    getvalue()
    withdraw()
    getvalue()