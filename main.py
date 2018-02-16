from config import Config
from time import sleep
from reader import EmailReader
import schedule

class Main:
    def __init__(self):
        self.config = Config()

        self.reader = EmailReader()

    def main(self):
        print("checking")
        account = self.config.getAccount()
        username = account["username"]
        password = account["password"]
        amount = self.config.config.get("account", "amount").replace("$", "").replace(",", "")
        _from = self.config.config.get("account", "from")

        self.reader.login(username, password)            
        self.reader.processMailbox(_from, amount)
        # self.reader.logout()

if __name__ == "__main__":
    m = Main()
    m.main()

    schedule.every(5).seconds.do(m.main)

    while 1:
        schedule.run_pending()
        sleep(1)
