import pytest
import tasks
from tasks import Task


def test_add_1():
    """tasks.get() using id returend from add() works."""
    task = Task('breathe', 'BRIAN', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)

    # ID意外は同じはず
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', [Task('sleep', done=True),
                                  Task('wake', 'brian'),
                                  Task('breathe', 'BRIAN', True),
                                  Task('exercise', 'BriaN', False)])
def test_add_2(task: tasks.Task):
    """ task add parameters """
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(task, t_from_db)


def equivalent(t1: Task, t2: Task):
    # id 意外のフィールドを全て比較
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


@pytest.fixture(autouse=True)
def initialized_task_db(tmpdir: str):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()
