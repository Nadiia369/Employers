import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Функція для розрахунку віку
def calculate_age(birth_date):
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Функція для аналізу даних та побудови діаграм
def analyze_data(csv_filename):
    try:
        male_count = 0
        female_count = 0
        age_categories = {'younger_18': 0, '18-45': 0, '45-70': 0, 'older_70': 0}
        gender_by_age = {'younger_18': {'male': 0, 'female': 0}, '18-45': {'male': 0, 'female': 0}, '45-70': {'male': 0, 'female': 0}, 'older_70': {'male': 0, 'female': 0}}

        with open(csv_filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаємо заголовки

            for row in reader:
                gender = row[3]
                birth_date = datetime.strptime(row[4], "%Y-%m-%d")
                age = calculate_age(birth_date)

                if gender == 'male':
                    male_count += 1
                else:
                    female_count += 1

                if age < 18:
                    age_categories['younger_18'] += 1
                    gender_by_age['younger_18'][gender] += 1
                elif 18 <= age < 45:
                    age_categories['18-45'] += 1
                    gender_by_age['18-45'][gender] += 1
                elif 45 <= age < 70:
                    age_categories['45-70'] += 1
                    gender_by_age['45-70'][gender] += 1
                else:
                    age_categories['older_70'] += 1
                    gender_by_age['older_70'][gender] += 1

        # Виведення кількості чоловіків та жінок
        print(f"Чоловіків: {male_count}, Жінок: {female_count}")
        plt.pie([male_count, female_count], labels=['Чоловіки', 'Жінки'], autopct='%1.1f%%')
        plt.title("Кількість чоловіків і жінок")
        plt.show()

        # Виведення вікових категорій
        print(age_categories)
        plt.bar(age_categories.keys(), age_categories.values())
        plt.title("Кількість співробітників за віковими категоріями")
        plt.show()

        # Виведення співробітників за статтю і віком
        for category, gender_data in gender_by_age.items():
            print(f"{category}: Чоловіків: {gender_data['male']}, Жінок: {gender_data['female']}")
            plt.bar(gender_data.keys(), gender_data.values(), color=['blue', 'pink'])
            plt.title(f"Кількість чоловіків і жінок у категорії {category}")
            plt.show()

        print("Ok, аналіз даних завершено успішно.")

    except FileNotFoundError:
        print("Помилка: файл CSV не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці даних: {e}")
# Виклик функції для аналізу та побудови діаграм
analyze_data('employees.csv')