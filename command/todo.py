import json
import os
from typing import List


# 加载特定用户的待办事项
def load_todos(person_id: str) -> List[str]:
    file_path = os.path.join("data", "todos", f"p{person_id}_todo.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []


# 保存待办事项到特定用户的 JSON 文件中
def save_todos(person_id: str, content: List[str]) -> None:
    file_path = os.path.join("data", "todos", f"p{person_id}_todo.json")
    with open(file_path, "w") as file:
        json.dump(content, file)


# 向待办事项列表中添加任务，并返回添加是否成功的状态
def add_todo_task(person_id: str, task: str) -> bool:
    todos = load_todos(person_id)
    todos.append(task)  # 直接在原始列表上添加任务
    try:
        save_todos(person_id, todos)
        return True  # 添加成功，返回 True
    except Exception as e:
        print(f"Error adding task: {e}")
        return False  # 添加失败，返回 False


# 从待办事项列表中移除任务
def remove_todo_task(person_id: str, task: str) -> None:
    todos = load_todos(person_id)
    if task in todos:
        todos.remove(task)
        save_todos(person_id, todos)


# 查看特定用户的所有待办事项
def view_todos(person_id: str) -> str:
    todos = load_todos(person_id)
    if todos:
        formatted_todos = "\n".join(f"{i+1}. {task}" for i, task in enumerate(todos))
        return formatted_todos
    else:
        return "没有待办事项。"
