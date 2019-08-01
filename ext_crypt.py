# The class defined here is imported by the main file.
import os
import random
from supported_file_info import *

class EXT_CRYPT:
    def __init__(self,file_name="",dest_file_type=""):
        self.input_file = file_name
        self.i_type = file_name.split(".")[-1]
        self.magic_file_dict = initialize_dict()

        self.supported_file_types = list(self.magic_file_dict.keys())

        if dest_file_type=="":
            self.d_type = self.get_random_ext()
        else:
            self.d_type = dest_file_type

        self.print_info()

    def get_random_ext(self):
        ret_val = self.supported_file_types[random.randrange(len(self.supported_file_types))]
        if self.i_type == ret_val:
            return self.get_random_ext()
        return ret_val

    def print_info(self):
        print(f"I: Input file supplied is {self.input_file}","\t")
        if os.path.exists(self.input_file):
            print(f"file found")
        else:
            print(f"file not found")
        print(f"I: Input file type is {self.i_type}")
        print(f"I: Desired output file type is {self.d_type}")

    def operate(self):
        print(f"I am operating")
        # TODO:
        # read the file and simple change the inputs magic with outputs magic
