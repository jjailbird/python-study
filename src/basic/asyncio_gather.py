import asyncio

async def factorial(name, number):
  f = 1
  for i in range(2, number + 1):
    print(f"Task {name}: Compute factorial({i})...")
    await asyncio.sleep(1)
    f *= i
  print(f"Task {name}: factorial({number}) = {f}")
  return f

async def main():
  # Schedule three calls *concurrently*:
  # res = await asyncio.gather(
  #   factorial("A", 2),
  #   factorial("B", 3),
  #   factorial("C", 4),
  # )
  # print(res)
  res1, res2, res3 = await asyncio.gather(
    factorial("A", 2),
    factorial("B", 3),
    factorial("C", 4),
  )
  print(res1, res2, res3)

asyncio.run(main())