from faker import Faker

class FakeIt:
    def __init__(self, locale):
        self.local = locale
        self.fake = Faker(self.local)
        self._runIt()
    def _runIt(self):
        fake_name = self.fake.name()
        fake_address = self.fake.address()
        fake_job_title = self.fake.job()
        fake_bank_name = self.fake.bank_country()
        fake_username = self.fake.user_name()
        fake_email = self.fake.email()
        fake_phone_number = self.fake.phone_number()
        fake_credit_card_number = self.fake.credit_card_number()
        fake_ssn = self.fake.ssn()
        fake_birthdate = self.fake.date_of_birth(minimum_age=18, maximum_age=90)
        
        print("Name:", fake_name)
        print("Address:", fake_address)
        print("Job Title:", fake_job_title)
        print("Bank Name:", fake_bank_name)
        print("Username:", fake_username)
        print("Email:", fake_email)
        print("Phone Number:", fake_phone_number)
        print("Credit Card Number:", fake_credit_card_number)
        print("SSN:", fake_ssn)
        print("Birthdate:", fake_birthdate)
        input("\nPress Enter to continue...")