from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List

@dataclass
class OrderItem:
    product_id: str
    quantity: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return self.quantity * self.unit_price

@dataclass
class Order:
    id: str
    customer_id: str
    items: List[OrderItem]
    status: str = "PENDING"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @property
    def total_amount(self) -> float:
        return sum(item.subtotal for item in self.items)

    def mark_as_paid(self) -> None:
        self.status = "PAID"