def main():
    annual_salary = float(input("Введите вашу годовую зарплату: "))

    total_cost = 1000000
    portion_down_payment = 0.25
    down_payment = total_cost * portion_down_payment
    r = 0.04
    months = 36

    low = 0
    high = 10000
    epsilon = 100
    steps = 0

    found = False

    while True:
        steps += 1
        mid = (low + high) // 2
        portion_saved = mid / 10000

        current_savings = 0.0
        for month in range(months):
            current_savings += current_savings * (r / 12)
            current_savings += (annual_salary / 12) * portion_saved

        if abs(current_savings - down_payment) <= epsilon:
            found = True
            break
        elif current_savings < down_payment:
            low = mid + 1
        else:
            high = mid - 1

        if low > high:
            break

    
    if found:
        print(f"Лучший вариант откладывать: {portion_saved:.4f} (доля от зарплаты)")
        print(f"Количество шагов двоичного поиска: {steps}")
    else:
        print("Невозможно накопить первоначальный взнос за 36 месяцев с этой зарплатой.")

if __name__ == "__main__":
    main()









