import os
import re

class Extractable(object):

    # PROPERTIES
    title = None
    content = None

    # METHODS
    def __init__(self, title=None, content=None):

        self.title = title
        self.content = content

    # Read file from a .txt file stored in a folder called 'plays'
    def read_content_from_file(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file_reader:
                self.content = file_reader.read()

    def transform_content(self, dir_path, act_one, act_two, act_three, act_four, act_five):

        # make directory path for new files
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # CHANGE ACT DIVIDERS: divides large text file into segments (acts)
        # Each segment is printed to its own file for analysis
        act1 = re.search("(ACT 1(.|\n)*ACT 2)", self.content).group(1)
        f = open(act_one, 'w')
        f.write(act1)

        act2 = re.search("(ACT 2(.|\n)*ACT 3)", self.content).group(1)
        f = open(act_two, 'w')
        f.write(act2)

        act3 = re.search("(ACT 3(.|\n)*ACT 4)", self.content).group(1)
        f = open(act_three, 'w')
        f.write(act3)

        act4 = re.search("(ACT 4(.|\n)*ACT 5)", self.content).group(1)
        f = open(act_four, 'w')
        f.write(act4)

        act5 = re.search("(ACT 5(.|\n)*)", self.content).group(1)
        f = open(act_five, 'w')
        f.write(act5)

    # RUN THE PROGRAM
    def run_program(self, play_name):
        dir_path = str("plays\\" + play_name + "\\act")
        name = str("plays\\" + play_name + ".txt")
        act1_name = str("plays\\" + play_name + "\\act\\act1.txt")
        act2_name = str("plays\\" + play_name + "\\act\\act2.txt")
        act3_name = str("plays\\" + play_name + "\\act\\act3.txt")
        act4_name = str("plays\\" + play_name + "\\act\\act4.txt")
        act5_name = str("plays\\" + play_name + "\\act\\act5.txt")

        self.read_content_from_file(name)
        self.transform_content(dir_path, act1_name, act2_name, act3_name, act4_name, act5_name)
