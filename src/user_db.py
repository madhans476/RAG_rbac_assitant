# Simulated user-role mapping
USER_DB = {
    "alice": "finance",
    "bob": "marketing",
    "charlie": "hr",
    "diana": "engineering",
    "emma": "employee",
    "ceo_tony": "c_level"
}

# Role-based document access permissions
ROLE_ACCESS = {
    "finance": ["finance"],
    "marketing": ["marketing"],
    "hr": ["hr", "employee_handbook"],
    "engineering": ["engineering"],
    "employee": ["employee_handbook"],
    "c_level": ["finance", "marketing", "hr", "engineering", "employee_handbook"]
}
