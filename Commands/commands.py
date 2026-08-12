from Commands.system import (
    help_command,
    identity_command,
    mission_command
)

from Commands.projects import (
    projects_command
)

from Commands.journal import (
    journal_command,
    journal_view_command
)

from Commands.workshop import (
    welcome_command,
    reflect_command,
    health_command,
    record_command
)

from Commands.tasks import (
    tasks_command,
    add_task_command,
    complete_task_command,
)

from Commands.memory import (
    remember_moment_command,
    garden_command
)

from Commands.search import (
    search_command,
)

from Commands.work import (
    work_command,
    end_work_command
)

COMMANDS = {
    "help": help_command,
    "identity": identity_command,
    "mission": mission_command,
    "welcome": welcome_command,
    "projects": projects_command,
    "record": record_command,
    "journal": journal_command,
    "view journal": journal_view_command,
    "reflect": reflect_command,
    "health": health_command,
    "tasks": tasks_command,
    "add task": add_task_command,
    "complete task": complete_task_command,
    "remember moment": remember_moment_command,
    "garden": garden_command,
    "search": search_command,
    "work": work_command,
    "end work": end_work_command
}