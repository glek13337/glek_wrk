def main():
    annual_salary = float(input("Введите вашу годовую зарплату: "))
    portion_saved = float(input("Введите долю зарплаты, которую будете откладывать (например, 0.1 для 10%): "))
    total_cost = float(input("Введите стоимость желаемого дома: "))

    portion_down_payment = 0.25  # 25% от стоимости дома
    r = 0.04  # годовая доходность (4%)

    current_savings = 0.0
    months = 0

    down_payment = total_cost * portion_down_payment

    while current_savings < down_payment:
        current_savings += current_savings * (r / 12)
        current_savings += (annual_salary / 12) * portion_saved
        months += 1

    print(f"\nВам понадобится {months} месяцев, чтобы накопить на первоначальный взнос.")

# Запуск программы
if __name__ == "__main__":
    main()