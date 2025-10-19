def parse_brief(brief: str):
    """
    Very small keyword-based parser.
    Returns dict with 'frontend' and 'backend' lists of tasks (strings).
    """
    brief_lower = brief.lower()
    frontend_tasks = []
    backend_tasks = []

    # Authentication / login
    if any(k in brief_lower for k in ["auth", "authentication", "login", "signup", "sign up", "register"]):
        frontend_tasks.append("Create login/signup pages & forms")
        backend_tasks.append("Implement auth endpoints (signup/login) and JWT/session handling")

    # Tasks / CRUD
    if any(k in brief_lower for k in ["task", "tasks", "todo", "to-do", "task management"]):
        frontend_tasks.append("Build dashboard, task list UI, create/edit/delete task UI")
        backend_tasks.append("Implement task CRUD endpoints with validation")

    # Sharing / social
    if any(k in brief_lower for k in ["share", "sharing", "collaborate", "collaboration"]):
        frontend_tasks.append("Add sharing UI & invite flows")
        backend_tasks.append("Implement sharing endpoints & permission checks")

    # Comments / comments
    if "comment" in brief_lower:
        frontend_tasks.append("Create comment component & UI")
        backend_tasks.append("Create comment endpoints and link to tasks/users")

    # File upload / attachments
    if any(k in brief_lower for k in ["upload", "attachment", "file"]):
        frontend_tasks.append("Add file upload UI")
        backend_tasks.append("Add file upload endpoint and storage wiring")

    # If nothing matched, add a general split
    if not frontend_tasks and not backend_tasks:
        frontend_tasks.append("Create basic UI (Home, About, placeholder pages)")
        backend_tasks.append("Create basic API skeleton (health check)")

    return {"frontend": frontend_tasks, "backend": backend_tasks}
