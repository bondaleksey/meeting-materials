import asyncio
from util import delay_with_message, delay


async def main() -> None:
    await delay(1)
    return "Hello, World!"


asyncio.run(main())
