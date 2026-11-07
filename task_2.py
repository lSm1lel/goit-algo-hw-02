from collections import deque


def is_palindrome(text):
    """
    Перевіряє, чи є рядок паліндромом.

    Регістр символів та пробіли не враховуються.
    """

    # Прибираємо пробіли та переводимо символи
    # у нижній регістр
    normalized_text = "".join(
        char.lower()
        for char in text
        if not char.isspace()
    )

    # Додаємо символи до двосторонньої черги
    chars = deque(normalized_text)

    # Порівнюємо символи зліва та справа
    while len(chars) > 1:
        left_char = chars.popleft()
        right_char = chars.pop()

        if left_char != right_char:
            return False

    return True


def main():
    text = input("Введіть рядок: ")

    if is_palindrome(text):
        print("Рядок є паліндромом.")
    else:
        print("Рядок не є паліндромом.")


if __name__ == "__main__":
    main()
