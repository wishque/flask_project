from app.user import tasks
from celery import states
def test_hello():
    result=tasks.add.apply(args=(1,2))
    assert result.state==states.SUCCESS
    assert result.result==3