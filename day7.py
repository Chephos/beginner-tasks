#Wordle
import random
game_active = True
word_list = [
    'crown','build','logic','plane',
    'focus','money','plant','plate',
    'pound',"other",'input','horse',
    'green','group','beans','guide',
    'layer','mayor','lunch','limit',
    'model','point','scope','score',
    'skate','title','total','world',
]

while game_active:
    prompt = input(f"You have six attempts.\n(Type q to exit and y to begin): ")
    if prompt.lower() == 'q':
        game_active = False
    elif prompt.lower()=='y':
        inner_loop = 0
        print(f"Enter your 5 letter word:")
        hidden_wrd = random.choice(word_list)
        print(hidden_wrd)
        while inner_loop < 6 and game_active:
            #print(inner_loop)
            attempt = input()
            

            #Game logic
            output = ""
            if len(attempt) !=5:
                print("Input a 5 letter word!!")
                continue
            for i in range(attempt.__len__()):
                if attempt[i] in hidden_wrd:
                    if attempt[i] == hidden_wrd[i]:
                        output += "√"
                    # elif attempt[i] in hidden_wrd:
                    #     if attempt[i] != hidden_wrd[i]:
                    #         output += "x"
                    else:
                        output += '+'
                elif attempt[i] not in hidden_wrd:
                    output += "x" 
            inner_loop +=1
            print(output)
            if attempt == hidden_wrd:
                print("You win!")
                game_active = False
                
            if inner_loop == 6:
                print("You've exhausted all your chances! ")
                game_active = False
                

