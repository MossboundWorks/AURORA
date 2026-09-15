class NavigationController:

    def __init__(self, window, brain):

        self.window = window

        self.brain = brain

        self.current_view = None

        self.history = []

    def show(self, view_function, *args, **kwargs):

        if self.current_view is not None:

            self.history.append(

                (

                    self.current_view,

                    self.current_args,

                    self.current_kwargs

                )

            )

        self.current_view = view_function

        self.current_args = args

        self.current_kwargs = kwargs

        view_function(

            self.window,

            self.brain,

            *args,

            **kwargs

        )

    def back(self):

        if not self.history:

            return

        view_function, args, kwargs = self.history.pop()

        self.current_view = view_function

        self.current_args = args

        self.current_kwargs = kwargs

        view_function(

            self.window,

            self.brain,

            *args,

            **kwargs

        )

    def go_to_workshop(self):

        from Interface.workshop_dashboard import show_dashboard

        self.history.clear()

        self.current_view = show_dashboard

        self.current_args = ()

        self.current_kwargs = {}

        show_dashboard(

            self.window,

            self.brain

        )