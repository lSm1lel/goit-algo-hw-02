
from collections import deque


def is_palindrome(text):
    text = "".join(char.lower() for char in text if not char.isspace())
    chars = deque(text)

    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False

    return True


def main():
    text = input("Введіть рядок для перевірки: ")

    if is_palindrome(text):
        print("Рядок є паліндромом.")
    else:
        print("Рядок не є паліндромом.")


if __name__ == "__main__":
    main()
