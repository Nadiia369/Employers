import csv
from faker import Faker
import random

# Словники для по батькові
male_patronymics = ['Олександрович', 'Миколайович', 'Петрович', 'Сергійович', 'Андрійович', 'Іванович', 'Васильович',
                    'Григорович', 'Дмитрович', 'Юрійович', 'Федорович', 'Анатолійович', 'Антонович', 'Остапович', 'Семенович', 'Вікторович', 'Дамирович', 'Опанасович', 'Вячеславович', 'Артемович']
female_patronymics = ['Олександрівна', 'Миколаївна', 'Петрівна', 'Сергіївна', 'Андріївна', 'Іванівна', 'Василівна',
                      'Григорівна', 'Дмитрівна', 'Юріївна', 'Федорівна', 'Анатоліївна', 'Антонівна', 'Остапівна', 'Семенівна', 'Вікторівна', 'Дамирівна', 'Опанасівна', 'Вячеславівна', 'Артемівна']

# Ініціалізація Faker для української локалізації
fake = Faker(locale='uk_UA')


# Функція для створення одного запису співробітника
def create_employee(gender):
    if gender == 'male':
        first_name = fake.first_name_male()
        patronymic = random.choice(male_patronymics)
    else:
        first_name = fake.first_name_female()
        patronymic = random.choice(female_patronymics)

    last_name = fake.last_name()
    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
    job = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [last_name, first_name, patronymic, gender, birth_date, job, city, address, phone, email]


# Створення CSV файлу
def generate_csv(filename, num_records):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання',
                         'Адреса проживання', 'Телефон', 'Email'])

        # Генерація 40% жінок і 60% чоловіків
        male_count = int(num_records * 0.6)
        female_count = num_records - male_count

        # Додавання записів для чоловіків
        for _ in range(male_count):
            writer.writerow(create_employee('male'))

        # Додавання записів для жінок
        for _ in range(female_count):
            writer.writerow(create_employee('female'))

    print(f"Створено файл {filename} з {num_records} записами.")


# Генерація 2000 записів
generate_csv('employees.csv', 2000)
