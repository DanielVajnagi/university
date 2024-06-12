import tkinter as tk
import re

def delete_words_with_mask():
    text = text_box.get("1.0", tk.END)  # Отримуємо вміст текстового поля
    mask = mask_entry.get()  # Отримуємо маску з поля введення

    # Замінюємо метасимволи [A-Z] на відповідний регулярний вираз
    mask_regex = re.sub(r'\[([A-Z])-(?=[A-Z])?([A-Z])\]', lambda x: '[' + x.group(1) + '-' + x.group(2) + ']', mask)

    # Створюємо регулярний вираз для пошуку слів, які відповідають масці
    pattern = re.compile(mask_regex)

    # Видаляємо знайдені слова з тексту (case sensitive)
    new_text = pattern.sub('', text)

    # Оновлюємо вміст текстового поля з новим текстом
    text_box.delete("1.0", tk.END)
    text_box.insert("1.0", new_text)

# Створення головного вікна
root = tk.Tk()
root.title("Delete Words with Mask")

try:
    with open("initial_text.txt", "r") as file:
        initial_text = file.read()
except FileNotFoundError:
    initial_text = "Initial text not found."
    
# Створення текстового поля для введення тексту
text_box = tk.Text(root, height=10, width=50)
text_box.insert("1.0", initial_text)

text_box.pack(pady=10)

# Створення поля для введення маски
mask_entry = tk.Entry(root, width=30)
mask_entry.pack()

# Кнопка для запуску процесу видалення слів за маскою
delete_button = tk.Button(root, text="Delete Words", command=delete_words_with_mask)
delete_button.pack(pady=5)

root.mainloop()
