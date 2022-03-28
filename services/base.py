from utils.file_storage.disk_file_storage import DiskFileStorage


class BaseService:
    def __init__(self, file_storage: DiskFileStorage = DiskFileStorage()):
        self.file_storage = file_storage
