# E Jolly 
# April 2024
# Main file for running storygraph to goodreads program. Run commandline

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import csv
from helpers import rename

#default fields that goodreads uses. 
goodread_fields = ['Title', 'Author', 'ISBN', 'My Rating', 'Publisher', 'Binding', 'Year Published', 'Original Publication Year', 'Date Read', 'Date Added', 'Shelves', 'Bookshelves', 'My Review']

Tk().withdraw()
filename = askopenfilename(filetypes=[("CSV files", ".csv")])

story_graph_list = []

with open(filename, encoding="utf8", newline='') as csvfile:
    bookreader = csv.DictReader(csvfile)

    # for row in bookreader:
    #     story_graph_list.append(row)
    story_graph_list = list(bookreader)

#Delete rows that are used in story graph, but not used in goodreads:
for row in range(len(story_graph_list)):
    story_graph_list[row].pop('Read Count')
    story_graph_list[row].pop('Moods')
    story_graph_list[row].pop('Pace')
    story_graph_list[row].pop('Character- or Plot-Driven?')
    story_graph_list[row].pop('Loveable Characters?')
    story_graph_list[row].pop('Diverse Characters?')
    story_graph_list[row].pop('Flawed Characters?')
    story_graph_list[row].pop('Star Rating')
    story_graph_list[row].pop('Content Warnings')
    story_graph_list[row].pop('Strong Character Development?')
    story_graph_list[row].pop('Content Warning Description')

    rename(story_graph_list[row], 'Author', 'Authors')
    rename(story_graph_list[row], 'Additional Authors', 'Contributors')   
    rename(story_graph_list[row], 'ISBN', 'ISBN/UID')
    rename(story_graph_list[row], 'Date Read', 'Dates Read')
    rename(story_graph_list[row], 'Average Rating', 'Star Rating')
    rename(story_graph_list[row], 'Exclusive Shelf', 'Read Status')
    rename(story_graph_list[row], 'Bookshelves', 'Tags')
    rename(story_graph_list[row], 'My Review', 'Review')
    rename(story_graph_list[row], 'Owned Copies', 'Owned?')

#This print is for testing purposes and will be replaced with saving to CSV
print(story_graph_list)