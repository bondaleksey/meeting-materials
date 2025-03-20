import asyncio
from ..util import delay_with_message, delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(10)
    return "Hello, World!"


async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(10)
    print(one_plus_one)
    print(message)


asyncio.run(main())
