from fastapi import Query, APIRouter
from fastapi.responses import JSONResponse
import sqlite3

router = APIRouter()


@router.get("/users")
def read_items_by_name(id_: int = Query(...)):
    """
    Gets items from the database based on the name
    """
    conn = sqlite3.connect("mydatabase.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE id='{id_}'")
    items = c.fetchall()
    conn.close()
    return JSONResponse(content={"items": items})


@router.get("/users_bind")
def read_items_by_id(id_: int = Query(...)):
    """
    Gets an item from the database based on the ID
    """
    # This is vulnerable to SQL Injection (Blind)
    conn = sqlite3.connect("mydatabase.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE id={id_}")
    items = c.fetchall()
    conn.close()
    if items:
        return 'Yes'
    return 'No'
