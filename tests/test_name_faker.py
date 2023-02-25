from fakeutils.name_faker import NameFaker

def test_name_faker():
    nf = NameFaker
    name = nf.get_fake_name()
    print("Name: ", name)