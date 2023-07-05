from datetime import datetime
from pydantic import BaseModel
from typing import Optional


# Pydantic models
class OrderBase(BaseModel):
    customer: str
    product: str
    quantity: int
    orderDate: Optional[datetime]
    dueDate: Optional[datetime]
    status: str
    priority: int
    productionLine: Optional[str]
    cost: Optional[float]
    price: Optional[float]


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer: Optional[str]
    product: Optional[str]
    quantity: Optional[int]
    orderDate: Optional[datetime]
    dueDate: Optional[datetime]
    status: Optional[str]
    priority: Optional[int]
    productionLine: Optional[str]
    cost: Optional[float]
    price: Optional[float]


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True


orders: list[Order] = []
order1 = Order(
    id=1,
    customer="小明",
    product="轴承",
    quantity=100,
    orderDate=datetime.now(),
    dueDate=datetime.now(),
    status="Received",
    priority=1,
    productionLine="Line1",
    cost=500.0,
    price=1000.0,
)
order2 = Order(
    id=2,
    customer="小孙",
    product="激光传感器",
    quantity=200,
    orderDate=datetime.now(),
    dueDate=datetime.now(),
    status="In Production",
    priority=1,
    productionLine="Line2",
    cost=1000.0,
    price=2000.0,
)
orders.append(order1)
orders.append(order2)


def get_orders():
    print("正在获取订单列表...")
    return orders


def create_order(order: OrderCreate):
    print("正在创建新订单...")
    new_order = Order(id=len(orders) + 1, **order.dict())
    orders.append(new_order)
    return new_order


def get_order(id: int):
    print(f"正在获取订单 {id}")
    # Here, you'd actually pull the order from your database using the id.
    for order in orders:
        if order.id == id:
            return order
    raise ValueError(f"订单 {id} 未找到")


def update_order(id: int, order: OrderUpdate):
    print(f"正在更新订单 {id}")
    for i, old_order in enumerate(orders):
        if old_order.id == id:
            updated_data = old_order.dict()  # get dict representation of the old order
            updated_data.update(
                order.dict(exclude_unset=True)
            )  # update it with new values, excluding unset ones
            updated_order = Order(
                **updated_data
            )  # create a new Order instance from updated data
            orders[i] = updated_order  # replace the old Order instance with the new one
            return updated_order
    raise ValueError(f"订单 {id} 未找到")


def delete_order(id: int):
    print(f"正在删除订单 {id}")
    # Here, you'd actually delete the order from your database using the id.
    for i, order in enumerate(orders):
        if order.id == id:
            return orders.pop(i)
    raise ValueError(f"订单 {id} 未找到")
