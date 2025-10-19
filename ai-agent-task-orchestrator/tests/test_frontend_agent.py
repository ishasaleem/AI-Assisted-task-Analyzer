from agents.frontend_agent import FrontendAgent
from pathlib import Path
import shutil

def test_frontend_generation(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    fa = FrontendAgent()
    # sample tasks (format used by coordinator)
    fa.handle_tasks([{"task": "Create login page", "status": "pending"}])

    base = Path("outputs/frontend_code")
    assert (base / "App.jsx").exists()
    assert (base / "pages" / "LoginPage.jsx").exists()
    assert (base / "pages" / "Dashboard.jsx").exists()
