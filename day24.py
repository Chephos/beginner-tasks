def bubble_sort(list:list,order:str)-> list:
    """Returns a sorted list"""
    if order == 'a':

        # try:
            for index,element in enumerate(list):
                z=len(list)-(len(list)-index+1)
                for j in range(z,len(list)):
                    if element > list[j]:
                        list[index],list[j] = list[j],list[index]
                        continue

            return list
        # except TypeError:
        #     print("Input a List!")


    elif order == 'd':

        # try:
            for index, element in enumerate(list):
                z=len(list)-(len(list)-index+1)
                for j in range(z,len(list)):
                    if element < list[j]:
                        list[index],list[j] = list[j],list[index]
                        

            return list
        # except TypeError:
        #     print("Input a List!")

        
test = ['a','z','d','e','f','g','h']
print(bubble_sort(test,'a'))