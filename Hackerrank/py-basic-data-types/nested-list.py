if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])


    marks = (x[1] for x in students)
    uniqueMarks = list(set(marks))

    sortedMarks = sorted(uniqueMarks)

    secondLowest = sortedMarks[1]

    for name in sorted([x[0] for x in students if x[1] == secondLowest]):
      print(name)