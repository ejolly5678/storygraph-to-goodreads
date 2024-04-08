# E Jolly 
# April 2024
# Main file for running storygraph to goodreads program. Run commandline

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import csv

Tk().withdraw()
filename = askopenfilename(filetypes=[("CSV files", ".csv")])

Title = []
Authors = []
Contributors = []
ISBN = []
Read_Status = []
Last_Date_Read = []
Read_Count = []
Moods = []
Pace = []
Characters = []
##need to remove some of these as they don't match up with goodreads. 

##Need a way to get goodreads book IDs into here. 

with open(filename, newline='') as csvfile:
    bookreader = csv.reader(csvfile, delimiter=',')
    linecount = 0
    for row in bookreader:
        print(', '.join(row))