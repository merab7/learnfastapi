"""
You can declare examples for a Pydantic model that will be added to the generated JSON Schema.
"""

from fastapi import Body, FastAPI
from pydantic import BaseModel
from pydantic.fields import Field
from typing import Annotated

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 }
#             ]
#         }
#     }
#
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results
#
#
class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, examples=["this is exampole of description"]
    )
    price: float
    tax: float | None = None

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "name": "Foo",
    #                 "description": "A very nice Item",
    #                 "price": 35.4,
    #                 "tax": 3.2,
    #             }
    #         ]
    #     }
    # }


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "this is example of name",
                    "price": "this is example of price",
                    "tax": "this is example of tax",
                }
            ]
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results
