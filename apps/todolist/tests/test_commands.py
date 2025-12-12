import pytest
from apiup import Context, Doc, G, exceptions
from apps.todolist.commands import AddTask, ArchiveTask

TodoListTask = Doc('TodoListTask')


async def test_AddTask(clean_db, users):
    ctx = Context.get()
    ctx.user = users.user
    todolist = await G('TodoList', by=ctx.user)

    task_title = 'test-title'
    task_details = 'more details'
    cmd = AddTask(todolist_id=todolist.id, task_title=task_title, task_details=task_details)
    cmd._validate()

    response = await cmd.command(ctx)

    assert response['id']
    assert response['title'] == task_title
    assert response['details'] == task_details
    assert await TodoListTask.manager().count() == 1


async def test_ArchiveTask(clean_db, users):
    ctx = Context.get()
    ctx.user = users.user
    task = await G('TodoListTask', by=ctx.user)

    cmd = ArchiveTask(task_id=task.id)
    cmd._validate()

    response = await cmd.command(ctx)

    assert response['archived'] is True
