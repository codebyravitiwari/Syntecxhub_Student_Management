"""
Data Storage Handler
Handles JSON file operations for student data persistence.
"""
import os
import sys
import json
from typing import List, Optional

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.student import Student


class DataHandler:
    """Handles reading and writing student data to JSON file."""
    
    def __init__(self, file_path: str = "data/students.json"):
        """
        Initialize DataHandler with file path.
        
        Args:
            file_path: Path to the JSON data file
        """
        self.file_path = file_path
    
    def _ensure_directory(self) -> None:
        """Ensure the directory for the data file exists."""
        directory = os.path.dirname(self.file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
    
    def load(self) -> List[Student]:
        """
        Load students from JSON file.
        
        Returns:
            List of Student objects
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file is invalid JSON
        """
        if not os.path.exists(self.file_path):
            return []
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            students = []
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        students.append(Student.from_dict(item))
            
            return students
        
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Warning: Invalid JSON in {self.file_path}. Starting fresh.")
            return []
    
    def save(self, students: List[Student]) -> bool:
        """
        Save students to JSON file.
        
        Args:
            students: List of Student objects to save
            
        Returns:
            True if successful, False otherwise
        """
        try:
            self._ensure_directory()
            
            data = [student.to_dict() for student in students]
            
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            return True
            
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def file_exists(self) -> bool:
        """
        Check if data file exists.
        
        Returns:
            True if file exists, False otherwise
        """
        return os.path.exists(self.file_path)
