"""
CLI Interface
Main entry point for the Student Management System.
"""
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.manager import StudentManager


class CLI:
    """Command-line interface for Student Management System."""
    
    def __init__(self):
        """Initialize CLI with StudentManager."""
        self.manager = StudentManager()
    
    def clear_screen(self) -> None:
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self) -> None:
        """Print application header."""
        print("\n" + "=" * 50)
        print("       STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
    
    def print_menu(self) -> None:
        """Print main menu options."""
        print("\n--- MAIN MENU ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
    
    def print_student_table(self, students: list) -> None:
        """
        Print students in a formatted table.
        
        Args:
            students: List of Student objects
        """
        if not students:
            print("\nNo students found.")
            return
        
        print("\n" + "-" * 50)
        print(f"{'ID':<15} {'NAME':<20} {'GRADE':<5}")
        print("-" * 50)
        
        for student in students:
            print(f"{student.student_id:<15} {student.name:<20} {student.grade:<5}")
        
        print("-" * 50)
        print(f"Total: {len(students)} student(s)")
    
    def get_input(self, prompt: str) -> str:
        """
        Get input from user with prompt.
        
        Args:
            prompt: Input prompt text
            
        Returns:
            User input string
        """
        return input(prompt).strip()
    
    def show_success(self, message: str) -> None:
        """Print success message."""
        print(f"\n✓ SUCCESS: {message}")
    
    def show_error(self, message: str) -> None:
        """Print error message."""
        print(f"\n✗ ERROR: {message}")
    
    def show_info(self, message: str) -> None:
        """Print info message."""
        print(f"\nℹ INFO: {message}")
    
    def pause(self) -> None:
        """Pause for user input."""
        input("\nPress Enter to continue...")
    
    def add_student(self) -> None:
        """Handle add student operation."""
        print("\n--- ADD STUDENT ---")
        
        student_id = self.get_input("Enter Student ID: ")
        name = self.get_input("Enter Name: ")
        grade = self.get_input("Enter Grade (A/B/C/D/F): ")
        
        success, message = self.manager.add_student(student_id, name, grade)
        
        if success:
            self.show_success(message)
        else:
            self.show_error(message)
    
    def view_students(self) -> None:
        """Handle view all students operation."""
        print("\n--- ALL STUDENTS ---")
        students = self.manager.list_students()
        self.print_student_table(students)
    
    def update_student(self) -> None:
        """Handle update student operation."""
        print("\n--- UPDATE STUDENT ---")
        
        student_id = self.get_input("Enter Student ID to update: ")
        
        # Check if student exists
        student = None
        for s in self.manager.list_students():
            if s.student_id == student_id:
                student = s
                break
        
        if not student:
            self.show_error(f"Student with ID '{student_id}' not found.")
            return
        
        print(f"Current info: Name='{student.name}', Grade='{student.grade}'")
        print("(Press Enter to keep current value)")
        
        name = self.get_input("Enter new name: ")
        grade = self.get_input("Enter new grade (A/B/C/D/F): ")
        
        # Use None for empty inputs to preserve existing values
        name = name if name else None
        grade = grade if grade else None
        
        success, message = self.manager.update_student(student_id, name, grade)
        
        if success:
            self.show_success(message)
        else:
            self.show_error(message)
    
    def delete_student(self) -> None:
        """Handle delete student operation."""
        print("\n--- DELETE STUDENT ---")
        
        student_id = self.get_input("Enter Student ID to delete: ")
        
        # Confirm deletion
        confirm = self.get_input(f"Are you sure you want to delete student '{student_id}'? (yes/no): ")
        
        if confirm.lower() != 'yes':
            self.show_info("Deletion cancelled.")
            return
        
        success, message = self.manager.delete_student(student_id)
        
        if success:
            self.show_success(message)
        else:
            self.show_error(message)
    
    def search_student(self) -> None:
        """Handle search student operation."""
        print("\n--- SEARCH STUDENT ---")
        
        query = self.get_input("Enter ID or Name to search: ")
        
        if not query:
            self.show_error("Search query cannot be empty.")
            return
        
        results = self.manager.search_student(query)
        
        if results:
            print(f"\nFound {len(results)} result(s):")
            self.print_student_table(results)
        else:
            self.show_info("No students found matching the query.")
    
    def run(self) -> None:
        """Run the CLI application."""
        while True:
            self.clear_screen()
            self.print_header()
            self.print_menu()
            
            choice = self.get_input("\nEnter your choice (1-6): ")
            
            try:
                if choice == '1':
                    self.add_student()
                    self.pause()
                elif choice == '2':
                    self.view_students()
                    self.pause()
                elif choice == '3':
                    self.update_student()
                    self.pause()
                elif choice == '4':
                    self.delete_student()
                    self.pause()
                elif choice == '5':
                    self.search_student()
                    self.pause()
                elif choice == '6':
                    self.show_info("Thank you for using Student Management System. Goodbye!")
                    break
                else:
                    self.show_error("Invalid choice. Please enter a number between 1 and 6.")
                    self.pause()
            except KeyboardInterrupt:
                self.show_info("\nOperation cancelled.")
                self.pause()
            except Exception as e:
                self.show_error(f"An unexpected error occurred: {e}")
                self.pause()


def main():
    """Main entry point."""
    try:
        cli = CLI()
        cli.run()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
