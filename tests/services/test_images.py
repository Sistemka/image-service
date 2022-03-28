import pytest

from settings import FILE_SIZES, FileSizes


def test_is_file_image(image_service, upload_file_image):
    is_image = image_service.is_file_image(file=upload_file_image)
    assert is_image is True


@pytest.mark.asyncio
async def test_add_image(image_service, upload_file_image):
    await image_service.add_image(image=upload_file_image)

    assert image_service.file_storage.set.called is True
    assert image_service.file_storage.set.call_count == len(FILE_SIZES)


def test_get_image(image_service, image_id):
    image_service.get_image(image_id=image_id, size=FileSizes.original)
    assert image_service.file_storage.get.called is True
