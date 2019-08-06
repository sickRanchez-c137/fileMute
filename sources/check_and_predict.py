from supported_file_info import *

DEBUG = False

try:
    import tkinter as tk
    from tkinter import *
    from tkinter import messagebox
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    from Tkinter import *
    from Tkinter import filedialog
except:
    print(f"E: Import Error: Module \"tkinter\" not found")
    sys.exit(-1)

def get_gui_filename(string_to_title):
    my_app = tk.Tk()
    my_app.withdraw()
    return filedialog.askopenfilename(title=string_to_title)

def print_help_message():
    print(f"********************File Mutate********************")
    print(f"Usage: python fileMutate.py -[flag][arguments]")
    print(f"\tflags\t\targuments\t:Task")
    print(f"\t-----\t\t---------\t:-----")
    print(f"\tm\t\t[file name]\t:Mute the File [file name]")
    print(f"\td\t\t[destn ext]\t: Muted File will have extension specified")
    print(f"\tr\t\t[file name]\t:unMute the File [file name]")
    print(f"\th\t\t\t:Print Help Message")
    print(f"\n\n\t\t Credits: Sick Ranchez c-137")
    return

def get_option_val(string_to_search):    
    space_pos = string_to_search.find(' ')
    if space_pos==-1:
        return string_to_search
    return string_to_search[:space_pos]

def check_bytes(first_seq,second_seq_list):
    ret_val = (False,second_seq_list[0])
    for second_seq in second_seq_list:
        first_seq_req = first_seq[:len(second_seq)]
        if first_seq_req==second_seq:
            if DEBUG:
                print(f"I: Found bytes while checking\n\t.. seems not modified")
            ret_val = (True,second_seq)
        else:
            continue
    return ret_val

def predict_extension(magic_file_dict,first_50_bytes,len_matched_byte):

    for each_file_type in magic_file_dict.keys():
        for each_magic_byte in magic_file_dict[each_file_type][0]:
            from_50_bytes = first_50_bytes[len_matched_byte:len_matched_byte+len(each_magic_byte)]
            if DEBUG:
                print(f"I: .. comparing {from_50_bytes} with {each_magic_byte} of .{each_file_type} type")
            if from_50_bytes==each_magic_byte:                
                return each_file_type
    return "NOT FOUND"
