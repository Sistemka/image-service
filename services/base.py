from utils.file_storage.disk_file_storage import DiskFileStorage


class BaseService:
    def __init__(self):
        self.file_storage = DiskFileStorage()
