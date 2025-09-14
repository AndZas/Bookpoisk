from fastapi import APIRouter
from server.api.schemas import Request, Response
from server.parsers.converters import convert_response, convert_request

router = APIRouter()


@router.post("/model", response_model=Response)
async def model(data: Request) -> Response:
    answer = convert_response(["Мастер и Маргарита - Михаил Булгаков", "1984 - Джордж Оруэлл"])
    return answer
