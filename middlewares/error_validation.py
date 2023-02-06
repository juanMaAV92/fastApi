
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code= 400,
        content=jsonable_encoder({"detail": exc.errors(), "Error": "Name field is missing"}),
    )
