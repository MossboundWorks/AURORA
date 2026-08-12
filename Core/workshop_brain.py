import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

PERSONALITY_FILE = os.path.join(
    BASE_DIR,
    "Config",
    "personality.json"
)

USER_FILE = os.path.join(
    BASE_DIR,
    "Config",
    "user.json"
)

from datetime import datetime

from Core.session_manager import SessionManager

from Core.session_controller import SessionController

class WorkshopBrain:

    def __init__(self):

        self.memory = {}
        self.projects = {}
        self.tasks = {}
        self.journal = {}
        self.personality = {}
        self.user = {}

        self.session_controller = SessionController()
        self.session_manager = self.session_controller.manager

        self.awaken()

    def load_json(self, path):

        if os.path.exists(path):

            with open(path, "r") as file:

                return json.load(file)

        return {}


    def awaken(self):

        self.memory = self.load_json(
            os.path.join(
                BASE_DIR,
                "Memory",
                "milestones.json"
            )
        )

        self.projects = self.load_json(
            os.path.join(
                BASE_DIR,
                "Memory",
                "projects.json"
            )
        )

        self.tasks = self.load_json(
            os.path.join(
                BASE_DIR,
                "Memory",
                "tasks.json"
            )
        )

        self.journal = self.load_json(
            os.path.join(
                BASE_DIR,
                "Memory",
                "workshop_journal.json"
            )
        )

        self.personality = self.load_json(
            PERSONALITY_FILE
        )

        self.user = self.load_json(
            USER_FILE
        )
    
    def get_projects(self):

        return self.projects.get(
            "projects",
            []
        )
    
    def find_project(self, name):

        projects = self.get_projects()

        for project in projects:

            if project["name"] == name:

                return project
            
    def get_project_tasks(self, project_name):

        tasks = self.tasks.get(
            "tasks",
            []
        )

        project_tasks = []

        for task in tasks:

            if task.get("project") == project_name:

                project_tasks.append(task)

        return project_tasks

    def get_tasks(self):

        return self.tasks.get(
            "tasks",
            []
        )

    def get_completed_tasks(self):

        completed_tasks = []

        for task in self.get_tasks():

            if task.get("completed", False):

                completed_tasks.append(task)

        return completed_tasks

    def get_completed_tasks(self):

        completed_tasks = []

        for task in self.get_tasks():

            if task.get("completed", False):

                completed_tasks.append(task)

        return completed_tasks

    def save_tasks(self):

        task_file = os.path.join(
            BASE_DIR,
            "Memory",
            "tasks.json"
        )

        with open(task_file, "w") as file:

            json.dump(
                self.tasks,
                file,
                indent=4
            )

    def add_task(self, task):

        if "tasks" not in self.tasks:

            self.tasks["tasks"] = []

        self.tasks["tasks"].append(
            task
        )

        self.save_tasks()

    def complete_task(self, task):

        for saved_task in self.get_tasks():

            if (
                saved_task["title"] == task["title"]
                and
                saved_task["project"] == task["project"]
            ):

                saved_task["completed"] = True
                saved_task["status"] = "Completed"

                break

        self.save_tasks()
    

    def update_task(self, old_task, updated_task):

        for index, saved_task in enumerate(self.get_tasks()):

            if (
                saved_task["title"] == old_task["title"]
                and
                saved_task["project"] == old_task["project"]
            ):

                updated_task["created"] = saved_task.get(
                    "created",
                    "Unknown"
                )

                updated_task["completed"] = saved_task.get(
                    "completed",
                    False
                )

                updated_task["status"] = saved_task.get(
                    "status",
                    "Not Started"
                )

                self.tasks["tasks"][index] = updated_task

                self.save_tasks()

                return
            
    def recommend_next_task(self):

        tasks = self.tasks.get(
            "tasks",
            []
        )

        unfinished = []

        for task in tasks:

            if not task.get(
                "completed",
                False
            ):

                unfinished.append(task)

        if not unfinished:

            return None
        
        priority_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3
        }

        unfinished.sort(
            key=lambda task: priority_order.get(
                task.get("priority", "Low"),
                3
            )
        )

        return unfinished[0]

    def get_next_action(self):

        task = self.recommend_next_task()

        
        if not task:

            return {
                "task": None, 
                "reason": "No unfinshed tasks found."
            }
        
        project = self.find_project(
            task["project"]
        )

        project_type: "Unknown"


        project_type = "Unknown"

        if project:
            project_type = project.get(
                "type",
                "Unknown"
            )

        reason = (
            f"This is a {task['priority']} priority task "
            f"connected to {task['project']}, "
            f"a {project_type} project."
        )
        return {
            "task": task,
            "reason": reason
        }

    def get_system_summary(self):

        action = self.get_next_action()

        summary = {

            "projects": len(
                self.get_projects()
            ),

             "tasks": len(
                 self.tasks.get(
                     "tasks",
                     []
                 )
             ),

             "current_focus": None,

             "project": None,

             "reason": None
        }

        if action["task"]:

            summary["current_focus"] = (
                action["task"]["title"]
            )

            summary["project"] = (
                action["task"]["project"]
            )

            summary["reason"] = (
                action["reason"]
            )

        return summary

    def write_journal_entry(self, project, focus, accomplishment, next_step):

        if "entries" not in self.journal:

            self.journal["entries"] = []

        entry = {

            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),

            "project": project,

            "focus": focus, 

            "accomplishment": accomplishment,

            "next_step": next_step
        }

        self.journal["entries"].append(
            entry
        )


        journal_file = os.path.join(
            BASE_DIR,
            "Memory",
            "workshop_journal.json"
        )

        with open(journal_file, "w") as file:

            json.dump(
                self.journal,
                file,
                indent=4
            )
        
        return entry

    def get_project_history(self, project_name):

        sessions = self.session_manager.get_sessions()

        history = []

        for session in sessions:

            if session.get("project") == project_name:

                history.append(session)

            return history

    def get_last_session(self):

        return self.session_manager.get_last_session()

    def get_current_work(self):

        return self.session_controller.get_work_context()

    def start_work(
            self, 
            project, 
            task=None
    ):

        return self.session_controller.begin_work(
            project,
            task
        )

    def finish_work(
        self,
        accomplishments=None,
        next_step=""
    ):

        session = self.session_controller.finish_work(
            accomplishments,
            next_step
        )

        if not session:

            return None

        self.record_session()

        return session

    def get_work_status(self):

        session = self.session_controller.get_work_context()

        if not session:
            return None

        return session

    def get_work_status(self):

        work = self.get_current_work()

        if not work:

            return (
                "No active work session."
            )

        project = work.get(
            "project",
            "Unknown Project"
        )

        task = work.get(
            "task"
        )

        started = work.get(
            "started",
            "Unknown"
        )

        status = work.get(
            "status",
            "Unknown"
        )

        report = []

        report.append(
            "Current Work"
        )

        report.append("")

        report.append(
            f"Project: {project}"
        )

        if task:

            report.append(
                f"Task: {task}"
            )

        report.append(
            f"Started: {started}"
        )

        report.append(
            f"Status: {status}"
        )

        return "\n".join(report)

    def record_session(self):

        session = self.session_manager.get_last_session()

        if not session:

            return None

        session_id = session.get(
            "id"
        )

        journal = self.journal

        if "entries" not in journal:

            journal["entries"] = []

        for entry in journal["entries"]:

            if entry.get("session_id") == session_id:

                return entry

        accomplishments = session.get(
            "accomplishments",
            []
        )

        if accomplishments:

            accomplishment = ", ".join(
                str(item)
                for item in accomplishments
            )

        else:

            accomplishment = ""

        entry = {

            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),

            "session_id": session_id,

            "project": session.get(
                "project",
                "Unknown"
            ),

            "focus": session.get(
                "task",
                "Unknown"
            ),

            "accomplishment": accomplishment,

            "next_step": session.get(
                "next_step",
                ""
            )
        }

        journal["entries"].append(
            entry
        )

        journal_file = os.path.join(
            BASE_DIR,
            "Memory",
            "workshop_journal.json"
        )

        with open(
            journal_file,
            "w"
        ) as file:

            json.dump(
                journal,
                file,
                indent=4
         )

        self.journal = journal

        return entry

    def get_identity(self):

        return self.personality.get(
            "identity",
            {}
    )

    def get_user(self):

        return self.user.get(
            "preferred_name",
            self.user.get(
                "name",
                "User"
            )
        )
    
    def get_creator(self):

        return self.personality.get(
            "creator",
            "Unknown"
        )
    
    def get_mission(self):

        return self.personality.get(
            "mission",
            {}
        )
    
    def get_project_activity(self):

        sessions = self.session_manager.get_sessions()

        activity = {}

        for session in sessions:

            project = session.get("project")


            activity[project] = (
                activity.get(project, 0) + 1
            )

        return activity
    
    def make_observation(self):

        activity = self.get_project_activity()

        observations = []


        if not activity:

            observations.append(
                "No workshop activity recorded yet."
            )

            return observations
        
        most_active = max(
            activity,
            key=activity.get
        )


        sessions = activity[most_active]

        observations.append(
            f"Your most active project is {most_active}."
        )

        observations.append(
            f"The Workshop has recorded {sessions} session(s) for this project."
        )

        return observations
    
    def give_recommendation(self):

        activity = self.get_project_activity()

        recommendations = []


        if not activity:

            recommendations.append(
                "Start a project session so I can learn your patterns."
            )

            return recommendations
        
        most_active = max(
            activity,
            key=activity.get
        )

        count = activity[most_active]

        recommendations.append(
            f"You have been focusing most on {most_active}."
        )

        if most_active == "Aurora":

            recommendations.append(
            "Your assistant systems are actively growing. Continue strengthening her foundation."
        )
            
        elif most_active == "Faerie Veil":

            recommendations.append(
                "Your creative world is calling. Consider developing the next piece of the story."
            )


        else:

            recommendations.append(
                f"Consider continuing progress on {most_active} while your momentum is strong."
            )


        return recommendations
    
    def get_recommendation_reason(self):

        activity = self.get_project_activity()

        if not activity:

            return (
                "I need more Workshop history "
                "before I can recognize patterns."
            )


        most_active = max(
            activity,
            key=activity.get
        )


        sessions = activity[most_active]


        return (
            f"I noticed that {most_active} "
            f"has been your most active project "
            f"with {sessions} recorded session(s). "
            "This suggests it is currently your strongest focus."
        )
    
    def format_response(self, message):

        identity = self.get_identity()

        voice_style = identity.get(
            "voice_style",
            "warm and helpful"
        )

        if "British" in voice_style:

            return (
                f"{self.get_user()}, {message}"
            )
        
        return message
    
    def get_workshop_summary(self):

        summary = []


        identity = self.get_identity()

        summary.append(
            f"Aurora Identity: {identity.get('role', 'Unknown')}"
        )


        summary.append("")


        if self.projects:

            summary.append(
            "Active Projects:"
            )

            for project in self.projects.get("projects", [])[:3]:

                summary.append(
                    f"   {project['name']}"
                )


        summary.append("")


        tasks = self.tasks.get(
            "tasks",
            []
        )


        if tasks:

            summary.append(
                "Current Tasks:"
            )

        for task in tasks[:3]:

            summary.append(
                f"   {task['title']}"
            )


        summary.append("")


        observations = self.make_observation()

        summary.append(
            "Workshop Observation:"
        )


        for observation in observations:

            summary.append(
                f"   {observation}"
            )


        summary.append("")


        recommendations = self.give_recommendation()

        summary.append(
            "Recommendation:"
        )


        for recommendation in recommendations:

            summary.append(
                f"   {recommendation}"
            )


        return summary
    
    def get_welcome_back(self):

        session = self.get_last_session()

        if not session:

            return (
                "Welcome back, {self.get_user()}. "
                "The Workshop is ready for a new beginning."
            )


        project = session.get(
            "project",
            "Unknown Project"
        )

        task = session.get(
            "task"
        )

        accomplishments = session.get(
            "accomplishments",
            []
        )

        next_step = session.get(
            "next_step",
            ""
        )

        status = session.get(
            "status",
            "Unknown"
        )


        message = (
            f"Welcome back, {self.get_user()}.\n\n"
            f"Last Workshop Session:\n"
            f"Project: {project}\n"
        )


        if task:

            message += (
                f"Task: {task}\n"
            )


        if status:

            message += (
                f"Status: {status}\n"
            )


        if accomplishments:

            message += "\nAccomplished:\n"

            for accomplishment in accomplishments:

                message += (
                    f"• {accomplishment}\n"
            )   


        if next_step:

            message += (
                f"\nNext Step:\n"
                f"{next_step}\n"
            )


        message += (
            "\nThe Workshop is ready to continue growing."
        )


        return message
    
    def health_check(self):

        checks = {
            
            "Memory": bool(
                self.memory.get(
                    "milestones",
                    []
                )
            ),

            "Projects": bool(
                self.projects.get(
                    "projects",
                    []
                )
            ),

            "Tasks": bool(
                self.tasks.get(
                    "tasks",
                    []
                )
            ),

            "Sessions": bool(
                self.session_manager.get_sessions()
            ),

            "Personality": bool(
                self.personality
            )
        }

        return checks

    def delete_task(self, task):

        self.tasks["tasks"] = [

            saved_task

            for saved_task in self.get_tasks()

            if not (

                saved_task["title"] == task["title"]

                and

                saved_task["project"] == task["project"]
            )
        ]

        self.save_tasks()

    def get_available_work(self):

        tasks = self.tasks.get(
            "tasks",
            []
        )

        available = []

        for task in tasks:

            if task.get("completed") is True:
                continue

            if task.get("status") == "Completed":
                continue

            available.append(task)

        return available

    def select_work(self):

        tasks = self.get_available_work()

        if not tasks:

            return None

        print()
        print("Available work:")
        print()

        for index, task in enumerate(tasks, start=1):

            project = task.get(
                "project",
                "Unknown Project"
            )

            priority = task.get(
                "priority",
                "Unknown"
            )

            print(
                f"{index}. "
                f"{task.get('title', 'Untitled')} "
                f"[{project} | {priority}]"
            )

        print()

        choice = input(
            "Select a task: "
        ).strip()

        if not choice.isdigit():

            return None

        index = int(choice) - 1

        if index < 0 or index >= len(tasks):

            return None

        return tasks[index]

