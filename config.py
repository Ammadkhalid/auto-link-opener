import configparser
from os.path import abspath
import os

class Config:
    def __init__(self, filename = "config.ini"):
        # get abs path
        filename = abspath(filename)

        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.read(filename)

    def getConfig(self):
        return self.config

    def read(self, file):
        filename = join("Config", file)

        try:
            file = open(filename, "r")
        except FileNotFoundError as e:
            print("Please Check {} is not exists in Config Directory".format(file))

        return file.read()

    def getMailInterval(self):
        try:
            interval = self.config.getfloat("Mail", "interval")
        except:
            interval = self.config.getint("Mail", "interval")

        return interval

    def getAccount(self):
        users = self.config.get("account", "username")
        passwords = self.config.get("account", "password")

        

        return {"username": users, "password": passwords}
