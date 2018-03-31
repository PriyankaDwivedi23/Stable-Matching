


def main():

    professors =[]
    students=[]
    n = int(input())
    for i in range(n):
        professors.append([int(x) for x in input().split(' ')])
    for j in range(n):
        students.append([int(x) for x in input().split(' ')])
    print("Professor" , professors)
    print("Student",students)
    free_professor = []
    #assign free professors
    for i in range(len(professors)):
        free_professor.append(i)
    print("Free Professor",free_professor)
    #maintain for matching

    partner_professor =[-1]*len(professors)
    partner_student = [-1]*len(students)

    while(len(free_professor) > 0):
        professorToBePaired = free_professor.pop()
        print("Current Professor " , professorToBePaired)
        for student in professors[professorToBePaired]:
            if partner_student[professorToBePaired] == -1 and partner_professor[student] == -1:
                partner_student[professorToBePaired] =student
                partner_professor[student] =professorToBePaired
                print("Now Professor ", professorToBePaired,"is paired with student ",student)
                # print("Student " ,partner_student)
                # print("Professor " , partner_professor)
                break
            else:
                currently_matched = partner_professor[student]
                print("Student ", student,"is already paired with Professor ", currently_matched)
                if(students[student].index(currently_matched)> students[student].index(professorToBePaired)):
                    partner_student[currently_matched]=-1
                    partner_student[professorToBePaired]=student
                    partner_professor[student]=professorToBePaired
                    print("New Partner formed : Professor ",professorToBePaired, 'is paired with student',student)
                    # print("Student ", partner_student)
                    # print("Professor ", partner_professor)
                    free_professor.append(currently_matched)
                    break

    print("Final Pairs are")
    print("Student ", partner_student)
    print("Professor ", partner_professor)



if __name__ == '__main__':
    main()
'''
5
0 1 2 3 4
1 2 3 0 4
2 3 0 1 4
3 0 1 2 4
0 1 2 3 4
1 2 3 4 0
2 3 4 0 1
3 4 0 1 2
4 0 1 2 3
0 1 2 3 4

'''