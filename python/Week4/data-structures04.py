print("hello")


class Song:
    def __init__(self):
        self.title = ""
        self.artist = ""
        
    def prompt(self):
        self.title = input("Enter the title: ")
        self.artist = input("Enter the artist: ")
        return self

    def display(self):
        print("Title: {}\nArtist: {}".format(self.title, self.artist))

from collections import deque

def main():
    playlist = deque()
    selection = ""
    while selection != "4":
        print("Options:")
        print("1. Add a new song to the end of the playlist")
        print("2. Insert a new song to the beginning of the playlist")
        print("3. Play the next song")
        print("4. Quit")
        selection = input("Enter selection: ")
        print()
        if selection == "1":
            playlist.append(Song().prompt())
            print()
        elif selection == "2":
            playlist.appendleft(Song().prompt())
            print()
        elif selection == "3":
            if len(playlist) == 0:
                print("The playlist is currently empty.")
                print()
            else:
                print("Playing song:") 
                song = playlist.popleft()
                song.display()
                print()
        else:
            print("Goodbye")

if __name__ == "__main__":
    main()
