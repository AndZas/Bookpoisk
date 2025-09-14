from typing import Dict, List
from server.api.schemas import Request, Response, Book


def convert_request(data: Request) -> Dict:
    read_books = [f"{i.title} - {i.author}" for i in data.read_books]
    all_books = [f"{i.title} - {i.author}" for i in data.all_books]
    return {"read_books": read_books, "all_books": all_books}


def convert_response(data: List) -> Response:
    recommended_books = [Book(id="", title=i.split(" - ")[0], author=i.split(" - ")[1], year="", description="",
                              genre="", pages=0) for i in data]
    return Response(recommended_books=recommended_books)
