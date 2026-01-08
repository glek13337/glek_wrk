def main():
    annual_salary = float(input("Введите начальную годовую зарплату: "))
    portion_saved = float(input("Введите долю зарплаты которую необходимо отложить: "))
    total_cost = float(input("Введите стоимость дома вашей мечты: "))
    semi_annual_raise = float(input("Введите полугодовое повышение зарплаты: "))

    portion_down_payment = 0.25 #25% от стоимости дома мечты
    down_payment = total_cost * portion_down_payment
    r = 0.04 #годовая доходность

    current_savings = 0.0
    month = 1

    down_payment = total_cost * portion_down_payment


    while current_savings < down_payment:
        month += 1

        current_savings += current_savings * (r / 12)
        current_savings += (annual_salary / 12) * portion_saved

        if month % 6 == 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)



    print(f"\nВам понадобится {month} месяцев, чтобы накопить на первоночальный взнос.")

if __name__ == "__main__":
    main()