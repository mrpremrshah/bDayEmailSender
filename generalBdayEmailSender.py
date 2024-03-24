import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from datetime import date

global b_day_diff
global age

days = [31,28,31,30,31,30,31,31,30,31,30,31]

def day_calculator(monthnumero,storing_variable):
    for k in range(0,int(monthnumero-1)):
        storing_variable += days[k]
    return storing_variable

b_day_diff = 0
current_day_dif = 0

today = date.today()

today_month = today.strftime("%m")
int_today_month = int(today_month)

today_day = today.strftime("%d")
int_today_day = int(today_day)

today_year = today.strftime("%Y")
int_today_year = int(today_year)

#current_total_days represent the amount of days it has been since the start of the current year

current_day_dif = day_calculator(int_today_month,current_day_dif)+int_today_day



def send_email(name,age):
    # Replace with your actual Gmail credentials
    sender_address = ''
    sender_pass = ''
    receiver_address = ''

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Birthday'

    # Add the body of your email here
    email_body = f"""
    Hello,

    It is {name}'s {age} birthday in one week

    """

    # Attach the body as a plain text part
    message.attach(MIMEText(email_body, 'plain'))

    # Create SMTP session for sending the mail
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_address, sender_pass)
            
        # Send the email
        server.sendmail(sender_address, receiver_address, message.as_string())
        server.quit()
        print('Email sent successfully.')
    except Exception as e:
        print('An error occurred:', str(e))



def bDay_Checker(name,birth_month,birth_day,birth_year):
    age = int_today_year-birth_year
    if birth_month == 1 and birth_day < 8:
        b_day_diff = 365+int(birth_day)
        age = int_today_year-birth_year+1
        if b_day_diff-current_day_dif==7:
            send_email(name,age)
        if b_day_diff-current_day_dif==1:
            send_email(name,age)
        exit()
        
    if (day_calculator(birth_month,b_day_diff)+birth_day)-current_day_dif==7:
        send_email(name,age)
    if (day_calculator(birth_month,b_day_diff)+birth_day)-current_day_dif==1:
        send_email(name,age)

def real_code():
# enter people's birthdays here
    bDay_Checker("example", 10, 5, 2005)