
from typing import List
from datetime import datetime
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException

# Assuming the above mentioned functions and models are already defined

def update_bearing_orders_cost_and_calculate_total_cost():
    orders = get_orders()
    bearing_orders = [order for order in orders if "轴承" in order.product]
    total_cost = 0

    for order in bearing_orders:
        new_cost = order.cost + 300
        order_update = OrderUpdate(cost=new_cost)
        update_order(order.id, order_update)
        total_cost += new_cost * order.quantity

    print("Total cost:", total_cost)
    return total_cost
