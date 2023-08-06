import random
from uuid import uuid4

import pytest
import sqlalchemy as sa
from task_flows.tables import task_errors_table, task_runs_table
from task_flows.task import TaskLogger


@pytest.fixture
def task():
    return TaskLogger(
        name=str(uuid4()),
        alert_slack=False,
        alert_email=False,
        alert_on_start=False,
        alert_on_error=False,
        alert_on_finish=False,
        required=False,
        exit_on_complete=False,
    )


def test_record_task_start(task, tables):
    task.record_task_start()
    query = sa.select(task_runs_table.c.task_name, task_runs_table.c.started).where(
        task_runs_table.c.task_name == task.task_name
    )
    with task.engine.begin() as conn:
        tasks = list(conn.execute(query).fetchall())
    assert len(tasks) == 1
    # name and started columns should be null.
    assert all(v is not None for v in tasks[0])


def test_record_task_error(task, tables):
    error = Exception(str(uuid4()))
    task.record_task_error(error)
    query = sa.select(task_errors_table).where(
        task_errors_table.c.task_name == task.name
    )
    with task.engine.begin() as conn:
        errors = list(conn.execute(query).fetchall())
    assert len(errors) == 1
    # no columns should be null.
    assert all(v is not None for v in errors[0])


def test_record_task_finish(task, tables):
    task.record_task_start()
    task.record_task_finish(
        success=random.choice([True, False]),
        retries=random.randint(0, 5),
        return_value=str(uuid4()),
    )
    query = sa.select(task_runs_table).where(task_runs_table.c.task_name == task.name)
    with task.engine.begin() as conn:
        tasks = list(conn.execute(query).fetchall())
    assert len(tasks) == 1
    # no columns should be null.
    assert all(v is not None for v in tasks[0])
