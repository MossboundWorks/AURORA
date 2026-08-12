from Core.session_manager import SessionManager


class SessionController:

    def __init__(self):

        self.manager = SessionManager()


    def get_active_session(self):

        return self.manager.get_active_session()


    def has_active_session(self):

        return self.manager.has_active_session()


    def begin_work(
        self,
        project,
        task=None
    ):

        active = self.manager.get_active_session()

        if active:

            return active

        return self.manager.start_session(
            project,
            task
        )


    def finish_work(
        self,
        accomplishments=None,
        next_step=""
    ):

        return self.manager.end_session(
            accomplishments,
            next_step
        )


    def get_work_context(self):

        session = self.get_active_session()

        if not session:

            return None

        return {
            "project": session.get(
                "project"
            ),

            "task": session.get(
                "task"
            ),

            "started": session.get(
                "started"
            ),

            "status": session.get(
                "status"
            )
        }