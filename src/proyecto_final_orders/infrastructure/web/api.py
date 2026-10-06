from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List, Any

from proyecto_final_orders.infrastructure.web.schemas import OrderItemCreate, OrderResponse
from proyecto_final_orders.infrastructure.web.security import get_current_user
from proyecto_final_orders.infrastructure.database.repositories import SQLAlchemyUnitOfWork
from proyecto_final_orders.application.use_cases import CreateOrderUseCase

router = APIRouter(prefix="/orders", tags=["Órdenes"])

engine = create_engine("sqlite:///orders.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_uow() -> SQLAlchemyUnitOfWork:
    return SQLAlchemyUnitOfWork(SessionLocal)

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(
    items: List[OrderItemCreate],
    uow: SQLAlchemyUnitOfWork = Depends(get_uow),
    current_user: str = Depends(get_current_user)
) -> Any:
    use_case = CreateOrderUseCase(uow)
    
    try:
        items_data = [item.model_dump() for item in items]
        
        order = use_case.execute(customer_id=current_user, items_data=items_data)
        return order
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))