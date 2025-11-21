import tkinter as tk
from pygame import mixer as mxr

root = tk.Tk()
version_number = 0.1
root.title(f"PyPlayer | Version: {version_number}")
root.geometry("210x400")

title_label = tk.Label(root, text="PyPlayer", font=("Helvetica", 16))
title_label.pack(pady=10)
play_button = tk.Button(root, text="Play", command=lambda: print("Playing"))
play_button.pack(pady=10)   
pause_button = tk.Button(root, text="Pause", command=lambda: print("Paused"))
pause_button.pack(pady=10)
stop_button = tk.Button(root, text="Stop", command=lambda: print("Stopped"))
stop_button.pack(pady=10)

volume_label = tk.Label(root, text="Volume")
volume_label.pack(pady=5)
volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=150)
volume_slider.set(50)
volume_slider.pack(pady=5)

def debug():
    print("Debug Info:")
    print(f"Volume: {volume_slider.get()}")
    print(root.winfo_width(), "x", root.winfo_height())

debug_button = tk.Button(root, text="Debug Info", command=debug)
debug_button.pack(pady=10)  

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
