from typing import Protocol, Optional
from proyecto_final_orders.domain.entities import Order

class OrderRepository(Protocol):
    def save(self, order: Order) -> None:
        ...
        
    def get_by_id(self, order_id: str) -> Optional[Order]:
        ...

class UnitOfWork(Protocol):
    orders: OrderRepository
    
    def __enter__(self) -> 'UnitOfWork':
        ...
        
    def __exit__(self, exc_type: type, exc_val: Exception, exc_tb: type) -> None:
        ...
        
    def commit(self) -> None:
        ...
        
    def rollback(self) -> None:
        ...