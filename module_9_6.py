def all_variants(text):
    # Опишите логику работы внутри функции all_variants.
    for x in range(len(text)):
        for r in range(len(text)-x):
            yield text[r:r + x + 1]


# Вызовите функцию all_variants и выполните итерацию
a = all_variants("abc")
for i in a:
    print (i)