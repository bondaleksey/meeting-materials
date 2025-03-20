import asyncio


async def delay(delay_seconds: int) -> int:
    print(f"I'm going to sleep for {delay_seconds} seconds")
    await asyncio.sleep(delay_seconds)
    print(f"I'm awake after {delay_seconds} seconds")
    return delay_seconds


async def delay_with_message(delay_seconds: int, message: str) -> int:
    print(message)
    print(f"I'm going to sleep for {delay_seconds} seconds")
    await asyncio.sleep(delay_seconds)
    print(f"I'm awake after {delay_seconds} seconds")
    return delay_seconds
