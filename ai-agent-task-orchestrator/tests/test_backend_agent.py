from agents.backend_agent import BackendAgent
from pathlib import Path

def test_backend_generation(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    ba = BackendAgent()
    ba.handle_tasks([{"task": "Create task endpoints", "status": "pending"}])

    base = Path("outputs/backend_code")
    assert (base / "app.py").exists()
    assert (base / "routes" / "auth_routes.py").exists()
    assert (base / "routes" / "task_routes.py").exists()
