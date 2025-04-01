class Department():
    def __init__(self, deptno, name, loc):
        self.dept_number = deptno
        self.name = name
        self.location = loc


    def to_dict(self) -> dict:
        """Convert Department object to a dictionary.
        
        Returns:
            Dictionary containing all department attributes.
        """
        return {
            'dept_number': self.dept_number,
            'name': self.name,
            'location': self.location
        }
