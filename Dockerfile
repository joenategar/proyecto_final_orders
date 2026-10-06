FROM python:3.12-slim AS builder
WORKDIR /app

RUN pip install pipx && pipx install poetry && pipx inject poetry poetry-plugin-export
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml README.md ./
COPY src/ ./src/

RUN poetry build -f wheel
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12-slim AS runner

RUN groupadd -r appgroup && useradd -r -g appgroup appuser
WORKDIR /app

COPY --from=builder /app/requirements.txt .
COPY --from=builder /app/dist/*.whl ./

RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir *.whl

RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8000
CMD ["uvicorn", "proyecto_final_orders.main:app", "--host", "0.0.0.0", "--port", "8000"]