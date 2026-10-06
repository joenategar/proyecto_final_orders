from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from proyecto_final_orders.infrastructure.web.api import router as orders_router
from proyecto_final_orders.infrastructure.web.security import create_access_token

app = FastAPI(title="Orders Service API", version="1.0.0")

app.include_router(orders_router)

@app.post("/login", tags=["Autenticación"])
def login(form_data: OAuth2PasswordRequestForm = Depends()) -> dict[str, str]:
    if form_data.username != "admin" or form_data.password != "secreto":
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    
    token = create_access_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}