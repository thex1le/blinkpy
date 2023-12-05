from os import environ
import asyncio
from datetime import datetime, timedelta
from aiohttp import ClientSession
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from blinkpy.helpers.util import json_load

TIMEDELTA = timedelta(environ.get("TIMEDELTA", 1))
username = "USERNAME HERE"
password = "PASSWORD HERE"


def get_date():
    return (datetime.now() - TIMEDELTA).isoformat()


async def download_videos(blink, save_dir="./media"):
    await blink.download_videos(save_dir, since=get_date())


async def start(session: ClientSession):
    blink = Blink(session=session)
    blink.auth = Auth({"username":username, "password":password}, session=session)
    await blink.start()
    return blink


async def main():
    session = ClientSession()
    blink = await start(session)
    await download_videos(blink)
    await session.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
