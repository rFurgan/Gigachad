class Option:
    def __init__(self, name, path, cwd, args, env):
        self.edit = False
        self.name = name
        self.path = path
        self.cwd = cwd
        self.args = args
        self.env = env

    def get(self):
        return {
            "name": self.name,
            "cwd": self.cwd,
            "args": self.args,
            "env": self.env,
        }