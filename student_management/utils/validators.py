"""
Input Validation Utilities
Validates student data inputs according to business rules.
"""

# Valid grades
VALID_GRADES = ["A", "B", "C", "D", "F"]


def validate_student_id(student_id: str) -> bool:
    """
    Validate student ID.
    
    Args:
        student_id: The student ID to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not student_id or not student_id.strip():
        return False
    return True


def validate_name(name: str) -> bool:
    """
    Validate student name (cannot be empty).
    
    Args:
        name: The name to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not name or not name.strip():
        return False
    return True


def validate_grade(grade: str) -> bool:
    """
    Validate student grade (must be A, B, C, D, or F).
    
    Args:
        grade: The grade to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not grade:
        return False
    return grade.upper() in VALID_GRADES


def validate_student_data(student_id: str, name: str, grade: str) -> tuple:
    """
    Validate all student data together.
    
    Args:
        student_id: The student ID
        name: The student name
        grade: The student grade
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not validate_student_id(student_id):
        return (False, "Student ID cannot be empty.")
    
    if not validate_name(name):
        return (False, "Name cannot be empty.")
    
    if not validate_grade(grade):
        return (False, f"Grade must be one of: {', '.join(VALID_GRADES)}")
    
    return (True, "")


def get_valid_grades() -> list:
    """
    Get list of valid grades.
    
    Returns:
        List of valid grade strings
    """
    return VALID_GRADES.copy()
