print(isinstance(8, int)) # True
print(isinstance('str', int)) # False
print(isinstance(True, bool)) # True
print(isinstance(True, int)) # True, тому що bool - підклас int
print(isinstance('a string', object)) # True, все є об‘єктами
print(isinstance(None, object)) # True, навіть None
print(isinstance(False, str)) # False
print(isinstance(int, type)) # True, будь-який клас – об‘єкт-екземпляр метакласу type
print(isinstance(42, type)) # False, 42 – це не тип даних