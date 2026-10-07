ROLES = {
    "student": ["tasks", "board"],
    "teacher": ["tasks", "board", "review"],
    "admin": ["tasks", "board", "review", "users", "permissions"],
}

def get_sections(role):
    return ROLES.get(role, [])