from database import FileManagerObject


class Directory:
    directories = []
    files = []
    name: str

    def __init__(self, name: str):
        self.name = name
        self.find_new()

    def find_new(self):
        for i in FileManagerObject.select().where(FileManagerObject.previous == self.name).namedtuples():
            if i.is_file:
                self.files.append(i.name)
            else:
                self.directories.append(Directory(i.name))


class File:
    name: str

    def __init__(self, name: str):
        self.name = name
