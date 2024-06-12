import random
import os


def generate_word(mask):
    word = ""
    countdown=0
    for char in mask:
        if char == '[':
            # Знаходимо індекси початкового та кінцевого символів діапазону
            start_index = mask.index('[') + 1
            end_index = mask.index(']')
            # Отримуємо початковий та кінцевий символи діапазону
            start_char = mask[start_index]
            end_char = mask[end_index - 1]  # Включаємо останній символ діапазону
            # Визначаємо випадковий символ з діапазону
            word += chr(random.randint(ord(start_char), ord(end_char)))
            countdown=4
        elif countdown!=0:
            countdown-=1
        else:
            word += char
    return word

def generate_words(mask, count):
    words = []
    for _ in range(count):
        word = generate_word(mask)
        words.append(word)
    return words

def print_words(words, filename=None):
    for word in words:
        print(word)
        if filename:
            with open(filename, 'a') as file:
                file.write(word + '\n')

def main():
    mask = input("Enter mask: ")
    count = int(input("Enter the number of words to generate: "))

    generated_words = generate_words(mask, count)
    print("Generated words:")
    print_words(generated_words)

    filename = "generated_words.txt"
    if os.path.exists(filename):
        os.remove(filename)
    print("Writing words to file", filename)
    print_words(generated_words, filename)

if __name__ == "__main__":
    main()
