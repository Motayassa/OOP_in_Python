class AppStore:
    applications = []

    @classmethod
    def add_application(cls, app):
        cls.applications.append(app)

    @classmethod
    def remove_application(cls, app):
        cls.applications.remove(app)

    def block_application(self, app):
        app.blocked = True

    @classmethod
    def total_apps(cls):
        return len(cls.applications)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.block_application(app_youtube)
print(app_youtube.__dict__)
print(AppStore.applications)
