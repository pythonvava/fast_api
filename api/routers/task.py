from typing import List
from fastapi import APIRouter
import api.schemes.task as task_schema

router = APIRouter()

@router.get("/tasts", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のTODOタスク")]


@router.post("/tasks")
async def create_tasks():
    pass


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    psss