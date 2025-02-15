"""
First, of course, you can mix Path, Query and request body parameter declarations freely and FastAPI will know what to do.

And you can also declare body parameters as optional, by setting the default to None:
"""

#
# from typing import Annotated
#
# from fastapi import FastAPI, Path, Body
# from pydantic import BaseModel
#
# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[
#         int, Path(title="The ID of the item to get", ge=0, le=1000)
#     ],
#     q: str | None = None,
#     item: Item | None = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results

"""

you can also declare multiple body parameters, e.g. item and user:

"""

#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results

"""
The same way there is a Query and Path to define extra data for query and path parameters, FastAPI provides an equivalent Body.

For example, extending the previous model, you could decide that you want to have another key importance in the same body, besides the item and user.

If you declare it as is, because it is a singular value, FastAPI will assume that it is a query parameter.

But you can instruct FastAPI to treat it as another body key using Body:
"""


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
# ):
#     results = {
#         "item_id": item_id,
#         "item": item,
#         "user": user,
#         "importance": importance,
#     }
#     return results


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#

# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: Annotated[int, Body(gt=0)],
#     q: str | None = None,
# ):
#     results = {
#         "item_id": item_id,
#         "item": item,
#         "user": user,
#         "importance": importance,
#     }
#     if q:
#         results.update({"q": q})
#     return results
