class Guest:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        # self.favourite_song = favourite_song

    def pay_for_entry(self, room):
        self.wallet -= room.price

    def guest_has_sufficient_funds(self, room):
        return self.wallet >= room.price
