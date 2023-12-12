from jokeapi import Jokes
from dotenv import load_dotenv
import os
import apprise
import asyncio
import aiohttp

load_dotenv()


async def run():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://v2.jokeapi.dev/") as response:
            status_code = response.status
            if 200 <= status_code < 300:
                print(f" Jokus is sent! ✔️ ")
            elif 400 <= status_code < 500:
                print(f" Client Error. Code: {status_code} ❌ ")
            elif 500 <= status_code < 600:
                print(f" Server Error. Code: {status_code} ❌ ")
            else:
                print(f" What is going on?: {status_code} ❓ ")


asyncio.run(run())


async def print_joke():
    j = await Jokes()

    # The parameters for the jokes can be adjusted here. More Infos: https://github.com/leet-hakker/JokeAPI-Python#parameters
    joke = await j.get_joke(
        lang="en", category=["programming", "pun"], blacklist=["nsfw", "racist"]
    )

    if joke["type"] == "single":
        return joke["joke"]
    else:
        return f"{joke['setup']} {joke['delivery']}"


async def main():
    joke_text = await print_joke()
    apobj = apprise.Apprise()

    # The notification service can be adjusted here. More Infos: https://github.com/caronc/apprise#supported-notifications
    apobj.add(f"nctalks://{os.getenv('NEXTCLOUDTALK_USER')}:{os.getenv('NEXTCLOUDTALK_PASS')}@{os.getenv('NEXTCLOUDTALK_HOST')}/{os.getenv('NEXTCLOUD_ROOM1')}/")

    apobj.notify(
        body=joke_text,
    )


if __name__ == "__main__":
    asyncio.run(main())
