# MetaMask Institutional SDK (Beta)

A Python library to create and submit Ethereum transactions to custodians connected with [MetaMask Institutional](https://metamask.io/institutions); the most trusted DeFi wallet and Web3 gateway for organizations.

> **BETA DISCLAIMER.** By using this library, you acknowledge the technology is still in Beta access and for internal testing purposes only. You are responsible for your use of the Beta access to Open Source SDK and ConsenSys is not responsible for any bugs, deficiencies or issues that may occur.

![Banner](https://image-server-xab.s3.eu-west-1.amazonaws.com/mmisdk-banner.png)

## Usage

Use this SDK to programmatically create Ethereum transactions, and submit them to custodians connected with MetaMask Institutional. Automate trading strategies on your wallets under custody, and still benefit from the institutional-grade security of your favorite qualified custodian and custody provider.

## Installing

```sh
pip3 install mmisdk
```

## Getting started

```bash
$ pip install mmisdk
```

```python
>>> from mmisdk import CustodianFactory

>>> factory = CustodianFactory()

>>> custodian = factory.create_for("qredo", "YOUR-TOKEN")

>>> transaction = custodian.create_transaction(qredo_tx_details, tx_params)
>>> custodian.get_transaction(transaction.id)
```

### Supported custodians

Use the custodian's Factory name param in the table below to instantiate a client for the right custodian.

| Custodian       | Supported | As of version | Factory name param  |
| --------------- | --------- | ------------- | ------------------- |
| Bitgo           | ✅        | `0.3.0`       | `"bitgo"`           |
| Bitgo Test      | ✅        | `0.3.0`       | `"bitgo-test"`      |
| Cactus          | ✅        | `0.2.0`       | `"cactus"`          |
| Cactus Dev      | ✅        | `0.2.0`       | `"cactus-dev"`      |
| FPG             | ✅        | `0.4.0`       | `"fpg-prod"`        |
| FPG Alpha       | ✅        | `0.4.0`       | `"fpg-alpha"`       |
| FPG Local       | ✅        | `0.4.0`       | `"fpg-local"`       |
| Gnosis Safe     | ✅        | `0.4.0`       | `"gnosis-safe"`     |
| Gnosis Safe Dev | ✅        | `0.4.0`       | `"gnosis-safe-dev"` |
| Qredo           | ✅        | `0.2.0`       | `"qredo"`           |
| Qredo Dev       | ✅        | `0.1.0`       | `"qredo-dev"`       |
| Saturn          | ✅        | `0.4.0`       | `"saturn"`          |
| Saturn Dev      | ✅        | `0.4.0`       | `"saturn-dev"`      |

## Creating a transaction

```python
import os

from mmisdk import CustodianFactory

# Instantiate the factory
factory = CustodianFactory()

# Grab your token from the environment, or anywhere else
token = os.environ["MMISDK_TOKEN_QREDO_DEV"]

# Create the custodian, using the factory
custodian = factory.create_for("qredo-dev", token)

# Build tx details
tx_params = {
    "from": "0x62468FD916bF27A3b76d3de2e5280e53078e13E1",
    "to": "0x62468FD916bF27A3b76d3de2e5280e53078e13E1",
    "value": "100000000000000000",  # in Wei
    "gas": "21000",
    "gasPrice": "1000",
    # "data": "0xsomething",
    # "type": "2"
    # "maxPriorityFeePerGas": "12321321",
    # "maxFeePerGas": "12321321",
}
qredo_extra_params = {
    "chainID": "3",
}

# Create the tx from details and send it to the custodian
transaction = custodian.create_transaction(tx_params, qredo_extra_params)
print(type(transaction))
# <class 'mmisdk.common.transaction.Transaction'>

print(transaction)
# id='2EzDJkLVIjmH6LZQ2W1T4wPcTtK'
# type='1'
# from_='0x62468FD916bF27A3b76d3de2e5280e53078e13E1'
# to='0x62468FD916bF27A3b76d3de2e5280e53078e13E1'
# value='100000000000000000'
# gas='21000'
# gasPrice='1000'
# maxPriorityFeePerGas=None
# maxFeePerGas=None
# nonce='0'
# data=''
# hash=''
# status=TransactionStatus(finished=False, submitted=False, signed=False, success=False, displayText='Created', reason='Unknown')
```

## Getting a transaction

```python
import os

from mmisdk import CustodianFactory

# Instantiate the factory
factory = CustodianFactory()

# Grab your token from the environment, or anywhere else
token = os.environ["MMISDK_TOKEN_CACTUS_DEV"]

# Create the custodian, using the factory
custodian = factory.create_for("cactus-dev", token)

# Get the transaction
transaction = custodian.get_transaction("5CM05NCLMRD888888000800", 5)

print(type(transaction))
# <class 'mmisdk.common.transaction.Transaction'>

print(transaction)
# id='5CM05NCLMRD888888000800'
# type='1'
# from_='0xFA42B2eCf59abD6d6BD4BF07021D870E2FC0eF20'
# to=None
# value=None
# gas='133997'
# gasPrice='2151'
# maxPriorityFeePerGas=None
# maxFeePerGas=None
# nonce=''
# data=None
# hash=None
# status=TransactionStatus(finished=False, submitted=False, signed=False, success=False, displayText='Created', reason='Unknown')

```

## Running the examples

You can also explore various usage examples in the directory [`./examples`](https://gitlab.com/ConsenSys/codefi/products/mmi/mmi-sdk-py/-/tree/main/examples).

To run them, first export your custodian's token in the expected environment variable, then run the example file. For instance:

```bash
$ export MMISDK_TOKEN_BITGO_TEST=xxxx
$ python examples/getting_a_transaction_bitgo.py
```

> Note: Each example file expects to find to token under a specific environment variable name, that depends on the custodian and the environment (dev/test/prod) you're addressing. Read each example's code to figure out the right variable.

## Subscribing to transaction events

🚨 NOT IMPLEMENTED YET

```python
def log_event(event, *args, **kwargs):
    log.debug('%s %s %s', event, args, kwargs)

custodian.on('transaction-update', log_event)
```

## MVP Scope

-   Works with one custodian type (either Qredo or JSON-RPC)
-   Library published on pypi for python3 only

## Developer documentation

For instructions about development, testing, building and release, check the [developer documentation](https://gitlab.com/ConsenSys/codefi/products/mmi/mmi-sdk-py).
