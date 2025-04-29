class Course:
    """
    Класс для представления учебного курса.

    Атрибуты:
        title (str): Название курса.
        duration (int): Длительность курса в часах.
    """

    def __init__(self, title: str, duration: int) -> None:
        """
        Инициализирует новый объект Course.

        Args:
            title (str): Название курса.
            duration (int): Длительность курса в часах.
        """
        self.title: str = title
        self.duration: int = duration

    def get_absolute_url(self) -> str:
        """
        Возвращает абсолютный URL курса.

        Returns:
            str: URL страницы курса на сайте.

        Пример:
            >>> course = Course('Data Science', 40)
            >>> course.get_absolute_url()
            'https://ivashev-edu.com/courses/Data-Science'
        """
        clean_title: str = self.title.strip().replace(" ", "-")
        return f"https://ivashev-edu.com/courses/{clean_title}"


class StudentProfile:
    """
    Класс для представления профиля студента.

    Атрибуты:
        full_name (str): Полное имя студента.
        email (str): Электронная почта студента.
    """

    def __init__(self, full_name: str, email: str) -> None:
        """
        Инициализирует новый объект StudentProfile.

        Args:
            full_name (str): Полное имя студента.
            email (str): Электронная почта студента.
        """
        self.full_name: str = full_name
        self.email: str = email

    def get_absolute_url(self) -> str:
        """
        Возвращает абсолютный URL профиля студента.

        Returns:
            str: URL страницы профиля на сайте.

        Пример:
            >>> profile = StudentProfile('Jane Doe', 'jane@example.com')
            >>> profile.get_absolute_url()
            'https://ivashev-edu.com/profiles/Jane-Doe'
        """
        clean_name: str = self.full_name.strip().replace(" ", "-")
        return f"https://ivashev-edu.com/profiles/{clean_name}"


# Примеры использования
course_front: Course = Course('Frontend', 38)
course_py: Course = Course('Python', 50)

st1: StudentProfile = StudentProfile('Andrew14', "andrew1413@mail.ru")
st2: StudentProfile = StudentProfile("Olga Petrova", "olgaPetrova@yandex.ru")

print(course_front.get_absolute_url())
print(course_py.get_absolute_url())
print(st1.get_absolute_url())
print(st2.get_absolute_url())

# Проверка доктестов
if __name__ == "__main__":
    import doctest
    doctest.testmod()
