FROM sinfallas/base-python-uv:3.13
LABEL maintainer="Jesus Palencia sinfallas@gmail.com"

WORKDIR /app
RUN uv pip install --system fastapi uvicorn redis
COPY main.py .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
