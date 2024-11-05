def find_common_participants(f, s, a=','):
    f = f.split(a)
    s = s.split(a)
    res = list(set(f).intersection(set(s)))
    res.sort()
    return res

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(f"{find_common_participants(participants_first_group, participants_second_group, a='|')}")
