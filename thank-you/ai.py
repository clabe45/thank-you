curr_agent_actions = {}

def agent(cls):
    global curr_agent_actions

    # apply agent actions to cls (because this function is executed after the `@action` calls)
    cls.actions = curr_agent_actions
    curr_agent_actions = {}

    return cls

def action(likelihood=1):
    """Marks an action that the current agent can do

    @param likelihood - Higher numbers mean more likely. Must be a whole number.
    """

    def func(fn):
        curr_agent_actions[fn] = likelihood

        return fn
    return func
