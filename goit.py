import queue
import time
import threading
import random
from collections import deque

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    while True:
        # Створення унікального номера для заявки
        request_id = random.randint(1000, 9999)
        # Додавання заявки до черги
        request_queue.put(request_id)
        print(f"Заявка {request_id} додана до черги")
        # Затримка перед наступною генерацією заявки
        time.sleep(random.uniform(1, 3))

# Функція для обробки заявок
def process_request():
    while True:
        if not request_queue.empty():
            # Видалення заявки з черги
            request_id = request_queue.get()
            print(f"Заявка {request_id} обробляється")
            # Імітація обробки заявки
            time.sleep(random.uniform(2, 5))
        else:
            print("Черга заявок пуста")
        # Затримка перед перевіркою черги на наявність заявок
        time.sleep(1)

# Створення та запуск потоків для генерації та обробки заявок
generate_thread = threading.Thread(target=generate_request)
process_thread = threading.Thread(target=process_request)

generate_thread.start()
process_thread.start()

# Очікування завершення виконання потоків
generate_thread.join()
process_thread.join()
def is_palindrome(s):
    # Перетворення рядка у нижній регістр та видалення пробілів
    s = s.lower().replace(" ", "")
    # Створення двосторонньої черги
    queue = deque(s)
    
    # Порівняння символів з обох кінців черги
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    
    return True

# Приклад використання функції
string1 = "A man a plan a canal Panama"
string2 = "racecar"
print(is_palindrome(string1))  # True
print(is_palindrome(string2))  # True
