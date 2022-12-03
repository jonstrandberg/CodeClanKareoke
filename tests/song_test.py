import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Africa", "Toto")
        self.song_2 = Song("What's My Age Again", "Blink 182")
        self.song_3 = Song("Money, Money, Money", "ABBA")
        self.song_4 = Song("Gypsy", "Fleetwood Mac")
        self.song_5 = Song("Once in a Lifetime", "Talking Heads")

    def test_song_title_name(self):
        self.assertEqual("Africa", self.song.title)

    def test_song_artist_name(self):
        self.assertEqual("Toto", self.song.artist)