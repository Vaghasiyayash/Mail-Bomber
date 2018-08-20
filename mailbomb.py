import smtplib
while True:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_sender = 'huntrking100001@gmail.com'
    gmail_pass = 'Huntrking@702'
    gmail_receiver = 'techogamer1517@gmail.com'
    msg = '>>>SPAM'
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_pass)
    server.sendmail(gmail_sender, gmail_receiver, msg)