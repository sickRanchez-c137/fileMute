# The class defined here is imported by the main file.
import os
import io
import sys
import random

try:
    import tkinter as tk
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    from Tkinter import *
    from Tkinter import messagebox
except:
    print(f"E: Import Error: Module \"tkinter\" not found")
    sys.exit(-1)

from check_and_predict import *

class EXT_CRYPT:
    def __init__(self,file_name="",dest_file_type=""):

        if file_name=="":
            print(f"E: Should never reach here, yet here you are ...")
            sys.exit(-1)

        self.input_file = file_name
        self.i_type = file_name.split(".")[-1].lower()
        self.magic_file_dict = initialize_dict()

        self.supported_file_types = list(self.magic_file_dict.keys())
        
        self.supported_in_type = False
        if self.i_type in self.supported_file_types:
            self.supported_in_type = True

        if dest_file_type in self.supported_file_types:
            self.d_type = dest_file_type
        else:
            if DEBUG:
                print(f"I: selecting random destination file type")
            self.d_type = self.get_random_ext()

        self.destination_magic = self.get_magic(self.d_type)

        self.output_file = "".join(file_name.split(".")[:-1:])+"."+self.d_type

        self.print_info()


    def get_magic(self,format_file):
        # return binary object that can directly be written to file
        return random.choice(self.magic_file_dict[format_file][0])

    def get_random_ext(self):
        ret_val = self.supported_file_types[random.randrange(len(self.supported_file_types))]
        if self.i_type == ret_val:
            return self.get_random_ext()
        return ret_val

    def print_info(self):
        if DEBUG:
            print(f"I: Input file supplied is {self.input_file}","\t")
        if os.path.exists(self.input_file):
            if DEBUG:
                print(f"file found")
        else:
            print(f"E: File not found")
        if DEBUG:
            print(f"I: Input file type is {self.i_type}")
            print(f"I: Desired output file type is {self.d_type}")

    def open_file(self):
        # no checking for file avail
        # .. should have already been done

        # open file to read in binary mode and read the first 50 bytes
        self.f_handle = open(self.input_file,"rb")
        # read the first 50 bytes from the file and convert to big-endian number
        try:
            self.orig_read_bytes = self.f_handle.read(50)
            self.orig_read_string = self.orig_read_bytes.decode("latin-1")
            if DEBUG:
                print(f"I:read from file {self.orig_read_bytes}\n\t {self.orig_read_string}")
        except Exception as e:
            # the file might not have 50 bytes
            print(f"E: File reading error. \n\t.. {e}")
            sys.exit(-1)

    def verify(self):
        
        expected_bytes_list = self.magic_file_dict[self.i_type][0]
        for each_expect in expected_bytes_list:
            
            # we need length because we need to compare with exact length from the file
            len_exp = len(each_expect)
            if DEBUG:
                print(f"I: Inside verify: comparing exp: {each_expect} with orig: {self.orig_read_bytes[:len_exp:]}")
            if self.orig_read_bytes[:len_exp:] == each_expect:
                return True
        return False

    def write_output_file(self):
        # it turns out you have to write the whole file completely

        # this technique needs to be thought again, but the current approach
        # .. to add the destination magic bytes in the beginning of file

        # go to the absolute beginning of file
        self.f_handle.seek(0,0)
        self.out_f_handle = open(self.output_file,'wb')
        if DEBUG:
            print(f"I: writing destination magic: \n\t {self.destination_magic}")
        self.out_f_handle.write(self.destination_magic)

        # this section copies from the source file to destination file
        while self.out_f_handle.write(self.f_handle.read(4096*4096)):
            pass

        self.f_handle.close()
        self.out_f_handle.close()

        tk.messagebox.showinfo("Complete!!!","New File Write Complete")

    def operate(self):
        if DEBUG:
            print(f"I am operating")

        # This section reads the first some bytes and tries to verify the type of file based on info provided
        self.open_file()
        
        # input type is supported but input type does not match
        if self.supported_in_type:
            if not self.verify():
                print(f"I: Input file is probably already obscured.\n\t.. Magic number from file type does not correspond to expected values")
            else:
                if DEBUG:
                    print(f"I: Magic number from file type corresponds to expected values")
        else:
            print(f"I: provided input file type is currently not supported for verification\n\t.. can still continue")

        
        self.write_output_file()

        if DEBUG:
            print(f"I: The output file name is {self.output_file}")
        return self.output_file

