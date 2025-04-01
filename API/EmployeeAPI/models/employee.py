class Employee():
    def __init__(self, emp_number, name, job, mgr, hiredate, sal, comm, dept_number):
        self.emp_number = emp_number
        self.name = name
        self.job = job
        self.mgr = mgr  # Manager's employee number
        self.hiredate = hiredate
        self.salary = sal
        self.commission = comm
        self.dept_number = dept_number  # Department number


    def to_dict(self) -> dict:
        """Convert Employee object to a dictionary.
        
        Returns:
            Dictionary containing all employee attributes.
        """
        return {
            'emp_number': self.emp_number,
            'name': self.name,
            'job': self.job,
            'mgr': self.mgr,
            'hiredate': self.hiredate,
            'salary': self.salary,
            'commission': self.commission,
            'dept_number': self.dept_number
        }
    
