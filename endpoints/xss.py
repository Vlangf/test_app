from fastapi import Query, APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get('/search', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'
