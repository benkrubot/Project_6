# Show me that you can sort data (sorting with 10 rectangles to start will help work out the basics!): (Note: if you can get 10 to sort, then you have a majority of these points...)

I used a for loop to append to my numbers list the 100 integers using the random module. After that I used the sorted function to sort the numbers list.

![alt text](https://i.imgur.com/Eyj1GTK.png)

# Create a GUI to display the collection of int values as rectangles,

To display my collection of int values as rectangles, I used a for loop in a for loop to create a 10x10 grid that creates the rectangles using labels, and by using the pop method I am able to take the first value out of the numbers list and place that as the text on the label. This loops until all 100 rectangles are created.

![alt text](https://i.imgur.com/j4xXA23.png)

# Include a button to start the sort process,

I created a button that when pressed will call the sorting function.

![alt text](https://i.imgur.com/nwhuZrp.png)

# Highlight the candidate value(s) both before and after moving the value(s) at each step of the sorting process,

After finding the candidate, it is removed from the labels list, then added to the sorted list. Then the background of that label is turned red. Then the sorted label will have green added to it. In the for loop, the sorted label will then be removed from all labels and added to cycle labels. Then a label will be created with the value, and the background (green) and if it is green then it will be added to the sorted list, otherwise it will be recycled back into the labels list. This then repeats for the rest of the labels.

![alt text](https://i.imgur.com/GUiAmyK.png)

![alt text](https://i.imgur.com/vSOnaFo.png)

# Pause after highlighting the candidate value(s)(before and after moving, possibly with different colors), (perhaps for 100-250ms based on a speed button or slider?)

Here I just have root.after(250) pause for 250ms

# Make it obvious when it has finished sorting the data set. (perhaps things flash, a border appears around the data set, or something pops up saying it completed)

When everything is sorted, every label will be green, as well as the label on the bottom will have changed from “...” to “List sorted!”

![alt text](https://i.imgur.com/63ZeOD5.png)

# What kinds of tests would be useful for this?  How could we test some of it to verify that it was working properly?

Not sure, I’ve had a hard time understanding this part of the class, and due to the unfortunate circumstances of this year and the class as well, I haven’t been able to get the feedback I needed to learn this.

# Implement some of those tests in PyTest!

I’m still unsure how to use PyTest, as well as how to create tests for methods or functions being used in a GUI.
