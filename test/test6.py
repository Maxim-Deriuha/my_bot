n = int(input())#ввод количества чисел
k = 0 # число для нахождения максимума
r = 0 # число для нахождения второго максимума
for i in range(1,n+1):# цикл
    a = int(input()) # ввод чисел
    if a > k : # сравнение если введёное число больше предыдущего максимума
        r = k # запоминаем предыдущее максимальное число
    else:
        r = max(r,a) # если максимум уже был найдет то мы дальше ищем следущее максимальное число
    k = max(a,k) # нахождения максимального числа

print(k) # вывод
print(r) # вывод