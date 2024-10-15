# Дополнительное практическое задание по модулю 1
# Андрей Галкин


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество в строку и сортируем по возрастанию
students_=list(students)
students_.sort()
#print(students_)

# Находим средний балл, деля сумму элементов вложенного списка на их количество
ball=[(sum(grades[0])/len(grades[0])),(sum(grades[1])/len(grades[1])),(sum(grades[2])/len(grades[2])),(sum(grades[3])/len(grades[3])),(sum(grades[4])/len(grades[4]))]
#print(ball)

# Создаём словарь из двух списков
d=dict(zip(students_,ball))
print(d)