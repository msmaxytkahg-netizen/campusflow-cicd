from app import get_sections

def test_student_has_no_admin_sections():
    sections = get_sections("student")
    assert "users" not in sections
    assert "permissions" not in sections

def test_admin_sees_permissions():
    assert "permissions" in get_sections("admin")

def test_unknown_role_gets_nothing():
    assert get_sections("hacker") == []