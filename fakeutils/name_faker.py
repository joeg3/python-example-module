from faker import Faker

class NameFaker():

    def get_fake_name(self):
        fake = Faker()
        return fake.name()
