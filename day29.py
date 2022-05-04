
def gpa_calculator(result:list)->float:
    """Returns the GPA of the student."""
    total_credit_unit = 0
    total_quality_point = 0

    for grade,credit_unit in result:
            

        total_credit_unit += credit_unit

        if grade.upper() == 'A':
            total_quality_point += (credit_unit*5)  
                    

        elif grade.upper() == 'B':
            total_quality_point += (credit_unit*4)  
                    

        elif grade.upper() == 'C':
            total_quality_point += (credit_unit*3)  
                    

        elif grade.upper() == 'D':
            total_quality_point += (credit_unit*2)  
                    

        elif grade.upper() == 'E':
            total_quality_point += (credit_unit*1)  
                    
        elif grade.upper() == 'F':
            total_quality_point += (credit_unit*0) 
            

    gpa = float((total_quality_point)/(total_credit_unit))
    

    return round(gpa,2)

#the input should be in the format [(grade,credit unit),(grade,i.e"A" or"B".,credit unit)...]
student1 = [('B',3),('C',2,),('c',1),('b',4),('a',5),('d',2)]
# for v,i in student1:
#     print(v.upper(),i)


print(f'GPA: {gpa_calculator(student1)}')
