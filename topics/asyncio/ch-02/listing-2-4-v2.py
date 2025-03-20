import asyncio
from ..util import delay_with_message, delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(5)
    return "Hello, World!"


async def main() -> None:
    message1 = await hello_world_message()
    one_plus_one = await add_one(1)
    message2 = await hello_world_message()
    two_plus_one = await add_one(2)
    print(one_plus_one)
    print(two_plus_one)
    print(message1)
    print(message2)


asyncio.run(main())
