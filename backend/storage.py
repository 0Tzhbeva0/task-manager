from __future__ import annotations

import json
import os
import threading
from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import HTTPException

from models import Task, TaskCreate, TaskUpdate


class JsonTaskStorage:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._lock = threading.Lock()

        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)
        if not os.path.exists(self._file_path):
            self._write_raw([])

    def _read_raw(self) -> List[Dict[str, Any]]:
        with open(self._file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("tasks.json must contain a JSON array")
        return data

    def _write_raw(self, tasks: List[Dict[str, Any]]) -> None:
        tmp_path = f"{self._file_path}.tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, self._file_path)

    def list(self) -> List[Task]:
        with self._lock:
            raw = self._read_raw()
            return [Task.model_validate(item) for item in raw]

    def get(self, task_id: int) -> Task:
        with self._lock:
            raw = self._read_raw()
            for item in raw:
                if int(item.get("id")) == task_id:
                    return Task.model_validate(item)
        raise HTTPException(status_code=404, detail="Task not found")

    def create(self, payload: TaskCreate) -> Task:
        with self._lock:
            raw = self._read_raw()
            next_id = (max((int(t.get("id", 0)) for t in raw), default=0) + 1) if raw else 1
            now = datetime.utcnow()
            task = Task(
                id=next_id,
                created_at=now,
                updated_at=now,
                **payload.model_dump(),
            )
            raw.append(task.model_dump(mode="json"))
            self._write_raw(raw)
            return task

    def update(self, task_id: int, payload: TaskUpdate) -> Task:
        with self._lock:
            raw = self._read_raw()
            for idx, item in enumerate(raw):
                if int(item.get("id")) == task_id:
                    existing = Task.model_validate(item)
                    patch = payload.model_dump(exclude_unset=True)
                    updated = existing.model_copy(update={**patch, "updated_at": datetime.utcnow()})
                    raw[idx] = updated.model_dump(mode="json")
                    self._write_raw(raw)
                    return updated
        raise HTTPException(status_code=404, detail="Task not found")

    def delete(self, task_id: int) -> None:
        with self._lock:
            raw = self._read_raw()
            new_raw = [t for t in raw if int(t.get("id")) != task_id]
            if len(new_raw) == len(raw):
                raise HTTPException(status_code=404, detail="Task not found")
            self._write_raw(new_raw)
