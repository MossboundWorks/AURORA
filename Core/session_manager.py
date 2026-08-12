import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

SESSION_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "workshop_sessions.json"
)

class SessionManager:

    def __init__(self):

        self.sessions = {
            "sessions": []
        }

        self.active_session = None

        self.load_sessions()

        self.restore_active_session()

    def load_sessions(self):

        if os.path.exists(SESSION_FILE):

            with open(
                SESSION_FILE,
                "r"
            ) as file:

                self.sessions = json.load(file)

        else:

            self.sessions = {
                "sessions": []
            }

    def restore_active_session(self):

        sessions = self.get_sessions()

        for session in reversed(sessions):

            if session.get("status") == "Active":

                self.active_session = session

                return

    def save_sessions(self):

        with open(
            SESSION_FILE,
            "w"
        ) as file:

            json.dump(
                self.sessions,
                file,
                indent=4
            )

    def start_session(
            self,
            project,
            task=None
    ):

        if self.active_session:

            return self.active_session

        now = datetime.now()

        session_id = now.strftime(
            "%Y-%m-%d-%H%M%S"
        )

        self.active_session = {

            "id": session_id,

            "project": project,

            "task": task,

            "started": now.strftime(
                "%Y-%m-%d %H:%M"
            ),

            "ended": None,

            "duration_minutes": None,

            "accomplishments": [],

            "next_step": "",

            "status": "Active"
        }

        self.sessions[
            "sessions"
        ].append(
            self.active_session
        )

        self.save_sessions()

        return self.active_session

    def end_session(
        self,
        accomplishments=None,
        next_step=""
    ):

        if not self.active_session:

            return None


        ended = datetime.now()

        started = datetime.strptime(
            self.active_session["started"],
            "%Y-%m-%d %H:%M"
        )


        duration = ended - started

        duration_minutes = round(
            duration.total_seconds() / 60
        )


        self.active_session["ended"] = (
            ended.strftime(
                "%Y-%m-%d %H:%M"
            )
        )


        self.active_session[
            "duration_minutes"
        ] = duration_minutes


        self.active_session[
            "accomplishments"
        ] = accomplishments or []


        self.active_session[
            "next_step"
        ] = next_step


        self.active_session[
            "status"
        ] = "Completed"


        session_id = self.active_session["id"]


        for index, session in enumerate(
            self.sessions["sessions"]
        ):

            if session.get("id") == session_id:

                self.sessions["sessions"][index] = (
                    self.active_session
                )

                break


        completed_session = (
            self.active_session
        )


        self.active_session = None


        self.save_sessions()


        return completed_session

    def get_active_session(self):

        return self.active_session

    def has_active_session(self):

        return self.active_session is not None

    def get_sessions(self):

        return self.sessions.get(
            "sessions",
            []
        )

    def get_last_session(self):

        sessions = self.get_sessions()


        if not sessions:

            return None

        return sessions[-1]

