pushkin_year_of_birth = "1799"
pushkin_day_of_birth = "6 июня"
year_of_birth = None
day_of_birth = None

while year_of_birth != pushkin_year_of_birth:
    year_of_birth = input("Введите год рождения А.С. Пушкина: ")
    if year_of_birth == pushkin_year_of_birth:
        while day_of_birth != pushkin_day_of_birth:
            day_of_birth = input("Введите день рождения А.С. Пушкина: ")
            if day_of_birth == pushkin_day_of_birth:
                print("Верно")
    else:
        print("Неверно, попробуйте ещё раз!")