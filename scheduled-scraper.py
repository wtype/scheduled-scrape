import requests
from bs4 import BeautifulSoup
import smtplib
import sched, time

s = sched.scheduler(time.time, time.sleep)

def do_this(sc):
	i = 1
	url = "URL_TO_SCRAPE"
    email_content = "EMAIL CONTENT"
    send_to = "EMAIL(S) TO SEND TO"
    my_login = "LOGIN"
    my_password = "PASSWORD"
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	nostock = soup.find_all("div", {"class": "not-available"})

	while i == 1:
		if nostock:
			print("no stock")
			i=2

		else:
			print("yes stock")
			content = email_content
			mail = smtplib.SMTP("smtp.gmail.com", 587)
			mail.ehlo()
			mail.starttls()
			mail.login(my_login, my_password)
			mail.sendmail(send_to, content)
			mail.close()
			i=1

	print(nostock)
	s.enter(300, 1, do_this, (sc,))

s.enter(300, 1, do_this, (s,))
s.run()
