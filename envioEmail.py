import smtplib
import email.message

def send_email():
    body = '''
    <p>Cotação das maiores ações da B3<p>
    '''

    msg = email.message.EmailMessage()
    subject = input("Subject: ")
    who = input("Sent From: ")
    to = input('Sent to: ')
    msg['Subject'] = subject
    msg['From'] = who
    msg['To'] = to
    password = input('type your password: ')

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Sent!')

send_email()