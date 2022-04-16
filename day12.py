studentemail = '@student.college.edu' 
std_count = 0
profemail = "@prof.college.edu" 
prof_count = 0
num_of_emails = int(input("How many emails do you want to type in? "))
for email in range(num_of_emails):
    user_email = input(f"Email {email+1}: ")
    if user_email.endswith(profemail):
            prof_count += 1
    elif user_email.endswith(studentemail):
            std_count += 1
print(f"You entered {prof_count} proffessor emails.")
print(f"You entered {std_count} student emails.")







# Initial thought process
# studentemail = '@student.college.edu' # len 20
# studentemail_reversed = studentemail[::-1]
# std_count = 0
# profemail = "@prof.college.edu" # len 17
# profemail_reversed = profemail[::-1]
# prof_count = 0
# num_of_emails = int(input("How may emails do you want to type in? "))
# for email in range(num_of_emails):
#     user_email = input(f"Email {email+1}: ")
#     user_email_reversed = user_email[::-1]
#     if user_email_reversed[:17] == profemail_reversed:
#             prof_count += 1
#     if user_email_reversed[:20]== studentemail_reversed:
#             std_count += 1
# print(f"You entered {prof_count} proffessor emails.")
# print(f"You entered {std_count} student emails.")

