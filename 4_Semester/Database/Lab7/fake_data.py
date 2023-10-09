import random

def generate_receipt_items(num_records):
    receipt_items = set()  # Множина для зберігання унікальних комбінацій

    while len(receipt_items) < num_records:
        receipt_id = random.randint(1, 50)
        item_id = random.randint(1, 100)
        receipt_items.add((receipt_id, item_id))

    return receipt_items

def generate_insert_queries(receipt_items):
    insert_queries = []
    for receipt_item in receipt_items:
        amount = round(random.uniform(10, 50), 0)
        query = f"INSERT INTO `Invoices_Items` (`Invoice_ID`, `Item_ID`, `Amount`) VALUES ({receipt_item[0]}, {receipt_item[1]}, {amount});"
        insert_queries.append(query)
    return insert_queries

def print_insert_queries(insert_queries):
    for query in insert_queries:
        print(query)

# Задати кількість записів для генерації
num_records = 1000

# Генерувати випадкові записи та запити INSERT
receipt_items = generate_receipt_items(num_records)
insert_queries = generate_insert_queries(receipt_items)

# Вивести запити INSERT
print_insert_queries(insert_queries)
