from apiup import Context

from apps.sample.sample_commands import HelloWorld, Sleep


async def test_HelloWorld(clean_db, users):
    cmd = HelloWorld()
    cmd._validate()
    response = await cmd.command(Context.get())
    assert response == {'Hello': 'World!'}


async def test_Sleep(clean_db, users):
    cmd = Sleep(seconds=2)
    cmd._validate()
    response = await cmd.command(Context.get())
    assert response == 'Slept for 2s'
