from typing import Union

from fastapi import FastAPI

import liuli_scrap
import liuli_info

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/liuli/list")
def read_liuli_list(url: str):
    global info_list
    soup = liuli_scrap.get_request_content(url=url)
    if soup != '' or soup is not None:
        info_list = liuli_scrap.get_news_list(soup=soup)
    return info_list

@app.get("/liuli/info")
def read_liuli_info(url: str):
    soup = liuli_scrap.get_request_content(url=url)
    if soup != '' or soup is not None:
        info = liuli_info.get_liuli_info(soup)
    return info
