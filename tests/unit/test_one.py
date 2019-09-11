import time
import tasks
from tasks import Task
import pytest

def test_defaults():
    time.sleep(0.1)
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_across():
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)


def test_asdict():
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected


def test_replace():
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected


def test_default_param():
    t = Task(summary="hoge", done=False, id=111)
    assert t.summary == "hoge"
    assert t.id == 111


def test_raises():
    """test failed"""
    with pytest.raises(TypeError):
        tasks.add(task='not a task object')
    
