#!/usr/bin/env python3
"""
Asynchronous generator that yields random numbers
between 0 and 10 with a 1-second delay between each yield.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers
    between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.unfiform(0, 10)

sync def print_yielded_values():
    """
    Asynchronously iterates over the async_generator, collecting and printing results.
    """

    result = []
    async for value in async_generator():
        result.append(value)
    print(result)

if __name__ == "__main__":
    asyncio.run(print_yielded_values())
