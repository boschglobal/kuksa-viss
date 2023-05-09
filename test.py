#!/usr/bin/env python

import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri, subprotocols=["VISSv2"]) as websocket:
        # name = input("What's your name? ")

        await websocket.send('''{"action: 34"lol"}''')
        rep = await websocket.recv()
        print(f"<<< {rep}")

        await websocket.send('''{"action": "lol"}''')
        rep = await websocket.recv()
        print(f"<<< {rep}")

        await websocket.send('''{"action": "get"}''')
        rep = await websocket.recv()
        print(f"<<< {rep}")

        await websocket.send('''{"action": "get", "path": "Vehicle.Speeeeed", "requestId":"sddf"}''')
        rep = await websocket.recv()
        print(f"<<< {rep}")

        await websocket.send('''{"action": "get", "path": "Vehicle.Speed", "requestId":"sddf"}''')
        rep = await websocket.recv()
        print(f"<<< {rep}")

        await websocket.send('''{"action": "get", "path": "Vehicle.OBD.Speed", "requestId":"sddf"}''')
        rep = await websocket.recv()
        print(f"<<< {rep}")

        print("SEEEEEEEEEET")

        await websocket.send('''{"action": "set"}''')
        rep = await websocket.recv()
        print(f"<<< {rep}")

        await websocket.send('''{"action": "set", "path": "Vehicle.Speed", "requestId":"sddf"}''')
        rep = await websocket.recv()
        print(f"<<< {rep}")

        await websocket.send('''{"action": "set", "path": "Vehicle.Speed", "value": "400", "requestId":"sddf"}''')
        rep = await websocket.recv()
        print(f"<<< {rep}")


if __name__ == "__main__":
    asyncio.run(hello())
