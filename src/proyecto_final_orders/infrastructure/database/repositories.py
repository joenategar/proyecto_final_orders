from sqlalchemy.orm import Session
from proyecto_final_orders.domain.entities import Order, OrderItem
from proyecto_final_orders.infrastructure.database.models import OrderModel, OrderItemModel

class SQLAlchemyOrderRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, order: Order) -> None:
        db_order = OrderModel(
            id=order.id,
            customer_id=order.customer_id,
            status=order.status
        )
        for item in order.items:
            db_item = OrderItemModel(
                product_id=item.product_id,
                quantity=item.quantity,
                unit_price=item.unit_price
            )
            db_order.items.append(db_item)
        self.session.add(db_order)

    def get_by_id(self, order_id: str) -> Order | None:
        # Simplificado; en un escenario real harías self.session.get(OrderModel, order_id)
        pass

class SQLAlchemyUnitOfWork:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.orders = SQLAlchemyOrderRepository(self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()