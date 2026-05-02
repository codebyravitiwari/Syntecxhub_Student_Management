"""
Student Manager Service
Business logic for managing student operations.
"""
import os
import sys
from typing import List, Optional

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.student import Student
from storage.data_handler import DataHandler
from utils.validators import (
    validate_student_data,
    validate_name,
    validate_grade,
    get_valid_grades
)


class StudentManager:
    """Manages all student-related operations."""
    
    def __init__(self, data_file: str = None):
        """
        Initialize StudentManager.
        
        Args:
            data_file: Path to the JSON data file (optional)
        """
        # Use default path if not provided
        if data_file is None:
            # Get the directory of this file and construct default path
            current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            data_file = os.path.join(current_dir, "data", "students.json")
        
        self.data_handler = DataHandler(data_file)
        self.students: List[Student] = []
        self._load_data()
    
    def _load_data(self) -> None:
        """Load existing students from file."""
        try:
            self.students = self.data_handler.load()
            print(f"Loaded {len(self.students)} student(s) from storage.")
        except Exception as e:
            print(f"Error loading data: {e}")
            self.students = []
    
    def _save_data(self) -> bool:
        """
        Save current students to file.
        
        Returns:
            True if successful, False otherwise
        """
        return self.data_handler.save(self.students)
    
    def _is_duplicate_id(self, student_id: str) -> bool:
        """
        Check if student ID already exists.
        
        Args:
            student_id: The student ID to check
            
        Returns:
            True if duplicate exists, False otherwise
        """
        return any(s.student_id == student_id for s in self.students)
    
    def _find_student(self, student_id: str) -> Optional[Student]:
        """
        Find student by ID.
        
        Args:
            student_id: The student ID to search for
            
        Returns:
            Student object if found, None otherwise
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def add_student(self, student_id: str, name: str, grade: str) -> tuple:
        """
        Add a new student to the system.
        
        Args:
            student_id: Unique student ID
            name: Student name
            grade: Student grade (A, B, C, D, F)
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        # Validate input
        is_valid, error_message = validate_student_data(student_id, name, grade)
        if not is_valid:
            return (False, error_message)
        
        # Normalize inputs
        student_id = student_id.strip()
        name = name.strip()
        grade = grade.upper().strip()
        
        # Check for duplicate ID
        if self._is_duplicate_id(student_id):
            return (False, f"Student ID '{student_id}' already exists.")
        
        # Create and add student
        student = Student(student_id, name, grade)
        self.students.append(student)
        
        # Save to file
        if self._save_data():
            return (True, f"Student '{name}' (ID: {student_id}) added successfully!")
        else:
            self.students.remove(student)
            return (False, "Failed to save student data.")
    
    def list_students(self) -> List[Student]:
        """
        Get all students.
        
        Returns:
            List of all Student objects
        """
        return self.students
    
    def update_student(self, student_id: str, name: str = None, grade: str = None) -> tuple:
        """
        Update an existing student's information.
        
        Args:
            student_id: Student ID to update
            name: New name (optional)
            grade: New grade (optional)
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        # Find student
        student = self._find_student(student_id)
        if not student:
            return (False, f"Student with ID '{student_id}' not found.")
        
        # Validate name if provided
        if name is not None:
            name = name.strip()
            if not validate_name(name):
                return (False, "Name cannot be empty.")
        
        # Validate grade if provided
        if grade is not None:
            grade = grade.upper().strip()
            if not validate_grade(grade):
                valid_grades = ", ".join(get_valid_grades())
                return (False, f"Invalid grade. Must be one of: {valid_grades}")
        
        # Update fields
        updates = []
        if name and name != student.name:
            student.name = name
            updates.append(f"name to '{name}'")
        if grade and grade != student.grade:
            student.grade = grade
            updates.append(f"grade to '{grade}'")
        
        if not updates:
            return (True, "No changes to update.")
        
        # Save to file
        if self._save_data():
            return (True, f"Student '{student.student_id}' updated: {', '.join(updates)}")
        else:
            return (False, "Failed to save student data.")
    
    def delete_student(self, student_id: str) -> tuple:
        """
        Delete a student from the system.
        
        Args:
            student_id: Student ID to delete
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        # Find student
        student = self._find_student(student_id)
        if not student:
            return (False, f"Student with ID '{student_id}' not found.")
        
        # Remove student
        self.students.remove(student)
        
        # Save to file
        if self._save_data():
            return (True, f"Student '{student.name}' (ID: {student_id}) deleted successfully!")
        else:
            self.students.append(student)
            return (False, "Failed to save student data.")
    
    def search_student(self, query: str) -> List[Student]:
        """
        Search students by ID or name.
        
        Args:
            query: Search query (matches ID or name)
            
        Returns:
            List of matching Student objects
        """
        query = query.strip().lower()
        results = []
        
        for student in self.students:
            if query in student.student_id.lower() or query in student.name.lower():
                results.append(student)
        
        return results
    
    def get_student_count(self) -> int:
        """
        Get total number of students.
        
        Returns:
            Count of students
        """
        return len(self.students)
