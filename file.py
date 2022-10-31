from tkinter import *
from tkinter import messagebox
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 21;

GPIO.setup(LED,GPIO.OUT)

win = Tk()
win.title("Morse Code Translator")
win.configure(background = "white")
win.geometry('350x90')

title = Label(win ,text = 'Convert to morse: ', bg = "white").grid(row=0)

value = Entry(win)
value.grid(row=0,column=1)
value.delete(0,END)

GPIO.output(LED,GPIO.LOW)

Convert = Button(text = "Convert",command = lambda: task(value.get()), height = 1, width = 13, border = 4).grid(row = 1, column = 1)

def close():
    win.destroy()
    GPIO.cleanup()

exit = Button(win, command = close, text = "EXIT", bg = "red", border = 4, cursor = "pirate")
exit.grid(row = 2, column = 1)
DATA = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
 



def dot():
    
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)

def dash():
    
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.9)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)
    
    
def task(morse_code):
    if len(morse_code) > 12:
        messagebox.showwarning("Exceeded","Max limit is 12 characters")
        win.destroy()
    
    elif len(morse_code) <= 12 and len(morse_code) >0:
  #value.delete(0,END)
      for alphabet in morse_code:
        for code in DATA[alphabet.upper()]:
            if code == '-':
               dash()
            elif code == '.':
               dot()
            else:
               time.sleep(0.5)
               time.sleep(0.5)

win.mainloop()