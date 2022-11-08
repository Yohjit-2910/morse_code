# Documentation
# Name : Yohjit Chopra
# Roll No. 2110994798

from tkinter import *           #importing all the important libraries
from tkinter import messagebox
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)          # setting up the set mode of the program
GPIO.setwarnings(False)         # for testing purposes I did turn of the warnings

LED = 21;                       # initialising the LED pin

GPIO.setup(LED,GPIO.OUT)        # setup of the led

win = Tk()                      # making a window through tkinter 
win.title("Morse Code Translator")  # Title of the window
win.configure(background = "white") # backgroud of the window
win.geometry('350x90')              # shape and size of the window

title = Label(win ,text = 'Convert to morse: ', bg = "white").grid(row=0)   # title of the program (but inside the GUI)

value = Entry(win)              # getting the input of the user
value.grid(row=0,column=1)      # setting the location of the input grid
value.delete(0,END)

GPIO.output(LED,GPIO.LOW)       # setting the LED to low (off)

Convert = Button(text = "Convert",command = lambda: task(value.get()), height = 1, width = 13, border = 4).grid(row = 1, column = 1)
                                # making a button to submit the letters which are to be translated into the morse
def close():
    win.destroy()               # making a fucntion to close the program
    GPIO.cleanup()

exit = Button(win, command = close, text = "EXIT", bg = "red", border = 4, cursor = "pirate")   # close button
exit.grid(row = 2, column = 1)  # location of the exit button
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
        '2': '..---',               # entire areay consisting of all the alphabeths and the conversion of those alphabets in terms of dots and dashes
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
    time.sleep(0.2)                     # a dot fucntion that will turn the LED on for 0.2 seconds and turn off for 0.2 seconds
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)

def dash():
    
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.9)                      # a dash fucntion that will turn the LED on for 0.9 seconds and turn off for 0.2 seconds
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)
    
    
def task(morse_code):
    if len(morse_code) > 12:        # a fucntion task (as per task sheet) if the characters entered are more than 12 units then a warning should be 
                                       # showed to the user
        messagebox.showwarning("Exceeded","Max limit is 12 characters") #this is a fuction of tkinter whihc whill show a warning in an another GUI 
        win.destroy()                                                       # window.
    
    elif len(morse_code) <= 12 and len(morse_code) >0:
  #value.delete(0,END)
      for alphabet in morse_code:
        for code in DATA[alphabet.upper()]:
            if code == '-':                 # converting - as dash and . as dot 
               dash()
            elif code == '.':
               dot()
            else:
               time.sleep(0.5)
               time.sleep(0.5)

win.mainloop()                      # loop continues to infinity
