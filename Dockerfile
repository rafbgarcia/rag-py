FROM python:3.9-slim

WORKDIR /app

# Install uv
RUN python3 -m pip install uv

# Copy your project files
COPY . .

# Use uv sync to install dependencies
RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
