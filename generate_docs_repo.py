import os

BASE_DIR = "project-docs-repo-template"

STRUCTURE = {
    "0-admin": [
        "contacts.md",
        "stakeholder-map.md",
        "glossary.md",
    ],
    "1-product": [
        "vision.md",
        "roadmap.md",
        "feature-requests.md",
        "user-personas.md",
        "user-journeys.md",
        "requirements/functional.md",
        "requirements/non-functional.md",
    ],
    "2-program-management": [
        "release-plan.md",
        "risk-register.md",
        "resource-planning.md",
        "gantt-charts/q4-2025.png",
        "status-reports/weekly-status-2025-09-19.md",
    ],
    "3-architecture": [
        "system-design.md",
        "data-flow-diagrams/README.md",
        "api-specs/README.md",
        "tech-stack-decision.md",
        "threat-model.md",
        "spike-docs/spike-caching-vs-queue.md",
    ],
    "4-development": [
        "setup-instructions.md",
        "code-style-guide.md",
        "branching-strategy.md",
        "tech-debt.md",
        "modules/auth-module.md",
    ],
    "5-qa": [
        "test-plan.md",
        "test-cases/README.md",
        "bug-reports/README.md",
        "test-summary-reports/README.md",
        "automation-framework-overview.md",
    ],
    "6-devops": [
        "ci-cd-pipelines.md",
        "deployment-process.md",
        "infrastructure-diagrams/README.md",
        "monitoring-alerts.md",
        "rollback-procedures.md",
    ]
}

def create_structure(base_dir, structure):
    for folder, files in structure.items():
        for file in files:
            path = os.path.join(base_dir, folder, file)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if not file.endswith('.png'):
                with open(path, 'w') as f:
                    f.write(f"# {os.path.basename(file).replace('-', ' ').title()}\n\n*To be filled by relevant stakeholders.*")

if __name__ == "__main__":
    os.makedirs(BASE_DIR, exist_ok=True)
    create_structure(BASE_DIR, STRUCTURE)
    with open(os.path.join(BASE_DIR, "README.md"), "w") as readme:
        readme.write("# Project Documentation Template\n\nOrganized by stakeholder responsibilities.")
    print(f"✅ Scaffold created in: {BASE_DIR}/")
