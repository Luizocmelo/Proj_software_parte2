class TimeRegister:
    def __init__(self, emp_id, date, hours):
        self.emp_id = emp_id
        self.date = date
        self.hours = hours
    def get_empTimeRegisters(self):
        return self.employeesTimeRegisters
    def set_to_clear_registers(self):
        self.employeesTimeRegisters = []
    def get_emp_id(self):
        return self.emp_id
    def set_emp_id(self, new_id):
        self.emp_id = new_id
    def get_date(self):
        return self.__date
    def set_date(self, new_date):
        self.__date = new_date    
    def get_hours(self):
        return self.__hours
    def set_hours(self, new_hours):
        self.__hours = new_hours   
    def __repr__(self):
        return "\nid: %i, data: %s -- %s horas\n\n" %(self.emp_id, self.date, self.hours)