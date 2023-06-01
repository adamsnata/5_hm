from pages.registration import Registration
from data.user import user


def test_form_fill_in():

    registration = Registration()
    registration.open()
    registration.fill_in(user)
    registration.submit()
    registration.check(user)
