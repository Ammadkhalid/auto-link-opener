import imaplib
import email, os
import email.header
from bs4 import BeautifulSoup
import re
import quopri
import requests

class EmailReader:

    def __init__(self, server='imap.gmail.com'):
        self.M = imaplib.IMAP4_SSL(server)

    def login(self, user, passwd):
        print("Logging")
        try:
            rv, data = self.M.login(user, passwd)
            print(rv)
        except imaplib.IMAP4.error as e:
            if "only allowed in states NONAUTH" in str(e):
                print("Already Logged in!")
                pass
            else:
                print ("LOGIN FAILED!!! ")
                print(e)

    def open(self, link):
        print("Opening Link:", link)
        req = requests.get(link)
        print("Status Code:",req.status_code)
        print(req.ok)


    def logout(self):
        self.M.logout()

    def processMailbox(self, _from = "no-reply@fivestreet.com", givenAmount = "200000", folder = "INBOX"):
        print("Processing Mail Inbox")
        self.M.select(folder)
        r, data = self.M.search(None, 'FROM "{}"'.format(_from), '(UNSEEN)')
        for num in data[0].split():
            rv, data = self.M.fetch(num, '(RFC822)')

            if rv != 'OK':
                print("ERROR getting message", num)
                return

            email_body = quopri.decodestring(data[0][1])

            bs = BeautifulSoup(email_body, "html.parser")

            d = "\n".join(f.text for f in bs.find_all("p") )
            t = re.findall(r"\$(.*)", d)
            click = False
            if t:
                amount = int(t[0].replace(",", ""))
                givenAmount = int(givenAmount)
                if amount >= givenAmount:
                    print("This Email is our target!")
                    click = True

            # now find btn and click
            if click:
                links = bs.findAll("a", href=True)
                for link in links:
                    if "claim" in link.text.lower():
                        # now open link
                        self.open(link['href'])
        print("Done")
