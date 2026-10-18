from queue import Queue
from itertools import count


# Створюємо чергу заявок
request_queue = Queue()

# Лічильник для унікальних номерів заявок
request_counter = count(1)


def generate_request():
    """Створює нову заявку та додає її до черги."""
    request_id = next(request_counter)

    request = {
        "id": request_id,
        "description": f"Заявка №{request_id}"
    }

    request_queue.put(request)

    print(
        f"Створено {request['description']} "
        f"та додано до черги."
    )


def process_request():
    """Обробляє першу заявку з черги."""
    if not request_queue.empty():
        request = request_queue.get()

        print(
            f"Обробляється {request['description']}."
        )

        request_queue.task_done()

        print(
            f"{request['description']} успішно оброблено."
        )
    else:
        print("Черга заявок порожня.")


def main():
    print("Система обробки заявок сервісного центру.")
    print("Enter — створити та обробити нову заявку.")
    print("q — завершити програму.")

    while True:
        command = input("\nВаш вибір: ").strip().lower()

        if command == "q":
            print("Роботу програми завершено.")
            break

        generate_request()
        process_request()


if __name__ == "__main__":
    main()