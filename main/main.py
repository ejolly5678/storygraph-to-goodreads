# E Jolly 
# April 2024
# Main file for running storygraph to goodreads program. Run commandline

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import csv

#default fields that goodreads uses. 
goodread_fields = ['Title', 'Author', 'ISBN', 'My Rating', 'Publisher', 'Binding', 'Year Published', 'Original Publication Year', 'Date Read', 'Date Added', 'Shelves', 'Bookshelves', 'My Review']

Tk().withdraw()
filename = askopenfilename(filetypes=[("CSV files", ".csv")])

story_graph_list = []

with open(filename, encoding="utf8", newline='') as csvfile:
    bookreader = csv.reader(csvfile, delimiter=',')
    linecount = 0
    for row in bookreader:
        story_graph_list.append(row)

