from faker import Faker

class NameFaker():

    def get_fake_name():
        fake = Faker()
        return fake.name()
