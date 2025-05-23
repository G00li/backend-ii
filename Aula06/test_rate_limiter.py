import pytest
import asyncio
import time
from rate_limiter import RateLimiter, rate_limit

@pytest.mark.asyncio
async def test_rate_limiter_basic():
    limiter = RateLimiter(max_calls=2, time_period=1.0)
    
    # Primeiras duas chamadas devem passar imediatamente
    start_time = time.time()
    await limiter.acquire()
    await limiter.acquire()
    assert time.time() - start_time < 0.1
    
    # Terceira chamada deve esperar
    start_time = time.time()
    await limiter.acquire()
    assert time.time() - start_time >= 1.0

@pytest.mark.asyncio
async def test_rate_limit_decorator():
    @rate_limit(max_calls=2, time_period=1.0)
    async def test_function():
        return "success"
    
    # Primeiras duas chamadas devem passar imediatamente
    results = await asyncio.gather(
        test_function(),
        test_function()
    )
    assert all(r == "success" for r in results)
    
    # Terceira chamada deve esperar
    start_time = time.time()
    result = await test_function()
    assert time.time() - start_time >= 1.0
    assert result == "success" 