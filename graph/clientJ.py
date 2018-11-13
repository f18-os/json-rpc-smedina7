# minimalistic client example from
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
import json
import node
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
    JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s, framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

from node import *

leaf1 = node("leaf1")
leaf2 = node("leaf2")
root = node("root", [leaf1, leaf1, leaf2])

# Execute in server:
# result = server.swapper('Hello World!')
assert isinstance(root, object)
result = server.swapper(json.dumps(root))

# "!dlroW olleH"
print(result)

# print(server.nop({1: [2, 3]}))

rpc.close()  # Closes the socket 's' also
