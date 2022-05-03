test = [
    [2,7,6],
    [9,5,1],
    [4,3,8]
]
def magic_square(table):
    rows={}
    columns= {}
    diagonal1 = []
    diagonal2 = []

    #summing the rows
    total_sum = None
    for i in range(len(table)):
        sum_r = 0
        for j in range(len(table[i])):
            sum_r += table[i][j]
        rows[f"row {i+1}"] = sum_r
        

    #summing the columns    
    for elem in range(len(table)):
        sum_c = 0
        for column in range(len(table[elem])):
            sum_c += table[column][elem]
        columns[f"col {elem +1}"] = sum_c
    

    #summing diagonals
    sum_d = 0
    sum_d1 = 0
    for elem in range(len(table)):
        sum_d += table[elem][elem]
        sum_d1 += table[elem][(len(table)-1)-elem]
            
    diagonal1.append(sum_d)
    diagonal2.append(sum_d1)

    total_sum = None
    for v in rows.values():
        if total_sum is None:
            total_sum = v
        elif total_sum != v:
            return False

    for v in columns.values():
        if total_sum != v:
            return False

    for z in diagonal1:
        if total_sum != z:
            return False

    for y in diagonal2:
        if total_sum != y:
            return False

    return True

        
        
    



result = magic_square(test)
if result:
    print("It's a magic square.")
else:
    print("It's not a magic square.")
