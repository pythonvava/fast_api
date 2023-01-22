from fastapi import APIRouter


router = APIRouter()


@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_done():
    pass


@router.delete("/tasks/{task_id}/dond", response_model=None)
async def unmark_task_as_done():
    pass