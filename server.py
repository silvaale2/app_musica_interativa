#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets
import ssl

logging.basicConfig()

STATE = {"value": 0}

USERS = set()


def state_event():
    return json.dumps({"type": "state", **STATE})


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "play":
                STATE["value"] = "play"
                await notify_state()
            elif data["action"] == "pause":
                STATE["value"] = "pause"
                await notify_state()
            elif data["action"] == "voltar":
                STATE["value"] = "voltar"
                await notify_state()
            elif data["action"] == "avancar":
                STATE["value"] = "avancar"
                await notify_state()
            elif data["action"] == "reiniciar":
                STATE["value"] = "reiniciar"
                await notify_state()
            elif data["action"] == "progresso":
                STATE["value"] = "progresso"
                STATE["numero"] = data["numero"]
                await notify_state()
            elif data["action"] == "enviar":
                STATE["value"] = "enviar"
                STATE["texto"] = data["texto"]
                await notify_state()
            elif data["action"] == "atualizarPlaylist":
                STATE["value"] = "atualizarPlaylist"
                STATE["p1"] = data["p1"]
                await notify_state()
            elif data["action"] == "atualizaContador":
                STATE["value"] = "atualizaContador"
                STATE["valorCorrente"] = data["valorCorrente"]
                await notify_state()    

            else:
                logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)

# Create the ssl context (to use https)
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
path_cert = "/var/www/html/flavio/certificado.pem"
path_key = "/var/www/html/flavio/chave.key"
ssl_context.load_cert_chain(path_cert, keyfile=path_key)

start_server = websockets.serve(
    counter, "alexandre.ufsj.edu.br", 6789, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
