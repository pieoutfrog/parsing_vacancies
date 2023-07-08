class Vacancies:
    """Класс для работы с вакансиями"""

    def __init__(self, url: str, salary: float, description: str, title: str, area: str, experience: str):
        """
        :param url: ссылка на вакансию
        :param salary: зарплата
        :param description: описание
        :param title: название вакансии
        :param area: область, где размещена вакансия
        :param experience: требуемый опыт
                """
        if salary is None or salary == '0' or salary == 0:
            self.salary = 0.0
        else:
            self.salary = salary
        self.description = description
        self.title = title
        self.area = area
        self.experience = experience
        self.url = url
        self.validate()

    def validate(self):
        """
        Класс, валидирующий данные
        """
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
        """
        Метод для приведения атрибутов к словарю
        :return: словарь с вакансиями
        """
        return self.__dict__

    def __str__(self):
        """
        :return: f-строка, выводящая данные в удобном формате
        """
        return f"""Название вакансии: {self.title}
Зарплата: {self.salary}
Требуемый опыт: {self.experience}
Описание: {self.description}
Ссылка на вакансию: {self.url}
Регион: {self.area}"""

    def __eq__(self, other):
        return self.salary == other.salary

    """
    Методы сравнения зарплат
    """

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
