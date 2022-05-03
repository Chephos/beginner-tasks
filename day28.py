#! python3
import smtplib, os

#You can change the email address and password to any of your choice
email_address= os.environ.get('EMAIL_ADDRESS')
email_password = os.environ.get('EMAIL_PASSWORD')



def send_email(recepients:list):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(email_address,email_password)

    subject = 'Hey Buddy!'
    body = "Hey man,\nI hope you are good and your mercies endureth for ever(that came out wrong lmaoo)\nHow are you though? I sent this message using python. Python is a high level programming language and I am doing all I can to master it- I hope you are trying to master somn just like me. Let me know what you are up to.\nLove you!\n\nWarm regards\nEfosa.py,\nmuahh"

    message = f"Subject: {subject}\n\n{body}"

    smtpObj.sendmail(email_address,recepients,message)
    smtpObj.quit()

send_email(['ecxunilag@gmail.com'])#input your desired email here
