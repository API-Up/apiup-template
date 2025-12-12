import pytest
from apiup import Doc, G, exceptions


TodoList = Doc('TodoList')
TodoListTask = Doc('TodoListTask')


async def test_TodoList(clean_db):
    todolist = await G('TodoList')
    assert await TodoListTask.manager().count() == 0
    task = await todolist.add_task('title', 'details')
    assert await TodoListTask.manager().count() == 1
    assert task in await todolist.get_tasks()


async def test_TodoListTask(clean_db):
    task = await G('TodoListTask', archived=False)
    await task.archive()
    assert task.archived is True
