import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Daryl Hall", 76, 20)
        self.guest_2 = Guest("John Oates", 74, 8)
        self.guest_3 = Guest("Stevie Nicks", 74, 40)
        self.guest_4 = Guest("Peter Gabriel", 72, 50)
        self.guest_5 = Guest("Kate Bush", 64, 100)

        self.room_1 = Room("The Club Tropicana Room", 4, 5)
        self.room_2 = Room("The Copacabana Room", 10, 20)
        self.room_3 = Room("Walking in Memphis Room", 20, 10)   


    def test_customer_name(self):
        self.assertEqual("Daryl Hall", self.guest.name)

    def test_customer_age(self):
        self.assertEqual(76, self.guest.age)

    def test_pay_for_entry(self):
        entry_fee = Room ("The Club Tropicana Room", 4, 5)
        self.guest.pay_for_entry(entry_fee)
        self.assertEqual(15, self.guest.wallet)

    def test_sufficient_funds_for_entry(self):
        self.assertEqual(True, self.guest.guest_has_sufficient_funds(self.room_1))

    def test_insufficient_funds_for_entry(self):
        self.assertEqual(False, self.guest_2.guest_has_sufficient_funds(self.room_2))
    





