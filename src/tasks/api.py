from typing import NamedTuple
from six import string_types


class Task(NamedTuple):
    """namedtuple Task"""
    summary: str = None
    owner: str = None
    done: bool = False
    id: int = None

# custom exceptions
class TasksException(Exception):
    """A tasks error has occurred."""
    

class UninitializedDatabase(TasksException):
    """Call tasks.start_tasks_db() before other functions."""

def add(task: Task) -> int:
    if not isinstance(task, Task):
        raise TypeError('task must be Task object')
    return 1

def get(task_id):  # type: (int) -> Task
    """Return a Task object with matching task_id."""
    if not isinstance(task_id, int):
        raise TypeError('task_id must be an int')
    if _tasksdb is None:
        raise UninitializedDatabase()
    task_dict = _tasksdb.get(task_id)
    return Task(**task_dict)


def list_tasks(owner=None):  # type: (str|None) -> list of Task
    """Return a list of Task objects."""
    if owner and not isinstance(owner, string_types):
        raise TypeError('owner must be a string')
    if _tasksdb is None:
        raise UninitializedDatabase()
    return [Task(**t) for t in _tasksdb.list_tasks(owner)]


def count():  # type: (None) -> int
    """Return the number of tasks in db."""
    if _tasksdb is None:
        raise UninitializedDatabase()
    return _tasksdb.count()


def update(task_id, task):  # type: (int, Task) -> None
    """Modify task in db with given task_id."""
    if not isinstance(task_id, int):
        raise TypeError('task_id must be an int')
    if not isinstance(task, Task):
        raise TypeError('task must be Task object')
    if _tasksdb is None:
        raise UninitializedDatabase()
    current_task = _tasksdb.get(task_id)
    updates = task._asdict()
    for field in task._fields:
        if field != 'id' and updates[field] is not None:
            current_task[field] = updates[field]
    _tasksdb.update(task_id, current_task)


def delete(task_id):  # type: (int) -> None
    """Remove a task from db with given task_id."""
    if not isinstance(task_id, int):
        raise TypeError('task_id must be an int')
    if _tasksdb is None:
        raise UninitializedDatabase()
    _tasksdb.delete(task_id)


def delete_all():  # type: () -> None
    """Remove all tasks from db."""
    if _tasksdb is None:
        raise UninitializedDatabase()
    _tasksdb.delete_all()


def unique_id():  # type: () -> int
    """Return an integer that does not exist in the db."""
    if _tasksdb is None:
        raise UninitializedDatabase()
    return _tasksdb.unique_id()


_tasksdb = None


def start_tasks_db(db_path, db_type):  # type: (str, str) -> None
    """Connect API functions to a db."""
    if not isinstance(db_path, string_types):
        raise TypeError('db_path must be a string')
    global _tasksdb
    if db_type == 'tiny':
        import tasks.tasksdb_tinydb
        _tasksdb = tasks.tasksdb_tinydb.start_tasks_db(db_path)
    elif db_type == 'mongo':
        import tasks.tasksdb_pymongo
        _tasksdb = tasks.tasksdb_pymongo.start_tasks_db(db_path)
    else:
        raise ValueError("db_type must be a 'tiny' or 'mongo'")


def stop_tasks_db():  # type: () -> None
    """Disconnect API functions from db."""
    global _tasksdb
    _tasksdb.stop_tasks_db()
    _tasksdb = None
