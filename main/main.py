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

#Delete rows that are used in story graph, but not used in goodreads:
for row in story_graph_list:
    story_graph_list[row].pop('Read Count', None)
    story_graph_list[row].pop('Moods', None)
    story_graph_list[row].pop('Pace', None)
    story_graph_list[row].pop('Character- or Plot-Driven?', None)
    story_graph_list[row].pop('Loveable Characters?', None)
    story_graph_list[row].pop('Diverse Characters?', None)
    story_graph_list[row].pop('Flawed Characters?', None)
    story_graph_list[row].pop('Star Rating', None)
    story_graph_list[row].pop('Content Warnings', None)
    story_graph_list[row].pop('Content Warning Description', None)
    story_graph_list[row].pop('Owned?', None)
    print(story_graph_list[row])
