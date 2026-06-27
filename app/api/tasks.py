@router.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):

    success = manager.complete_task(task_id)

    if not success:
        return {"error": "Task not found"}

    return {"message": "Task completed"}

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    success = manager.delete_task(task_id)

    if not success:
        return {"error": "Task not found"}

    return {"message": "Task deleted"}