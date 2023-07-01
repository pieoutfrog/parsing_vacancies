class Vacancies:
    def __init__(self, url: str, salary: float, description: str, title: str, area: str, experience: str):
        self.url = url
        if salary is None or salary == '0' or salary == 0:
            self.salary = 0.0
        else:
            self.salary = salary
        self.description = description
        self.title = title
        self.area = area
        self.experience = experience
        self.validate()

    def validate(self):
        if not isinstance(self.title, str):
            raise ValueError("Название должно быть строкой")
        if not isinstance(self.url, str):
            raise ValueError("Ссылка должна быть строкой")
        if not isinstance(self.salary, (int, float)):
            raise ValueError("Зарплата должна быть цифровым значением")
        if not isinstance(self.description, str):
            raise ValueError("Описание должно быть строкой")
        if not isinstance(self.area, str):
            raise ValueError("Регион должен быть строкой")

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"""Название вакансии: {self.title}
Зарплата: {self.salary}
Требуемый опыт: {self.experience}
Описание: {self.description}
Ссылка на вакансию: {self.url}
Регион: {self.area}"""

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary
