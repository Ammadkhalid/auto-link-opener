import unittest


class AutoLinkOpenerTest(unittest.TestCase):

    # -- @test -- #
    def test_get_account_details_from_file(self):
        import os
        from config import Config

        #Create a dummy config
        file = open('test.ini','wt')
        config = self.getTestConfig()
        file.write(config)
        file.close()

        #Get the config data
        config = Config(filename = 'test.ini')
        account = config.getAccount()

        #Compare email and password
        self.assertEqual(account['username'], 'testconfig@gmail.com')
        self.assertEqual(account['password'], 'testconfig')

        #Delete the dummy file
        os.remove('test.ini')
    
    # -- @test -- #
    def test_login_to_gmail_account(self):
        pass


    # -- Test Config -- #
    def getTestConfig(self):
        return """
        [account]
        # Put Gmail Account
        username = testconfig@gmail.com
        password = testconfig

        # Minimum Amount
        amount = $200,000

        # From
        from = no-reply@fivestreet.com
        """
    


if __name__ == "__main__":
    unittest.main()