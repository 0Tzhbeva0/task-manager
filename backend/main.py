from __future__ import annotations

import os
from pathlib import Path
from typing import List

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from models import Task, TaskCreate, TaskUpdate
from storage import JsonTaskStorage


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = os.environ.get("TASKS_FILE", str(BASE_DIR / "tasks.json"))

storage = JsonTaskStorage(DATA_FILE)

app = FastAPI(title="Task Manager API", version="1.0.0")

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/api/tasks", response_model=List[Task])
def list_tasks() -> List[Task]:
    return storage.list()


@app.get("/api/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    return storage.get(task_id)


@app.post("/api/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate) -> Task:
    return storage.create(payload)


@app.put("/api/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate) -> Task:
    return storage.update(task_id, payload)


@app.delete("/api/tasks/{task_id}", status_code=204)
def delete_task(task_id: int) -> Response:
    storage.delete(task_id)
    return Response(status_code=204)
