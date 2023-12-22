Input Format:

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student 2 over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints:
* 2 <= N <= 5
* There will always be one or more students having the second lowest grade.
  
Output Format:
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.




                # Code

if __name__ == '__main__':
    students = []
    scores = set()

    # Input the number of students
    
    n = int(input())

    # Input student names and grades
    
    for _ in range(n):
        name = input()
        score = float(input())
        students.append((name, score))
        scores.add(score)

    # Finding the second lowest score
    second_lowest = sorted(scores)[1]

    # Finding students with the second lowest score
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest]

    # Sorting students' names alphabetically and printing them
    second_lowest_students.sort()
    for student in second_lowest_students:
        print(student)


