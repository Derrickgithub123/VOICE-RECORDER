from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import os

def Record():
    freq=44100
    dur=int(duration.get())
    recording=sound.rec(dur*freq,
    samplerate=freq,channels=1)

    try:
      dur = int(duration.get())
      recording = sound.rec(dur * freq, samplerate=freq, channels=1)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for duration.")
        return

    temp = dur

    while temp>0:
        Label(text=f"{str(temp)}",font="arial 40",width=4,background="white").place(x=300,y=500)
        root.update()
        time.sleep(1)
        temp-=1

    messagebox.showinfo("Time's up", "Recording completed.")

    sound.wait()

    write("recording.wav",freq,recording)
    messagebox.showinfo("Save Status", f"Recording saved at: {os.path.abspath('recording.wav')}")

root=Tk()
root.geometry("700x700+400+80")
root.resizable(True,True)
root.title("Kanyoko's Voice Recorder")
root.configure(background="black")

#icon
try:
 image_icon=PhotoImage(file="recorder.png")
 root.iconphoto(False,image_icon)
except Exception:
    print("icon file not found. Ensure 'recorder.png' is in the directory.")

#logo
try:
 photo=PhotoImage(file="recorder.png")
 myimage=Label(image=photo,background="white")
 myimage.pack(padx=5,pady=5)
except Exception:
    print("Logo file not found. Ensure 'recorder.png' is in the directory.")
    
#name
Label(text="Kanyoko's Voice Recorder",font="arial 30 bold",background="red",fg="green").pack()

#entry box
duration=StringVar()
entry=Entry(root,textvariable=duration,font="arial 15",width=10).pack(padx=10,pady=10)
Label(text="Enter time in seconds",font="arial 15",background="black",fg="white").pack()

#button
record=Button(root,font="arial 20",text="Record",bg="red",fg="white", border=0,command=Record) .pack(pady=30)

root.mainloop()

