money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
total_money = money_capital + salary
while total_money > spend - salary:
    if months < 1:
        total_money -= spend
        months += 1
    if months >= 1:
        total_money += salary
        spend *= (1 + increase)
        total_money -= spend
        months += 1
print("Количество месяцев, которое можно протянуть без долгов:", months)
