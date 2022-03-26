from app.routes.v1.handlers import images
from utils.tools.routers import Router, compile_routers

routers = [
    Router(router=images.router, tags=['Images'], prefix='/images'),
]


compiled_routers = compile_routers(
    routers=routers,
    root_prefix='/api/v1'
)
