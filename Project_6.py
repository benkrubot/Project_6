# This program will sort the random integers created by finding the lowest value corresponding to the label using cget,
# then using a loop that will recreate the label with the lowest value sorting into ascending order. The loop in organize
# is probably inefficient as it will only create 1 green label (indicating sorted) with the sorted lowest value, and then
# it will iterate through the rest of the loop so that each number is cycled back into the labels list. After that is done
# then sorting will find the lowest value again, and this whole process will repeat until there are none left. So I think
# this is iterating a lot of times. Would love to see how a more efficient program works. Also got a boatload of information
# helping with this and the previous project thanks to stackoverflow.

from tkinter import *
import random

root = Tk()
root.title("Sorting")
root.geometry("600x600")
sorted_list = []
labels_list = []

def create_labels():
    # This will create a list of 100 random integers, then randomly put those integers
    # onto the 10x10 labels created. Then it will append those labels to the labels list
    global sorted_list
    global labels_list
    # Updating status if reset pressed
    sort_lab.configure(text="...")
    # This is for when reset and sort is pressed so that it starts from scratch
    # and doesn't automatically highlight everything green
    for x in sorted_list:
        x.destroy()
    for x in labels_list:
        x.destroy()
    sorted_list = []
    labels_list = []

    # Creating 100 random integers 1-100 into vals
    vals = []
    for x in range(100):
        vals.append(random.randint(1, 100))

    # Placing vals randomly onto the labels and creating labels
    for i in range(10):
        for j in range(10):
            z = Label(root, text=vals.pop(0), background="white", height=2, width=4, font=("Roboto", 12))
            z.place(x=50 + (50 * j), y=50 + (i * 50))
            labels_list.append(z)


def sorting():
    # This will find the lowest value, indicated by highlighting red
    global sorted_list
    global labels_list

    # Disabling the buttons
    sort_but.configure(state=DISABLED)
    reset_but.configure(state=DISABLED)

    while labels_list:
        # Finding the lowest value using cget and storing into low label
        low_label = None
        for x in labels_list:
            if low_label:
                if x.cget("text") < low_label.cget("text"):
                    low_label = x
            else:
                low_label = x

        # Removing the lowest value from label list, adding to sorted list, highlighting label red
        labels_list.remove(low_label)
        sorted_list.append(low_label)
        low_label.configure(background="red")

        # Update the window, and pause for 250ms
        root.update()
        root.after(250)
        organize()

    # Updating label and enabling buttons
    sort_but.configure(state=NORMAL)
    sort_lab.configure(text="List sorted!")
    reset_but.configure(state=NORMAL)


def organize():
    # This will be called by sort after finding lowest value, will then organize by lowest value
    global sorted_list
    global labels_list
    # print("this is currently sorted: ", sorted_list) #test
    # Getting the values of the labels
    all_labels = list(map(lambda l: ("green", l.cget("text")), sorted_list)) + list(
        map(lambda l: ("white", l.cget("text")), labels_list))
    # This speeds up the process
    for x in sorted_list:
        x.destroy()
    for x in labels_list:
        x.destroy()
    sorted_list = []
    labels_list = []

    # Reorganizing lowest value
    for i in range(10):
        for j in range(10):
            # Removing lowest val into old_labels, then recycle the others
            old_labels = all_labels.pop(0)
            #print(old_labels[1])  # testing
            # Placing lowest val onto label
            z = Label(root, text=old_labels[1], background=old_labels[0], height=2, width=4, font=("Roboto", 12))
            z.place(x=50 + (50 * j), y=50 + (i * 50))
            # If it is green, it will be placed in sorted list, otherwise recycled back in labels_list
            if old_labels[0] == "green":
                sorted_list.append(z)
            else:
                labels_list.append(z)


# Creating buttons
sort_but = Button(root, text="Sort", command=sorting)
sort_but.place(x=50, y=550)
sort_lab = Label(root, text="...", font=("Roboto", 12))
sort_lab.place(x=130, y=550)
reset_but = Button(root, text="Reset", command=create_labels)
reset_but.place(x=85, y=550)

create_labels()
root.mainloop()