#!/user/bin/env python3
""" Asynchronous generator that yields random numbers 
between 0 and 10 with a 1-second delay between each yield."""

from asyncio import sleep
from random import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Asynchronous generator that yields random numbers between 0 and 10"""
    for i in range(10):
        await sleep(1)
        yield random.unfiform(0, 10)
