from pathlib import Path
from uuid import uuid4

import pytest
from PIL import Image
from fastapi import UploadFile

from settings import BASE_DIR
from tests.mocks import DiskFileStorageMock
from services.v1.images import ImagesService


@pytest.fixture()
def image_path() -> Path:
    return Path(BASE_DIR, 'tests', 'data', 'test.jpg')


@pytest.fixture(scope='function')
def upload_file_image(image_path) -> UploadFile:
    with open(image_path, 'rb') as f:
        file = UploadFile(filename='test.jpg', file=f, content_type='image/jpg')
        yield file


@pytest.fixture()
def image_pil(image_path) -> Image:
    return Image.open(image_path)


@pytest.fixture()
def image_id() -> uuid4:
    return uuid4()


@pytest.fixture()
def disk_file_storage_mock():
    return DiskFileStorageMock()


@pytest.fixture()
def image_service(disk_file_storage_mock):
    return ImagesService(file_storage=disk_file_storage_mock)
