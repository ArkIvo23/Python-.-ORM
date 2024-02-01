Домашнее задание к лекции «Python и БД. ORM»
Задание 1
Составить модели классов SQLAlchemy по схеме (в приложении, см. "book_publishers_scheme").



Легенда: система хранит информацию об издателях (авторах), их книгах и фактах продажи. Книги могут продаваться в разных магазинах, поэтому требуется учитывать не только что за книга была продана, но и в каком магазине это было сделано, а также когда.

Интуитивно необходимо выбрать подходящие типы и связи полей.

Задание 2
Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

Напишите Python-скрипт, который:

подключается к БД любого типа на ваш выбор, например, к PostgreSQL;
импортирует необходимые модели данных;
принимает имя или идентификатор издателя (publisher), например, через input(). Выводит построчно факты покупки книг этого издателя:
название книги | название магазина, в котором была куплена эта книга | стоимость покупки | дата покупки
Пример (было введено имя автора — Пушкин):

Капитанская дочка | Буквоед     | 600 | 09-11-2022
Руслан и Людмила  | Буквоед     | 500 | 08-11-2022
Капитанская дочка | Лабиринт    | 580 | 05-11-2022
Евгений Онегин    | Книжный дом | 490 | 02-11-2022
Капитанская дочка | Буквоед     | 600 | 26-10-2022
Задание 3 (необязательное)
Заполните БД тестовыми данными.

Тестовые данные берутся из папки fixtures. Пример содержания в JSON-файле.

Возможная реализация: прочитать JSON-файл, создать соотведствующие экземляры моделей и сохранить в БД.

Пример реализации, но сначала попытайтесь самостоятельно ;)
Общие советы
Параметры подключения к БД следует выносить в отдельные переменные: логин, пароль, название БД и пр.
Загружать значения лучше из окружения ОС, например, через os.getenv().
Заполнять данными можно вручную или выполнить необязательное задание 3.