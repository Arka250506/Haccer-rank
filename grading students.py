def gradingStudents(grades):
    # Write your code here
    nilai = []
    for hasil in grades:
        if hasil  >= 38 :
            bagi5 = hasil  % 5 
            if bagi5 >= 3 :
                hasil +=  (5 - bagi5) 
        nilai.append(hasil)
    return nilai                          
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
