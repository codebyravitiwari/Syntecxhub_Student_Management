"""
Student Model
Represents a student entity with all required attributes and methods.
"""

class Student:
    """A class representing a student with unique ID, name, and grade."""
    
    def __init__(self, student_id: str, name: str, grade: str):
        """
        Initialize a Student instance.
        
        Args:
            student_id: Unique identifier for the student
            name: Name of the student
            grade: Grade of the student (A, B, C, D, F)
        """
        self.student_id = student_id
        self.name = name
        self.grade = grade
    
    def to_dict(self) -> dict:
        """
        Convert Student object to dictionary.
        
        Returns:
            Dictionary representation of the student
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Student':
        """
        Create Student object from dictionary.
        
        Args:
            data: Dictionary containing student data
            
        Returns:
            Student instance
        """
        return Student(
            student_id=data.get("student_id", ""),
            name=data.get("name", ""),
            grade=data.get("grade", "")
        )
    
    def __repr__(self) -> str:
        """String representation of Student object."""
        return f"Student(id={self.student_id}, name={self.name}, grade={self.grade})"