# =========================================
# TEST THE WORKSHOP BRAIN
# =========================================

if __name__ == "__main__":

    brain = WorkshopBrain()

    brain.awaken()

    print("✨ Identity:")
    print(brain.get_identity())

    print()

    print("🌱 Creator:")
    print(brain.get_creator())

    print()

    print("🌙 Mission:")
    mission = brain.get_mission()

    print(f"✨ {mission['primary']}")

    for goal in mission["secondary"]:
        print(f"🌱 {goal}")

    print()

    activity = brain.get_project_activity()

    print("📚 Workshop Activity")

    print()

    for project, count in activity.items():
        print(f"✨ {project}: {count} session(s)")

    print()

    print("🌿 Aurora Observations")

    print()

    for observation in brain.make_observation():

        print(observation)

    print()

    print("💡 Aurora Recommendations")

    print()

    for recommendation in brain.give_recommendation():

        print(recommendation)

    print()

    print("🧠 Aurora Reasoning")

    print()

    print(
        brain.get_recommendation_reason()
    )

    print()

    print("✨ Aurora Voice Test")

    print()

    print(
        brain.format_response(
            "the Workshop is ready for today's creation."
        )
    )

    print()

    print("🌙 Aurora Workshop Summary")

    print()

    for line in brain.get_workshop_summary():

        print(line)

    print()

    print("🌿 Aurora Welcome")

    print()

    print(
        brain.get_welcome_back()
    )

    print()

    print("🔎 Projects Debug")

    print(brain.projects)

    print()

    print("⚙ Aurora Health Check")

    for system, status in brain.health_check().items():

        symbol = "✅" if status else "❌"

        print(
            f"{symbol} {system}"
        )

    print()

    print("Task Test")

    print()

    for task in brain.get_tasks():

        print(task["title"])

    print()

    print("Completed Tasks")

    print()

    for task in brain.get_completed_tasks():

        print(task["title"])

    print()

    print("👤 User Test:")

    print(
        brain.get_user()
    )