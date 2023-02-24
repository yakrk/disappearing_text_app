import tkinter as tk
from tkinter import ttk


# Create a view with Tkinter
BACKGROUND_COLOR = "white"
# Create window
window = tk.Tk()
window.title("Watermark Maker")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
window.geometry("800x400")
set_font = 'C:\Windows\Fonts\Arial.ttf'

entered_text = ""


class Timer:
    def __init__(self):
        self.count = 5
        self.count_down()
        self.timer = None

    def count_down(self):
        global entered_text
        remaining_time.config(text=f"Remaining time: {self.count} seconds")
        if self.count > 0:
            self.count -= 1
            self.timer = window.after(1000, self.count_down)
        else:
            text_label.config(text="")
            entered_text = ""
        window.update()

    def reset_countdown(self):
        self.count = 5
        window.after_cancel(self.timer)

# catch typing event and show text


def type_event(event):
    global entered_text
    global countdown
    countdown.reset_countdown()
    entered_text = entered_text + event.char
    text_label.config(text=f"{entered_text}")
    countdown.count_down()


# Create remaining time label
remaining_time = tk.Label(
    text="", background=BACKGROUND_COLOR, font=("Arial", 12))
remaining_time.pack()

# Show entered text
text_label = tk.Label(text="Enter text here:\n", background=BACKGROUND_COLOR, anchor="w",
                      width=400, wraplength=700, justify="left", font=("Arial", 14), foreground="#000000")
text_label.pack()

# set timer
countdown = Timer()

# catch user keyboard entry
event_sequence = '<KeyPress>'
window.bind(event_sequence, type_event)


window.mainloop()
