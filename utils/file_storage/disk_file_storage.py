from pathlib import Path

from PIL import Image

from utils.tools.singleton import Singleton
from settings import IMAGES_DIR, FileSizes


class DiskFileStorage(metaclass=Singleton):

    @staticmethod
    def set(key: str, size: FileSizes, file: Image) -> None:
        file_dir = Path(IMAGES_DIR, key)
        file_dir.mkdir(exist_ok=True)

        file_path = Path(file_dir, size.value)
        file.save(file_path, format=file.format)

    @staticmethod
    def get(key: str, size: FileSizes) -> [Path, None]:
        file_path = Path(IMAGES_DIR, key, size.value)
        if not file_path.exists():
            return
        return file_path
