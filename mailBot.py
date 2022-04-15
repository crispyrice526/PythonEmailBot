
import smtplib

i = 0

print("Hello! Welcome to the simpliest email bot ever! Make sure to use a throw away email when sending emails with this software! ")

baseEmail = input("What is your email: ")
emailPass = input("What is your email password? This is required for the software to send emails from your account: ")
receiverEmail = input("What email address do you want to send the emails too:" )
runTime = input("How many emails do you want to send: ")
subject = input("Email Subject: ")
body = input("Email Main Text: ")



while i < int(runTime):
	i += 1
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()

		smtp.login(baseEmail, emailPass)
		msg = f"Subject: {subject}\n\n{body}"

		smtp.sendmail(baseEmail, receiverEmail, msg)