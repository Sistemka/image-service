import pytest

from utils.resize_image import resize_image


@pytest.mark.parametrize(
    'width,height', [
        (100, 2000),
        (2000, 1051),
    ])
def test_resize_image(image_pil, width, height):
    image = resize_image(image_pil, width=width, height=height)
    image_w, image_h = image.size
    assert image_w == width
    assert image_h == height
