from apiup import Command, Context, Doc, F, Jsonable, Permission, command

TodoList = Doc('TodoList')
TodoListTask = Doc('TodoListTask')


@command(method='POST', endpoint='/todolist/task/add', permission=Permission.OWNER)
class AddTask(Command):
    todolist_id: str = F(type='string', format='id')
    task_title: str = F(type='string')
    task_details: str = F(type='string')

    async def command(self, ctx: Context) -> Jsonable:
        todolist = await TodoList.auth_user().get_by_id_or_raise(self.todolist_id)
        task = TodoListTask(todolist_id=todolist.id)
        task.title = self.task_title
        task.details = self.task_details
        await task.save_by_auth_user()
        return task.to_dict(by=ctx.user)


@command(method='POST', endpoint='/todolist/task/archive', permission=Permission.OWNER)
class ArchiveTask(Command):
    task_id: str = F(type='string', format='id')

    async def command(self, ctx: Context) -> Jsonable:
        task: TodoListTask = await TodoListTask.auth_user().get_by_id_or_raise(self.task_id)
        task.archived = True
        await task.save_by_auth_user()
        return task.to_dict(by=ctx.user)
