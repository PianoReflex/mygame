import tkinter

# import math
# import PIL

# initialize our window to display graphics
window = tkinter.Tk()
window.title("bad game")
HEIGHT = window.winfo_screenheight()  # finds height of window
WIDTH = window.winfo_screenwidth()  # finds width of window
window.geometry("{1}x{0}".format(int(HEIGHT / 2), int(WIDTH / 2)))

c = tkinter.Canvas(window, height=int(HEIGHT / 2), width=int(WIDTH / 2),
                   highlightthickness=0)
c.pack()  # put the canvas widget inside our window
for i in range(0, HEIGHT, 10):
    c.create_line(i, 0, i, WIDTH)

for i in range(0, WIDTH, 10):
    c.create_line(0, i, HEIGHT, i)


class Player:
    def __init__(self, movement_speed, coords, color):
        """
        size parameter: adjusts size of player
        movement_speed parameter: adjusts speed of our player
        coords parameter: sets spawn coordinates of player
        """
        self.coords = coords
        self.movement_speed = movement_speed
        self.color = color

    def spawn(self, coords):
        self.player2 = c.create_oval(coords, fill=self.color, outline=self.color)
        self.player_gun = c.create_rectangle(coords[2] / 2, coords[3] / 1.4, (coords[2] / 2) + 2.5 * (coords[3] / 2),
                                        (coords[1] / 2) + 0.5 * (coords[1] / 0.25), fill="grey", outline="grey")
        print(coords[0] / 2, coords[1] / 2)

    def movement(self, event = "<Key>"):
        key = event.keysym
        if key == "Right":
            c.move(self.player2, 1, 0)
            c.move(self.player_gun, 1, 0)
        elif key == "Left":
            c.move(self.player2, -1, 0)
            c.move(self.player_gun, -1, 0)
        elif key == "Up":
            c.move(self.player2, 0, -1)
            c.move(self.player_gun, 0, -1)
        elif key == "Down":
            c.move(self.player2, 0, 1)
            c.move(self.player_gun, 0, 1)



player = Player(10, (0, 10, 50, 50), "blue")
player.spawn((0, 10, 50, 60))
def main_game_loop():
    c.bind_all("<Key>", player.movement)
    window.after(60, lambda: main_game_loop())


main_game_loop()

window.mainloop()  # so we can actually see stuff
