class Option:
    def __init__(self, name, cwd, args, env):
        self.edit = False
        self.options = {
            "name": name,
            "cwd": cwd,
            "args": args,
            "env": env,
        }
        self.options.update(env)
        self.max = len(self.options.keys())
