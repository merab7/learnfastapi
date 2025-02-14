from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

#
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="the id of the item to get")],
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ):
#     result = {"item_id": item_id}
#     if q:
#         result.update({"q": q})
#     return result


"""
A path parameter is always required as it has to be part of the path. Even if you declared it with None or set a default value, it would not affect anything, it would still be always required
"""


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)],
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


"""
ge: greater or equal
gt: greater than
le: less than or equal
"""
