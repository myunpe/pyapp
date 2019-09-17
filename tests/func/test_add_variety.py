import pytest
import tasks
from tasks import Task


tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('wake', 'brian'),
                Task('breathe', 'Brian', True),
                Task('execrise', 'BrIaN', False))

task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]


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


@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task: Task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task: Task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


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


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():
    """Demonstrate"""

    def test_equivalent(self, task: Task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        """We can use"""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id
