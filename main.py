import tkinter
import math
from PIL import ImageTk, Image

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
    c.create_line(i, 0, i, WIDTH, fill = "light grey")

for i in range(0, WIDTH, 10):
    c.create_line(0, i, HEIGHT, i, fill = "light grey")


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

    def spawn(self, coords, movement):
        p = Image.open("tank.png")
        p2 = ImageTk.PhotoImage(p)
        player2 = c.create_image(coords[0], coords[1], image = p2)
        p2.image = p2

        self.movement = movement
    def movement2(self, event="<Key>"):
        key = event.keysym
        if key == "Right":
            c.delete("all")
            for i in range(0, HEIGHT, 10):
                c.create_line(i, 0, i, WIDTH, fill = "light grey")

            for i in range(0, WIDTH, 10):
                c.create_line(0, i, HEIGHT, i, fill = "light grey")
            self.coords[0] += 3
            p = Image.open("tank.png")
            p2 = ImageTk.PhotoImage(p)
            p2.image = p2
            player2 = c.create_image(self.coords[0], self.coords[1], image=p2)

        elif key == "Left":
            c.delete("all")
            for i in range(0, HEIGHT, 10):
                c.create_line(i, 0, i, WIDTH, fill="light grey")

            for i in range(0, WIDTH, 10):
                c.create_line(0, i, HEIGHT, i, fill="light grey")
            self.coords[0] -= 3
            p = Image.open("tank.png")
            p2 = ImageTk.PhotoImage(p)
            p2.image = p2
            player2 = c.create_image(self.coords[0], self.coords[1], image=p2)
        elif key == "Up":
            c.delete("all")
            for i in range(0, HEIGHT, 10):
                c.create_line(i, 0, i, WIDTH, fill="light grey")

            for i in range(0, WIDTH, 10):
                c.create_line(0, i, HEIGHT, i, fill="light grey")
            self.coords[1] -= 3
            p = Image.open("tank.png")
            p2 = ImageTk.PhotoImage(p)
            p2.image = p2
            player2 = c.create_image(self.coords[0], self.coords[1], image=p2)
        elif key == "Down":
            c.delete("all")
            for i in range(0, HEIGHT, 10):
                c.create_line(i, 0, i, WIDTH, fill="light grey")

            for i in range(0, WIDTH, 10):
                c.create_line(0, i, HEIGHT, i, fill="light grey")
            self.coords[1] += 3
            p = Image.open("tank.png")
            p2 = ImageTk.PhotoImage(p)
            p2.image = p2
            player2 = c.create_image(self.coords[0], self.coords[1], image=p2)


def mouse_movement(event):
    x, y = event.x, event.y

player = Player(10, [0, 10, 50, 50], "blue")
player.spawn([0, 10, 50, 80], 3)


def main_game_loop():
    c.bind_all("<Key>", player.movement2)
    window.after(500, lambda: main_game_loop())


main_game_loop()

window.mainloop()  # so we can actually see stuff
