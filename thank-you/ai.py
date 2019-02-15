class Agent():
    def __init__(self):
        self.actions = {}

    def action(self, likelihood=1):
        """Marks an action that the current agent can do

        @param likelihood - Higher numbers mean more likely. Must be a whole number.
        """

        this = self

        def func(fn):
            this.actions[fn] = likelihood

            return fn
        return func
