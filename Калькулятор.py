import math

def enhanced_calculator():
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Ошибка: деление на ноль!",
        '^': lambda x, y: x ** y,
        'sqrt': lambda x, _: math.sqrt(x) if x >= 0 else "Ошибка: корень из отрицательного числа!"
    }
    
    print("=" * 40)
    print("УЛУЧШЕННЫЙ КАЛЬКУЛЯТОР")
    print("=" * 40)
    print("Доступные операции:")
    print("+ : Сложение")
    print("- : Вычитание")
    print("* : Умножение")
    print("/ : Деление")
    print("^ : Возведение в степень")
    print("sqrt : Квадратный корень")
    print("exit : Выход")
    print("=" * 40)
    
    while True:
        try:
            op = input("\nВведите операцию (или 'exit' для выхода): ").strip().lower()
            
            if op == 'exit':
                print("Выход из калькулятора. До свидания!")
                break
            
            if op not in operations:
                print("Неизвестная операция!")
                continue
            
            if op == 'sqrt':
                num = float(input("Введите число: "))
                result = operations[op](num, None)
            else:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                result = operations[op](num1, num2)
            
            print(f"Результат: {result}")
            
        except ValueError:
            print("Ошибка: введите корректное число!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

# Запуск улучшенного калькулятора
if __name__ == "__main__":
    enhanced_calculator()