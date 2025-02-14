from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel, NonNegativeFloat
from typing import Annotated


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

#
# @app.get("/")
# async def root():
#     return {"message": "hellow world"}
#
#
# @app.get("/users/{user_name}")
# async def read_user(user_name: str):
#     return {"user_name": user_name}
#
#
# @app.get("/users/user_id/{user_id}")
# async def get_id(user_id: int):
#     return {"user_id": user_id}
#
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}
#


# Query Parameters¶
# When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.


# fake_items_db = [
#     {"item_name": "Foo"},
#     {"item_name": "Bar"},
#     {"item_name": "Baz"},
# ]
#
#
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


# optional parameters
# The same way, you can declare optional query parameters, by setting their default to None
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}
#
# Query parameter type conversion¶
# You can also declare bool types, and they will be converted:

#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "This is an amazing item that has a long description"
#             }
#         )
#     return item

# Required query parameters¶
# When you declare a default value for non-path parameters (for now, we have only seen query parameters), then it is not required.
#
# If you don't want to add a specific value but just make it optional, set the default as None.
#
# But when you want to make a query parameter required, you can just not declare any default value:


#
#
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item
#
# And of course, you can define some parameters as required, some as having a default value, and some entirely optional:
# @app.get("/items/{item_id}")
# async def read_user_item(
#     item_id: str, needy: str, skip: int = 0, limit: int | None = None
# ):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# # @app.post("/items")
# # async def create_item(item: Item):
# #     return item
#
#
# @app.post("items")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax is not None:
#         full_price = item.tax + item.price
#         item_dict.update({"full_price": full_price})
#     return item_dict


# @app.get("/items")
# async def read_item(q: Annotated[str | None, Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "foo"}, {" item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# i can use ellipsis(...) as a default and it is saying that this is required
# alo ... means that this variable is required and None can as well be sent as a
# value.
#
# @app.get("/items/")
# async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# i can declare that parameter can get multyple values by asign it to a list
# i can also declear multyple default values as a string = ["something1", "something2", "something3"]
# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query()] = None):
#     query_items = {"q": q}
#     return query_items


# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(
#             alias="item-query",
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#             max_length=50,
#             pattern="^Fixedquery$",
#             deprecated=True,
#         ),
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
