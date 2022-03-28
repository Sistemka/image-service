import io
from uuid import UUID, uuid4
from pathlib import Path

from fastapi import UploadFile
from PIL import Image

from services.base import BaseService
from settings import settings, FILE_SIZES, FileSizes
from utils.resize_image import resize_image


class ImagesService(BaseService):

    @staticmethod
    def is_file_image(file: UploadFile) -> bool:
        if file.content_type in settings.ALLOWED_IMAGE_TYPES:
            return True
        return False

    async def add_image(self, image: UploadFile) -> str:
        image_id = str(uuid4())

        content = await image.read()
        image = Image.open(io.BytesIO(content))

        for size, (width, height) in FILE_SIZES.items():
            if size == FileSizes.original:
                resized_image = image
            else:
                resized_image = resize_image(image=image, width=width, height=height)

            self.file_storage.set(key=image_id, size=size, file=resized_image)

        return image_id

    def get_image(self, image_id: UUID, size: FileSizes) -> [Path, None]:
        return self.file_storage.get(key=str(image_id), size=size)
