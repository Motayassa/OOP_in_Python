CURRENT_OS = 'windows'   # 'windows', 'linux'


class FileDialogFactory:
    def __new__(cls, title, path, exts):
        if CURRENT_OS == 'windows':
            return cls.create_windows_filedialog(title, path, exts)
        if CURRENT_OS == 'linux':
            return cls.create_linux_filedialog(title, path, exts)

    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
