############### 1. 모델 사용하기

# from fastapi import FastAPI
# from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# app = FastAPI()


# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax is not None:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

############### 2. 요청 본문 + 경로 매개변수
#FastAPI는 경로 매개변수와 일치하는 함수 매개변수가 경로에서 
# 가져와야 한다는 것을 인지하며, Pydantic 모델로 선언된 그 함수 
# 매개변수는 요청 본문에서 가져와야 한다는 것을 인지할 것입니다.
#

# from fastapi import FastAPI
# from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# app = FastAPI()


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

###### 요청 본문 + 경로 + 쿼리 매개변수¶
# 본문, 경로 그리고 쿼리 매개변수 모두 동시에 선언할 수도 있습니다.

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result