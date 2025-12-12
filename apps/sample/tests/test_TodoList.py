import pytest

from apiup import Doc, G, exceptions


async def test_structure():
    TodoList = Doc('TodoList')
    assert hasattr(TodoList(), 'id')
    assert hasattr(TodoList(), 'name')
    assert hasattr(TodoList(), 'tasks')


async def test_basic_validations(clean_db):
    with pytest.raises(exceptions.ValidationError):
        await G('TodoList', name='a')


async def test_adding_tasks(clean_db):
    TodoList = Doc('TodoList')
    doc = TodoList(name='Test list')
    assert doc.id is None
    assert doc.tasks == {}
    await doc.save()
    assert doc.id

    description = 'My test task'
    details = 'All information of the task here'
    await doc.add_task(description, details)
    assert doc.tasks == {description: {'details': details, 'completed': False}}
