import asyncio
import sys
import time

from prefect.deployments import run_deployment


async def submit(n: int):
    deployments = []
    start = time.time()

    print(f"Submitting {n} deployments")
    for _ in range(n):
        deployments.append(run_deployment('hello/trillian', timeout=0))
    
    print("Awaiting submissions")
    await asyncio.gather(*deployments)
    stop = time.time() - start
    print(f"All submissions completed in {stop:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(submit(int(sys.argv[1])))
