from extractor import Extractable
from nltk.corpus import stopwords
import os
import re


class Text(object):

    # PROPERTIES
    title = None
    alliteration_number = None
    content = None
    alli_counter = None
    alliteration = None

    # METHODS
    def __init__(self, alliteration_number=None, content=None, alli_counter=None, alliteration=None):

        self.alliteration_number = alliteration_number
        self.content = content
        self.alli_counter = alli_counter
        self.alliteration = alliteration

    # Read play's act files
    def read_content_from_file(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file_reader:
                self.content = file_reader.read()

    # refine files
    def regular_expressions(self, change_text_file):
        print("Beginning REs")

        # deletes stage directions
        self.content = re.sub(r'\[(.|\n)*?\]', " ", self.content)

        # deletes character names
        self.content = re.sub(r'\b[A-Z0-9]{2,}\b *,?', "", self.content)

        # deletes random - signs to prevent miscounts
        self.content = re.sub(r'-*', "", self.content)

        # deletes quotation marks to prevent miscounts
        self.content = re.sub(r'"', " ", self.content)

        with open(change_text_file, 'w') as out:
            out.write(self.content)

    def loop_through_lines(self, change_text_file, results_file, results_dir_path, title, act_number):

        # create directory path for results and writes play title and act number to file
        if not os.path.exists(results_dir_path):
            os.makedirs(results_dir_path)
        with open(results_file, 'a') as out:
            out.write("Play: " + title + "\n")
            out.write("  Act Number: " + str(act_number) + "\n")

        # alliteration_number: how many times a letter is repeated for it to be 'alliteration'
            # Ex: 'We would run' would be classified as alliteration if alliteration_number = 1
            # But would NOT be if alliteration_number = 2
        self.alliteration_number = 1
        self.alli_counter = 0

        # ANALYSIS OF ALLITERATION
        with open(change_text_file, 'r') as fh:
            # Refine lines & count/record alliteration in each one
            for line in fh:
                letter = []
                text = line.lower()
                splited = text.split()

                # CHANGE STOPWORDS: 'filtered_words' is now the line content. Deletes stopwords if True.
                stpwds = False
                if stpwds:
                    filtered_words = [word for word in splited if word not in stopwords.words('english')]
                else:
                    filtered_words = splited

                # Create a list of first letter in a line's words
                for word in filtered_words:
                    letter.append(word[0])

                # Check if letter is repeated. If so, add to a set called 'self.alliteration'
                # and make the alliteration counter go up by one.
                if len(letter) != len(set(letter)):
                    self.alli_counter += 1
                    self.alliteration = set([x for x in letter if letter.count(x) > self.alliteration_number])

                    # Appends line's alliteration letters to a results file
                    with open(results_file, 'a') as out:
                        out.write(", ".join(self.alliteration) + "\n")

            # Print counter results to file
            with open(results_file, 'a') as out:
                out.write("  Number of Alliterations: " + str(self.alli_counter) + "\n\n")

        # Remove WIP file
        if os.path.exists(change_text_file):
            os.remove(change_text_file)


class Play(Text):

    # Divide plays into acts (to speed up program)
    # see extractor.py
    def extract(self, play_name):
        a = Extractable()
        a.run_program(play_name)

    # RUN THE FILE Pt. 1
    def run(self, play_name, act_number):
        name = str("plays\\" + play_name + "\\act\\" + "act" + act_number + ".txt")
        results = str("plays\\" + play_name + "\\results\\" + "act" + act_number + "_results.txt")
        results_dir_path = str("plays\\" + play_name + "\\" + "results")
        change = str("plays\\" + play_name + "\\" + "change_text_file.txt")
        print("Starting Act %s for %s" % (act_number, play_name))
        self.read_content_from_file(name)
        self.regular_expressions(change)
        self.loop_through_lines(change, results, results_dir_path, play_name, act_number)

    # RUN THE FILE Pt 2
    def run_program(self, play_name):
        self.extract(play_name)
        self.run(play_name, "1")
        self.run(play_name, "2")
        self.run(play_name, "3")
        self.run(play_name, "4")
        self.run(play_name, "5")
        # Add more acts/sections as needed. MAKE SURE TO EDIT extractor.py FILE BEFORE DOING SO.
