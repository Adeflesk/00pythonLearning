class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "."+last + '@company.com'

        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first , last, pay = emp_str.split('-')
        return cls(first, last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()== 5 or day.weekday()== 6:
            return False
        return True

         
emp_1 = Employee("Adrian","Corsini", 50000)
emp_2 = Employee("Steven","Corsini", 60000)
emp_3 = Employee.from_string('Sarah-Corsini-45000')


Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.num_of_emps)
print(emp_3.fullname())
import datetime
my_date = datetime.date(2018, 8, 10)
print(Employee.is_workday(my_date))
