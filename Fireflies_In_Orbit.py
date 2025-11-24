"""
Orbiting Fireflies Project:
"""

# importing relevant libraries
import simplegui
import math
import random

# creating the dimensions of the window
WIDTH = 600
HEIGHT = 400

CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

# Global Settings
NUM_FIREFLIES = 7

speed_scale = 1.0
timer_running = False

fireflies = []


# function for creating each individual firefly
def new_firefly():
    return {
        "angle": random.uniform(0, 2 * math.pi),

        "speed": random.uniform(0.01, 0.05),

        "radius": random.uniform(50, 150),

        "color": random.choice(["red", "orange", "yellow", "green", "blue", "purple", "pink"]),

        "size": random.randint(3, 6),

    }


# Creates all fireflies
for _ in range(NUM_FIREFLIES):
    fireflies.append(new_firefly())


# timer used to update all angles
def update_angles():
    for f in fireflies:
        f["angle"] += f["speed"] * speed_scale


# draw: convert the dimensions and draw each firefly
def draw(canvas):
    # display speed multiplier
    canvas.draw_text("Speed: x" + str(round(speed_scale, 2)), (20, 30), 20, "orange")

    for f in fireflies:
        # convert polar coordinates to (x,y)
        x = CENTER_X + f["radius"] * math.cos(f["angle"])
        y = CENTER_Y + f["radius"] * math.sin(f["angle"])

        # Add the flicker effect
        flicker = random.uniform(-2, 2)
        glow_size = max(1, f["size"] + flicker)

        # draw the firefly
        canvas.draw_circle((x, y), glow_size, 1, f["color"], f["color"])


# Button Handlers
def start_stop():
    global timer_running

    if timer_running:
        timer.stop()
        timer_running = False
    else:
        timer.start()
        timer_running = True


def faster():
    global speed_scale
    speed_scale *= 1.2


def slower():
    global speed_scale
    speed_scale *= 0.8


# Frame and Timer Setup
frame = simplegui.create_frame("Orbiting Fireflies", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# User Buttons
frame.add_button("Start / Stop", start_stop, 100)
frame.add_button("Faster", faster, 100)
frame.add_button("Slower", slower, 100)

# timer
timer = simplegui.create_timer(30, update_angles)

# start the frame
frame.start()