from apiup import Q
from base_docs import TodoListData, TodoListTaskData

# Common utilities:
# from utils import http, json, secrets, utc, types
# from utils.log import Log


class TodoList(TodoListData):
    async def add_task(self, title: str, details: str) -> TodoListTask:
        task: TodoListTask = TodoListTask(todolist_id=self.id)
        task.title = title
        task.details = details
        await task.save_by_auth_user()
        return task

    async def get_tasks(self) -> list[TodoListTask]:
        return await TodoListTask.manager().find(where=Q.todolist_id == self.id)


class TodoListTask(TodoListTaskData):
    async def archive(self) -> None:
        self.archived = True
        await self.save()
