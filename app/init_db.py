"""Initialise the Employee Directory SQLite Database"""

from app import init_db

def main() -> None:
    """Create the database schema"""
    
    init_db()
    print("Employee Directory database initialised successfully")

    
if __name__ == "__main__":
    main()