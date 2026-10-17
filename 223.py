while True:
    n = int(input())

    if n > 100:
        break  # Припиняємо зчитування чисел
    if n < 10:
        continue  # Пропускаємо число та переходимо до наступного

    print(n)

