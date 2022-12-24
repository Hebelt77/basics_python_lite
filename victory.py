people = ["Исаак Ньютон", "Альберт Эйнштейн", "Никола Тесла", "Томас Эдисон", "Константин Циолковский"]
year_of_birth = ["1642", "1879", "1856", "1847", "1857"]
total_true = 0
total_false = 0
end = None

while end != "нет":
    for i in range(len(people)):
        year = input(f"Введите год рождения {people[i]}: ")     # Правильные ответы:
        if year == year_of_birth[i]:                            # Исаак Ньютон - 1642
            total_true += 1                                     # Альберт Эйнштейн - 1879
        else:                                                   # Никола Тесла - 1856
            total_false += 1                                    # Томас Эдисон - 1847
    percent_true = total_true * 100 / len(people)               # Константин Циолковский - 1857
    print(f'''  Количество правильных ответов - {total_true}  
  Количество неправильных ответов - {total_false}
  Процент правильных ответов - {percent_true}%
  Процент неправильных ответов - {100 - percent_true}%''')
    end = (input(f"Хотите начать игру сначала?: 'Да/Нет': ")).lower()