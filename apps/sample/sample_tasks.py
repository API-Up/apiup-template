import asyncio
import random
import typing

from apiup import Field, Log, Task


class HelloWorldTask(Task):
    async def process(self, **kwargs: typing.Any) -> Task.JSONType:
        return 'ok'


class SleepTask(Task):
    task_params: typing.ClassVar[dict[str, Field]] = dict(seconds=Field(type='int'))

    async def process(self, seconds: int = 0, **kwargs: typing.Any) -> str:
        Log.info(f'Sleeping for {seconds}s')
        seconds = int(seconds or random.uniform(1, 5))
        for _ in range(seconds):
            await asyncio.sleep(1)
            self.progress += int(100 * 1 / seconds)
        Log.info(f'Slept {seconds}s')
        return f'Slept for {seconds}s'
