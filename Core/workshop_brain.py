import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

SESSION_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "workshop_sessions.json"
)

PERSONALITY_FILE = os.path.join(
    BASE_DIR,
    "Config",
    "personality.json"
)

from datetime import datetime

class WorkshopBrain:

    def __init__(self):

        self.memory = {}
        self.projects = {}
        self.tasks = {}
        self.journal = {}
        self.sessions = {}
        self.personality = {}


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
                "moments.json"
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

        self.sessions = self.load_json(
            SESSION_FILE
        )

        self.personality = self.load_json(
            PERSONALITY_FILE
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

                updated_task["due_date"] = saved_task.get(
                    "due_date",
                    ""
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

            "high": 1, 
            "High": 1,

            "medium": 2,
            "Medium": 2,

            "low": 3,
            "Low":3
        }

        unfinished.sort(
            key=lambda task: priority_order.get(
                task.get("priority", "low"),
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

    def record_session(self, project, note):

        if "sessions" not in self.sessions:

            self.sessions["sessions"] = []


        session = {

            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),

            "project": project,

            "note": note
        }

        self.sessions["sessions"].append(
            session
        )

        with open(SESSION_FILE, "w") as file:

            json.dump(
                self.sessions,
                file,
                indent=4
            )

        return session
    
    def get_project_history(self, project_name):

        sessions = self.sessions.get(
            "sessions",
            []
        )

        history = []

        for session in sessions:

            if session.get("project") == project_name:

                history.append(session)


        return history

    def get_last_session(self):

        sessions = self.sessions.get(
            "sessions",
            []
        )

        if not sessions:

            return None
        
        return sessions [-1]
    
    def get_identity(self):

        return self.personality.get(
            "identity",
            {}
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

        sessions = self.sessions.get(
            "sessions",
            []
        )

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
                "🌱 No workshop activity recorded yet."
            )

            return observations
        
        most_active = max(
            activity,
            key=activity.get
        )


        sessions = activity[most_active]

        observations.append(
            f"🌿 Your most active project is {most_active}."
        )

        observations.append(
            f"✨ The Workshop has recorded {sessions} session(s) for this project."
        )

        return observations
    
    def give_recommendation(self):

        activity = self.get_project_activity()

        recommendations = []


        if not activity:

            recommendations.append(
                "🌱 Start a project session so I can learn your patterns."
            )

            return recommendations
        
        most_active = max(
            activity,
            key=activity.get
        )

        count = activity[most_active]

        recommendations.append(
            f"✨ You have been focusing most on {most_active}."
        )

        if most_active == "Aurora":

            recommendations.append(
            "🌿 Your assistant systems are actively growing. Continue strengthening her foundation."
        )
            
        elif most_active == "Faerie Veil":

            recommendations.append(
                "🦋 Your creative world is calling. Consider developing the next piece of the story."
            )


        else:

            recommendations.append(
                f"📚 Consider continuing progress on {most_active} while your momentum is strong."
            )


        return recommendations
    
    def get_recommendation_reason(self):

        activity = self.get_project_activity()

        if not activity:

            return (
                "🌱 I need more Workshop history "
                "before I can recognize patterns."
            )


        most_active = max(
            activity,
            key=activity.get
        )


        sessions = activity[most_active]


        return (
            f"🌿 I noticed that {most_active} "
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
                f"🌿 Moss, {message}"
            )
        
        return message
    
    def get_workshop_summary(self):

        summary = []


        identity = self.get_identity()

        summary.append(
            f"✨ Aurora Identity: {identity.get('role', 'Unknown')}"
        )


        summary.append("")


        if self.projects:

            summary.append(
            "📚 Active Projects:"
            )

            for project in self.projects.get("projects", [])[:3]:

                summary.append(
                    f"   ✨ {project['name']}"
                )


        summary.append("")


        tasks = self.tasks.get(
            "tasks",
            []
        )


        if tasks:

            summary.append(
                "📋 Current Tasks:"
            )

        for task in tasks[:3]:

            summary.append(
                f"   🌱 {task['title']}"
            )


        summary.append("")


        observations = self.make_observation()

        summary.append(
            "🌿 Workshop Observation:"
        )


        for observation in observations:

            summary.append(
                f"   {observation}"
            )


        summary.append("")


        recommendations = self.give_recommendation()

        summary.append(
            "💡 Recommendation:"
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
                "🌿 Welcome back, Moss. "
                "The Workshop is ready for a new beginning."
            )


        return (
            f"🌿 Welcome back, Moss.\n\n"
            f"📖 Last Workshop Memory:\n"
            f"You were working on {session['project']}.\n\n"
            f"✨ You:\n"
            f"{session['note']}\n\n"
            f"🌱 The Workshop is ready to continue growing."
        )
    
    def health_check(self):

        checks = {
            
            "Memory": bool(
                self.memory.get(
                    "moments",
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
                self.sessions.get(
                    "sessions",
                    []
                )
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

        print("📋 Task Test")

        print()

        for task in brain.get_tasks():

            print(task["title"])

    
