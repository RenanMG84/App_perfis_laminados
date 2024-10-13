import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a Frame without a background color
frame = tk.Frame(root, width=200, height=100)
frame.pack()

# Change the background color later
frame.configure(bg="lightgreen")

# Start the Tkinter main loop
root.mainloop()
