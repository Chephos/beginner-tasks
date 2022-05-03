
def gpa_calculator(result:dict):
    """Returns the GPA of the student."""
    total_credit_unit = 0
    total_quality_point = 0

    for grade,credit_unit in result.items():
        total_credit_unit += credit_unit

        if grade.upper() == 'A':
            total_quality_point += (credit_unit*5)  
            print(total_quality_point)

        elif grade.upper() == 'B':
            total_quality_point += (credit_unit*4)  
            print(total_quality_point)
            
        elif grade.upper() == 'C':
            total_quality_point += (credit_unit*3)  
            print(total_quality_point)

        elif grade.upper() == 'D':
            total_quality_point += (credit_unit*2)  
            print(total_quality_point)

        elif grade.upper() == 'E':
            total_quality_point += (credit_unit*1)  
            print(total_quality_point)

        elif grade.upper() == 'F':
            total_quality_point += (credit_unit*0) 
            print(total_quality_point)

    gpa = float((total_quality_point)/(total_credit_unit))
    print(total_quality_point,total_credit_unit)

    return gpa

student1 = {'B':3,'C':2,'C':1,'b':4,'a':5,'d':2}
print(f'GPA: {gpa_calculator(student1)}')