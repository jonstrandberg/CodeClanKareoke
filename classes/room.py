class Room:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.guest_list = []
        self.list_of_songs = []

    def guest_count(self):
        return len(self.guest_list)

    def checkin_guest(self, guest):
        if len(self.guest_list) < self.capacity:
            self.guest_list.append(guest)
        else:
            return "Sorry room is full"

    def checkout_guest(self, guest):
        self.guest_list.remove(guest)

    def empty_song_list(self):
        return len(self.list_of_songs)
    
    def add_song_to_room(self, song):
        self.list_of_songs.append(song)

    def play_song(self):
        self.add_song_to_room
        return self.list_of_songs[-1]




