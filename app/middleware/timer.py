import time
from fastapi import Request

# simple restaurant analogy
async def timing_middleware(request: Request, call_next):
    # 1. Customer walks in. Start a stopwatch.
    start = time.perf_counter()

     # 2. Tell the kitchen to make the food. 
    # 3. "await" means: "While the kitchen cooks, I will help other people."
    response = await call_next(request)

    # 4. The kitchen is done! Stop the stopwatch.
    response.headers["X-Process-time"] = f"{time.perf_counter() - start:.4f}"

    # 5. Hand the food to the customer.
    return response
