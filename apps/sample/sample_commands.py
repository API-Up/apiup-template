import asyncio
import random

from apiup import Command, Context, F, Jsonable, Log, Permission, command


# http GET http://localhost:50000/sample/hello-world
@command(method='GET', endpoint='/sample/hello-world', permission=Permission.PUBLIC)
class HelloWorld(Command):
    async def command(self, ctx: Context) -> Jsonable:
        return {'Hello': 'World!'}


# http POST http://localhost:50000/sample/sleep seconds=2
@command(method='POST', endpoint='/sample/sleep', permission=Permission.PUBLIC)
class Sleep(Command):
    seconds: int = F(type='int', min=0, max=10)

    async def command(self, ctx: Context) -> Jsonable:
        seconds: int = int(self.seconds or random.uniform(1, 5))
        Log.info(f'Sleeping for {seconds}s')
        await asyncio.sleep(seconds)
        Log.info(f'Slept {seconds}s')
        return f'Slept for {seconds}s'
