class AppStore:
    applications = []

    @classmethod
    def add_application(cls, app):
        cls.applications.append(app)

    @classmethod
    def remove_application(cls, app):
        cls.applications.remove(app)

    def block_application(self, app):
        self.blocked = True

    @classmethod
    def total_apps(cls):
        return len(cls.applications)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
