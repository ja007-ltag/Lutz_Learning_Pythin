"""
Полиморфизм и классы
"""


class Employee:
    """Универсальный супер-класс"""
    def compute_salary(self):
        """Расчёт зарплаты"""
        ...

    def give_raise(self):
        """Повышение зарплаты"""
        ...

    def promote(self):
        """Продвижение"""
        ...

    def retire(self):
        """Увольнение"""
        ...


class Engineer(Employee):
    """Специализированный подкласс"""
    def compute_salary(self):
        """Специальный подсчёт зарплаты"""
        ...


bob = Employee()
sue = Employee()
tom = Engineer()

company = [bob, sue, tom]  # Составной объект
for emp in company:
    # Выполнить версию для данного объекта: стандартную или специальную
    print(emp.compute_salary())
