Alliteration Tracker
-----------------------

Created by: Eryn Lyle, 07/12/17
Tested with files from Folger Digital Texts
Python 3.6

The Alliteration Tracker/Counter allows users to collect large datasets about the use of alliteration in texts,
specifically plays. It was created to analyze the open-access Folger Digital Texts editions of The Complete Works of
William Shakespeare, but can be adapted to any line-division based text (drama, poetry, etc) provided to user
changes the regexes to fit their needs.

Adding Play Files
-----------------
Add play files into a folder called 'plays'
The extractor will divide them into acts.
Depending on the source/formatting of the specific play
you may need to change the regular expressions to accurately capture
act divisions [This is done in the extractor.py file]

Analyzing Plays
----------------
Change regexs in alliteration.py to match play's specific features
Current regexs are for analysis of a Folger Digital Text .txt file
Results contain both alliteration counts and what specific letters are repeated
They are divided into acts and contained within the 'results' folder of each play

Alliteration Number
-------------------
alliteration_number equals the number of times a letter needs to be repeated for it to be 'alliteration'
    Ex: 'We will run' would be classified as alliteration if alliteration_number = 1
    But NOT if alliteration_number = 2
    alliteration_number = 1: "We Will run into the Woods" is TRUE [repeated 1+ times]
    alliteration_number = 2: "We Will run into the Woods" is TRUE [repeated 2+ times]
    alliteration_number = 3: "We Will run into the Woods" is FALSE [NOT repeated 3+ times]

Result Outputs
---------------
In each act's result file is every letter that is alliterated, per line. Some lines have
multiple letters that repeat
    Ex. We wish we wish upon a shooting star would return {w, s}, assuming alliteration_number = 1
At the bottom, the total counter number of lines with alliteration are displayed

Turning on/off stopwords
------------------------
Turning stopwords on means common words like "and", "if", "can", "he", etc. will be removed.
If you wish to turn stopwords on/off, in alliteration.py
set the variable 'stpwds' to True/False in def loop_through_lines
The default setting is stopwords off. Common words will NOT be removed.
