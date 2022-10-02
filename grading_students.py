#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

import math
def gradingStudents(grades):
    # Write your code here
    newGrades = []
    for a in grades:
        b = math.ceil(a/5)*5
        # print(b)
        if a<38 or (b-a)>=3:
            newGrades.append(a)
        elif (b-a)<3:
            newGrades.append(b)
    return newGrades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for i in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
