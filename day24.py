def bubble_sort(list:list,order:str)-> list:
    """Returns a sorted list"""
    if order == 'a':
        try:
            for index, element in enumerate(list):
                z=len(list)-(len(list)-index+1)
                # if element < list[z]:
                #     list[z],list[index]=list[index],list[z]
                    
                for i in range(z,len(list)):
                    if list[i] < list[z]:
                        list[z],list[i]=list[i],list[z]
            return list

        except TypeError:
            print("Input a List!")

        


    elif order == 'd':

        try:
            for index, element in enumerate(list):
                z=len(list)-(len(list)-index+1)
                # if element > list[z]:
                #         list[index],list[z] = list[z],list[index]
                for nxt_elem in range(z,len(list)):
                    if list[nxt_elem] > list[z]:
                        list[nxt_elem],list[z] = list[z],list[nxt_elem]
                        

            return list
        except TypeError:
            print("Input a List!")

        
test = ['a','z','d','e','f','g','h']
numbers = [1,5,3,4,7,2,56,34,23,11,345,676,55,433,767,77,65,8,65]
print(bubble_sort(numbers,'a'))