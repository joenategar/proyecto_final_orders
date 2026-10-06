import uuid
from typing import List, Any
from proyecto_final_orders.domain.entities import Order, OrderItem
from proyecto_final_orders.application.ports import UnitOfWork

class CreateOrderUseCase:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    def execute(self, customer_id: str, items_data: List[dict[str, Any]]) -> Order:
        if not items_data:
            raise ValueError("La orden debe contener al menos un artículo.")

        items = [
            OrderItem(
                product_id=item["product_id"],
                quantity=item["quantity"],
                unit_price=item["unit_price"]
            )
            for item in items_data
        ]
        
        order = Order(
            id=str(uuid.uuid4()),
            customer_id=customer_id,
            items=items
        )

        with self.uow:
            self.uow.orders.save(order)
            self.uow.commit()

        return order