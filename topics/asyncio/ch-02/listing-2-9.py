import asyncio
from ..util import delay_with_message, delay


async def main():
    sleep_for_three = asyncio.create_task(delay(30))
    sleep_for_two = asyncio.create_task(delay(20))
    sleep_again = asyncio.create_task(delay(30))

    await sleep_for_three
    await sleep_for_two
    await sleep_again


asyncio.run(main())
