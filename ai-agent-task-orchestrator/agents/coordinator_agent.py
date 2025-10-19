from agents.frontend_agent import FrontendAgent
from agents.backend_agent import BackendAgent

class CoordinatorAgent:
    def __init__(self):
        self.frontend_agent = FrontendAgent()
        self.backend_agent = BackendAgent()

    def process_brief(self, project_brief):
        print(f"Received project brief: {project_brief}")

        frontend_keywords = ["frontend", "ui", "react"]
        backend_keywords = ["backend", "api", "database"]

        result = {"frontend": [], "backend": []}

        if any(k in project_brief.lower() for k in frontend_keywords):
            result["frontend"] = self.frontend_agent.generate_tasks(project_brief)
        if any(k in project_brief.lower() for k in backend_keywords):
            result["backend"] = self.backend_agent.generate_tasks(project_brief)

        # Fallback: assign to backend if nothing matches
        if not result["frontend"] and not result["backend"]:
            result["backend"] = self.backend_agent.generate_tasks(project_brief)

        return result
