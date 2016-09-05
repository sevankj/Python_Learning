class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bady = Song(["Happy birthday my son"])

success = Song(["You have achieved success"])

happy_bady.sing_me_a_song()

success.sing_me_a_song()

