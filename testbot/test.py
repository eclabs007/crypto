
from wazirx_sapi_client.websocket import WebsocketClient
import asyncio
api_key, secret_key = "test_api_key", "test_secret_key"
ws_client = WebsocketClient()

asyncio.create_task(
    ws_client.connect()
)

# to subscribe
await ws_client.subscribe(
    events=["btcinr@depth"],
)

await ws_client.subscribe(
    events=["wrxinr@depth"],
    id=1  # id param not mandatory
)

await ws_client.subscribe(
    events=["orderUpdate"]
)

await ws_client.subscribe(
    events=["outboundAccountPosition"],
    id=2  # id param not mandatory
)

### to unsubscribe
#await ws_client.unsubscribe(
#    events=["outboundAccountPosition", "wrxinr@depth"],
#)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()