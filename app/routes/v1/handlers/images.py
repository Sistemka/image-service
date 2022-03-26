from uuid import UUID
from pydantic import BaseModel

from fastapi import APIRouter, status, UploadFile, File, HTTPException
from fastapi.responses import FileResponse

from services.v1.images import ImagesService
from settings import FileSizes

router = APIRouter()


class AddImage(BaseModel):
    image_id: UUID
    detail: str


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=AddImage
)
async def add_image(
        file: UploadFile = File(...),
):
    service = ImagesService()
    is_image = service.is_file_image(file)
    if not is_image:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='invalid image')

    image_id = await service.add_image(file)
    return AddImage(image_id=image_id, detail='image has been added')


@router.get(
    '/{size}/{image_id}',
)
def get_image(
        image_id: UUID,
        size: FileSizes = FileSizes.original
):
    service = ImagesService()

    image_path = service.get_image(image_id=image_id, size=size)
    if not image_path:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no such image')
    return FileResponse(path=image_path)
