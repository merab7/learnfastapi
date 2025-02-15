"""If you have a group of query
parameters that are related, you can create
a Pydantic model to declare them.

This would allow you to re-use the model in
multiple places and also to declare
validations and metadata for all the parameters at once. 😎
"""

from typing import Annotated, Literal

from fastapi import FastAPI, Query, Path
from fastapi.datastructures import Default
from pydantic import BaseModel, Field

app = FastAPI()
#
#
# class FilterParams(BaseModel):
#     limit: int = Field(100, gt=0, le=100)
#     offset: int = Field(0, ge=0)
#     order_by: Literal["created_at", "updated_at"] = "created_at"
#     tags: list[str] = []
#
#
# @app.get("/items/")
# async def read_items(filter_query: Annotated[FilterParams, Query()]):
#     return filter_query

"""

In some special use cases (probably not very common), you
might want to restrict
the query parameters that you want to receive.

You can use Pydantic's model configuration to forbid any extra fields:


"""

#
# class FilterParams(BaseModel):
#     model_config = {"extra": "forbid"}
#
#     limit: int = Field(100, gt=0, le=100)
#     offset: int = Field(0, ge=0)
#     order_by: Literal["created_at", "updated_at"] = "created_at"
#     tags: list[str] = []
#
#
# @app.get("/items/")
# async def read_items(filter_query: Annotated[FilterParams, Query()]):
#     return filter_query


class User(BaseModel):
    name: str
    description: str | None = None
    price: float | None = 2.5
    tax: float | None = None
    brand: list[str] = ["asus", "delly"]
    order_by: Literal["created_at", "updated_at"] = "created at"


@app.put("item/{item_id}")
async def updated_item(
    item_id: Annotated[
        int, Path(title="The ID of the item to get", ge=0, le=1000)
    ],
    q: Annotated[str, Query(title="this is query parameter", max_length=50)],
    user: User | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if user:
        results.update({"user": user})
    return results
