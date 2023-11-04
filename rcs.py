import os
import random
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def from_func():
    filepath = filedialog.askdirectory(initialdir='D:\Anas Files\Videos')
    fromdir.set(filepath)

def to_func():
    filepath = filedialog.askdirectory(initialdir='D:\Anas Files\Videos')
    todir.set(filepath)

video_format = ('.webm', '.mkv', '.flv', '.vob', '.ogg', '.mp4')

# window
window = tk.Tk()
window.geometry('500x300')
window.title('Random Clip Selector')

# frame
frame = ttk.Frame(window)
frame.pack()

# RCS label
app_title = ttk.Label(frame, text='Random Clip Selector')
app_title.grid(row=0, column=0)

# file location from
fromdir_frame = tk.Frame(frame, pady=10)
fromdir_frame.grid(row=0)
fromdir = tk.StringVar()
from_label = ttk.Label(fromdir_frame, text='From file location', anchor='w', width=40)
from_label.grid(row=0, column=0)
from_file_entry = ttk.Entry(fromdir_frame, textvariable=fromdir, width=40)
from_file_entry.grid(row=1, column=0)
from_file_button = ttk.Button(fromdir_frame, text='...', command=from_func)
from_file_button.grid(row=1, column=1)

# file location to
todir_frame = tk.Frame(frame, pady=10)
todir_frame.grid(row=1)
todir = tk.StringVar()
to_label = ttk.Label(todir_frame, text='Save to file location', anchor='w', width=40)
to_label.grid(row=0, column=0)
to_file_entry = ttk.Entry(todir_frame, textvariable=todir, width=40)
to_file_entry.grid(row=1, column=0)
to_file_button = ttk.Button(todir_frame, text='...', command=to_func)
to_file_button.grid(row=1, column=1)

# number of videos to shuffle
vids_frame = tk.Frame(frame, pady=10)
vids_frame.grid(row=2)
vids_label = ttk.Label(vids_frame, text='No. of vids', anchor='w', justify=tk.LEFT, width=40)
vids_label.grid(row=0, column=0)
number_of_vids = tk.IntVar()
ttk.Spinbox(vids_frame, from_=5, to=40, justify=tk.LEFT, textvariable=number_of_vids, width=20).grid(row=1, column=0)
    
def shuffle_videos():
    try:
        clip_list = []
        dir_list = os.listdir(fromdir.get())
        for file in dir_list:
            name, extension = os.path.splitext(file)
            if extension in video_format:
                clip_list.append(file)
            else:
                pass
        
        random_list = random.sample(clip_list, number_of_vids.get())

        for clip in random_list:
            clip = fromdir.get() + '/' + clip
            shutil.move(clip, todir.get())

        global success_popup
        success_popup = tk.Toplevel(window)
        success_popup.title('Success')
        success_popup.geometry('200x100')

        success_message = ttk.Label(success_popup, text=f'Successfully randomized {number_of_vids.get()} videos!')
        success_message.pack(pady=20)

        ok_popup = ttk.Button(success_popup, text='Ok', command=success_popup.destroy)
        ok_popup.pack()

    except ValueError:
        failure_popup = tk.Toplevel(window)
        failure_popup.title('Error')
        failure_popup.geometry('300x100')

        failure_message = ttk.Label(failure_popup, text='Number of requested clips exceed amount of videos')
        failure_message.pack(pady=20)

        ok_popup = ttk.Button(failure_popup, text='Ok', command=failure_popup.destroy)
        ok_popup.pack()
    

# button to exec
start = ttk.Button(frame, text='Start', command=shuffle_videos)
start.grid(row=3, column=0, pady=10)

# run
window.mainloop()