import unittest
from classes.guest import Guest
from classes.song import Song
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.room_1 = Room("The Club Tropicana Room", 4, 5)
        self.room_2 = Room("The Copacabana Room", 10, 20)
        self.room_3 = Room("Walking in Memphis Room", 20, 10)

        self.guest = Guest("Daryl Hall", 76, 20)
        self.guest_2 = Guest("John Oates", 74, 30)
        self.guest_3 = Guest("Stevie Nicks", 74, 40)
        self.guest_4 = Guest("Peter Gabriel", 72, 50)
        self.guest_5 = Guest("Kate Bush", 64, 100)

        self.song_1 = Song("Africa", "Toto")
        self.song_2 = Song("What's My Age Again", "Blink 182")
        self.song_3 = Song("Money, Money, Money", "ABBA")
        self.song_4 = Song("Gypsy", "Fleetwood Mac")
        self.song_5 = Song("Once in a Lifetime", "Talking Heads")

    def test_room_name(self):
        self.assertEqual("The Club Tropicana Room", self.room_1.name)

    def test_capacity(self):
        self.assertEqual(4, self.room_1.capacity)

    def test_room_starts_with_no_guests(self):
        self.assertEqual(0, self.room_1.guest_count())

    def test_checkin_a_guest(self):
        self.room_1.checkin_guest(self.guest)
        self.assertEqual(1, len(self.room_1.guest_list))

    def test_checkin_multiple_guests(self):
        self.room_1.checkin_guest(self.guest)
        self.room_1.checkin_guest(self.guest_2)
        self.assertEqual(2, len(self.room_1.guest_list))

    def test_remove_a_guest(self):
        self.room_1.checkin_guest(self.guest)
        self.room_1.checkout_guest(self.guest)
        self.assertEqual(0, len(self.room_1.guest_list))

    def test_that_list_of_songs_starts_empty(self):
        self.assertEqual(0, self.room_1.empty_song_list())

    def test_add_songs_to_room(self):
        self.room_2.add_song_to_room(self.song_1)
        self.assertEqual(1, len(self.room_2.list_of_songs))

