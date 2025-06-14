from typing import List
from src.user_db import USER_DB, ROLE_ACCESS

def authenticate_user(username: str) -> bool:
    """Check if the user exists in the system."""
    return username in USER_DB

def get_user_role(username: str) -> str:
    """Fetch the user's role from the DB. Default is 'employee'."""
    return USER_DB.get(username, "employee")

def get_permitted_sources(role: str) -> List[str]:
    """
    Given a role (e.g. 'hr'), return the list of allowed document sources.
    These are used to filter document chunks during retrieval.
    """
    return ROLE_ACCESS.get(role, ["employee_handbook"])
