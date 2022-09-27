from data_manager import DataManager

data_manager = DataManager()

class Users():

    def create_user(self):
        self.first_name = input("What is your first name?\n")
        self.last_name = input("What is your last name?\n")
        self.email = "email1"
        self.check_email = "email2"
        
        while self.email != self.check_email:
            self.email = input("What is your email?\n")
            self.check_email = input("Please confirm email\n")

            if self.email != self.check_email:
                print ("Incorect email, please try again.")
            else:
                print ("Email comfirmed, you are in the club.")
        
        data_manager.add_user(self.first_name, self.last_name, self.email)