from pathlib import Path
from enum import auto

import dotenv
from pydantic import BaseSettings

from utils.tools.str_enum import StrEnum


BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = Path(BASE_DIR, 'images')
IMAGES_DIR.mkdir(exist_ok=True)


class Settings(BaseSettings):
    PORT: int = 8011
    IS_DEBUG: bool = False

    TITLE: str = 'Image Service'
    VERSION: str = '0.1.0'

    ALLOWED_IMAGE_TYPES = {
        'image/jpeg',
        'image/png',
        'image/tiff'
    }

    class Config:
        env_file = Path(BASE_DIR, '.env')
        dotenv.load_dotenv(env_file)


settings = Settings()


class FileSizes(StrEnum):
    original = auto()
    small = auto()
    medium = auto()


FILE_SIZES = {
    FileSizes.original: (None, None),
    FileSizes.small: (150, 150),
    FileSizes.medium: (500, 500)
}
