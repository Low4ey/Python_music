from playsound import playsound


chika="E:\Python_music\songs\chika.mp3"
jojo="E:\Python_music\songs\jojo.mp3"
class Stack:
    def __init__(self):
        self.list=[]
    
    def Add_Song(self,val):
            self.list.append(val)

    def peek(self):
        return self.list[len(self.list)-1]
    
    def pop(self):
        if self.list==[]:
            print(f" stack is empty")
        else:
            self.list.pop(0)


Playlist=Stack()
Playlist.Add_Song(jojo)
Playlist.Add_Song(chika)
def play_Song(ll):
    while True:
        print(f"Press 1 to play First Song\n Press 2 to Play Next Song.\n Press 3 to Add Song.\n Press 4 to Delete Current Song. \n Press 5 to Show Playlist \n Press 0 to Exit Music Player")
        choice=int(input())
        for i in Playlist.list:
            if choice==1:
                print(f"Playing song located at {i}")
                playsound(i)
                break
            elif choice==2:
                Playlist.pop()
                playsound(Playlist.list[0])
                break
            elif choice==3:
                print("Enter Music Path")
                ll.Add_Song(input())
                break
            elif choice==4:
                ll.list.pop()
            elif choice==5:
                print(i)
            elif choice==0:
                return
            else:
                print("Invalid Input")
                return

play_Song(Playlist)
