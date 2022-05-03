def prime_numbers(n:int) -> list:
    """Returns a list of prime numbers from 2 to n"""

    prime_no = [i for i in range(2,n+1)]
    stop = True

    
    p=2
    for index,num in enumerate(prime_no):
            
            if num%p == 0 and num != p:
                prime_no.pop(index)
                # print(prime_no)
                continue
            else:
                #for j in range(len(prime_no)):
                    if num > p:
                        p = num
                        print('x')
                        continue
                    else:
                        break
                # if x > p:
                #     p=x

        
        # for j in prime_no:
        #     if j>p:
        #         p = j
        #         stop = True
        #     else:
        #         stop = False

    return prime_no

print(prime_numbers(100))