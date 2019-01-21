# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    b = []
    for a in str(ticket_number):
        b.append(int(a))
    if sum(b[:3]) == sum(b[-3:]) :
        return True
    else :
        return False
    


print(lucky_ticket(123006))
print(lucky_ticket(512321))
print(lucky_ticket(436751))