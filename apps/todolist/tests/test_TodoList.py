import pytest

from apiup import Doc, G, exceptions


async def test_structure():
    TodoList = Doc('TodoList')
    assert hasattr(TodoList(), 'id')
    assert hasattr(TodoList(), 'name')

    TodoListTask = Doc('TodoListTask')
    assert hasattr(TodoListTask(), 'id')
    assert hasattr(TodoListTask(), 'title')
    assert hasattr(TodoListTask(), 'details')


async def test_basic_validations(clean_db):
    with pytest.raises(exceptions.ValidationError):
        await G('TodoList', name='a')


async def test_adding_tasks(clean_db):
    TodoList = Doc('TodoList')
    doc = TodoList(name='Test list')
    assert doc.id is None
    await doc.save()
    assert doc.id

    assert len(await doc.get_tasks()) == 0
    description = 'My test task'
    details = 'All information of the task here'
    await doc.add_task(description, details)
    assert len(await doc.get_tasks()) == 1
