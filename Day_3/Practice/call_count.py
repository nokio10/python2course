# Как с помощью атрибутов функции посчитать количество вызовов этой функции?
def func(a=5, b=8):
    if not hasattr(func, 'call_count'):
        func.call_count = 0  # Создание счетчика при первом вызове
    func.call_count += 1  # Увеличение счетчика при каждом вызове функции
    return a + b

print(func())
print(func(10, 20))
print(func())
print(func(4, 9))
print(func(4, 9))
print(func.call_count)
print(getattr(func, 'call_count'))