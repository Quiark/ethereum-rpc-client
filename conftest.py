import threading

import pytest


@pytest.fixture(scope="session")
def eth_coinbase():
    from ethereum import tester
    return tester.encode_hex(tester.accounts[0])


@pytest.yield_fixture()
def rpc_server():
    from testrpc.__main__ import create_server
    from testrpc.testrpc import evm_reset

    server = create_server('127.0.0.1', 8545)

    evm_reset()

    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    yield server

    server.shutdown()
    server.server_close()


@pytest.fixture()
def rpc_client():
    from eth_rpc_client import Client
    client = Client('127.0.0.1', '8545')
    return client
