import json
import os
from typing import List


# 加载特定用户的待办事项
def load_todos(person_id: str) -> List[str]:
    file_path = os.path.join("data", "todos", f"{person_id}_todo.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []


# 保存待办事项到特定用户的 JSON 文件中
def save_todos(person_id: str, content: List[str]) -> None:
    file_path = os.path.join("data", "todos", f"{person_id}_todo.json")
    with open(file_path, "w") as file:
        json.dump(content, file)


# 向待办事项列表中添加任务
def add_todo_task(person_id: str, task: str) -> None:
    todos = load_todos(person_id)
    todos.append(task)  # 直接在原始列表上添加任务
    save_todos(person_id, todos)


# 从待办事项列表中移除任务
def remove_todo_task(person_id: str, task: str) -> None:
    todos = load_todos(person_id)
    if task in todos:
        todos.remove(task)
        save_todos(person_id, todos)


# 查看特定用户的所有待办事项
def view_todos(person_id: str) -> List[str]:
    return load_todos(person_id)
