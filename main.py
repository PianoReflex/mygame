import tkinter
import math
from PIL import ImageTk, Image

# initialize our window to display graphics
window = tkinter.Tk()
window.title("bad game")
HEIGHT = window.winfo_screenheight()  # finds height of window
WIDTH = window.winfo_screenwidth()  # finds width of window
window.geometry("{1}x{0}".format(int(HEIGHT / 2), int(WIDTH / 2)))

c = tkinter.Canvas(window, height=HEIGHT * 2, width=WIDTH * 2,
                   highlightthickness=0)
c.place(x=WIDTH/2 + (WIDTH/4), y=HEIGHT/2, anchor="center")  # put the canvas widget inside our window
window.wm_attributes("-transparentcolor", "white")
for i in range(0, HEIGHT, 10):
    c.create_line(i, 0, i, WIDTH, fill="light grey")

for i in range(0, WIDTH, 10):
    c.create_line(0, i, HEIGHT, i, fill="light grey")


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

    def spawn(self, coords, movement, canv_coord_x, canv_coord_y, move):
        p = Image.open("tank.png")
        p2 = ImageTk.PhotoImage(p)
        p2.image = p2

        self.movement = movement
        self.canv_coord_x = WIDTH/2 + (WIDTH/4)
        self.canv_coord_y = HEIGHT/2
        self.player_coord_x = coords[0]
        self.player_coord_y = coords[1]
        self.move = move

        c.place(x = WIDTH/2 + (WIDTH/4), y = HEIGHT/2, anchor = "center")
        player2 = c.create_image(coords[0], coords[1], image=p2)

    def movement2(self, event="<Key>"):
        key = event.keysym
        if key == "Right":
            c.delete("all")
            for i in range(0, HEIGHT, 10):
                c.create_line(i, 0, i, WIDTH, fill="light grey")

            for i in range(0, WIDTH, 10):
                c.create_line(0, i, HEIGHT, i, fill="light grey")
            p = Image.open("tank.png")
            p2 = ImageTk.PhotoImage(p)
            p2.image = p2
            self.canv_coord_x -= self.move
            self.coords[0] += self.move
            c.place(x=self.canv_coord_x, y=self.canv_coord_y, anchor="center")
            player2 = c.create_image(self.coords[0], self.coords[1], image=p2)

        elif key == "Left":
            c.delete("all")
            for i in range(0, HEIGHT, 10):
                c.create_line(i, 0, i, WIDTH, fill="light grey")

            for i in range(0, WIDTH, 10):
                c.create_line(0, i, HEIGHT, i, fill="light grey")
            p = Image.open("tank.png")
            p2 = ImageTk.PhotoImage(p)
            p2.image = p2
            self.canv_coord_x += self.move
            self.coords[0] -= self.move
            c.place(x=self.canv_coord_x, y=self.canv_coord_y, anchor="center")
            player2 = c.create_image(self.coords[0], self.coords[1], image=p2)
        elif key == "Up":
            c.delete("all")
            for i in range(0, HEIGHT, 10):
                c.create_line(i, 0, i, WIDTH, fill="light grey")

            for i in range(0, WIDTH, 10):
                c.create_line(0, i, HEIGHT, i, fill="light grey")
            p = Image.open("tank.png")
            p2 = ImageTk.PhotoImage(p)
            p2.image = p2
            self.canv_coord_y += self.move
            self.coords[1] -= self.move
            c.place(x=self.canv_coord_x, y=self.canv_coord_y, anchor="center")
            player2 = c.create_image(self.coords[0], self.coords[1], image=p2)
        elif key == "Down":
            c.delete("all")
            for i in range(0, HEIGHT, 10):
                c.create_line(i, 0, i, WIDTH, fill="light grey")

            for i in range(0, WIDTH, 10):
                c.create_line(0, i, HEIGHT, i, fill="light grey")
            p = Image.open("tank.png")
            p2 = ImageTk.PhotoImage(p)
            p2.image = p2
            self.canv_coord_y -= self.move
            self.coords[1] += self.move
            c.place(x=self.canv_coord_x, y=self.canv_coord_y, anchor="center")
            player2 = c.create_image(self.coords[0], self.coords[1], image = p2)


def mouse_movement(event):
    x, y = event.x, event.y


player = Player(10, [WIDTH/2, HEIGHT/2 + (HEIGHT/4)], "blue")
player.spawn([WIDTH/2, HEIGHT/2 + (HEIGHT/4)], 3, WIDTH/2, HEIGHT/2, 3)


def main_game_loop():
    c.bind_all("<Key>", player.movement2)
    window.after(60, lambda: main_game_loop())


main_game_loop()

window.mainloop()  # so we can actually see stuff
