class Singleton:
 _instance = None # атрибут, який зберігає екземпляр класу
 
 """ Метод __new__ викликають при створенні екземпляра класу """

 # Якщо екземпляр ще не створений, то створюємо його
 def __new__(cls, *args, **kwargs):
    if cls._instance is None:
        cls._instance = object.__new__(cls, *args, **kwargs)
 # Повертаємо екземпляр, який існує
    return cls._instance
 def __init__(self):
    self.value = 8
obj1=Singleton(); print(obj1.value)
obj2 = Singleton(); obj2.value = 42
print(obj1.value)
