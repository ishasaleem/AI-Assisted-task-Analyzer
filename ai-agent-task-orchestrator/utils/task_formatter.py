def format_tasks(parsed: dict):
    """
    Wrap tasks into a small structured JSON-like object.
    parsed: dict with 'frontend' and 'backend' lists (strings)
    """
    frontend = [{"task": t, "status": "pending"} for t in parsed.get("frontend", [])]
    backend = [{"task": t, "status": "pending"} for t in parsed.get("backend", [])]
    return {"frontend": frontend, "backend": backend}
