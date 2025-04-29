# Учебные Курсы и Профили Студентов

Этот проект содержит два класса: `Course` и `StudentProfile`, которые представляют учебные курсы и профили студентов соответственно.

## Описание

### Класс `Course`

Класс `Course` используется для представления учебного курса. Он имеет следующие атрибуты:
- `title` (str): Название курса.
- `duration` (int): Длительность курса в часах.

#### Методы

- `get_absolute_url() -> str`: Возвращает абсолютный URL страницы курса на сайте.

#### Пример использования

```python
course_front = Course('Frontend', 38)
course_py = Course('Python', 50)

print(course_front.get_absolute_url())  # Вывод: 'https://ivashev-edu.com/courses/Frontend'
print(course_py.get_absolute_url())    # Вывод: 'https://ivashev-edu.com/courses/Python'
