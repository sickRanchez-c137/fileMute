# This is a file obfuscator tool for you.
# It implements one of the most naiive method of information hiding by changing the magic number
#  .. or special keywords in a file with any random magic number picked from the list.
# This would gve the impression that the type of file is something else, while it is not
import os
import sys

# our other module, imoprt everything
from ext_crypt import *
from ext_decrypt import *

def main():
    # name some variables
    file_name = ""
    dest_file_type = ""
    output_file_name = ""

    # will be false for revert operation
    mute = True

    # read command line arguments
    if len(sys.argv)>1:
        long_argv = " ".join(sys.argv[1:])
        if DEBUG:
            print(f"I: .. the long argument is \"{long_argv}\"")

        list_of_dashes = [pos for pos, char in enumerate(long_argv) if char == '-']

        if DEBUG:
            print(f"I: .. \'-\' found at positions {list_of_dashes}")

        for each_option in list_of_dashes:
            letter_option = ''
            option_value = ""
            try:
                letter_option = long_argv[each_option+1]
                to_search = long_argv[each_option+3:]
                option_value = get_option_val(to_search)
            except:
                print(f"E: .. Illegal Use of \'-\'")
                sys.exit(-1)

            if letter_option == 'r' or  letter_option == 'R':
                # this is revert section
                file_name = option_value
                if not os.path.isfile(file_name):
                    print(f"E: .. file {file_name} not found")
                    file_name = get_gui_filename("Select File to Revert")
                mute = False

            elif letter_option == 'h' or  letter_option == 'H':
                print_help_message()
                return

            elif letter_option == 'm' or  letter_option == 'M':
                file_name = option_value
                if not os.path.isfile(file_name):
                    print(f"E: .. file {file_name} not found")
                    file_name = get_gui_filename("Select File to Mute")
                mute = True

            elif letter_option == 'd' or  letter_option == 'D':
                dest_file_type = option_value
                if file_name=="":
                    file_name = get_gui_filename("Select File to Mute")
                    mute = True

            else:
                print(f"E: Illegal options specified")
                print_help_message()
                return

    # if no argument provided, pop-up a dialog box
    elif len(sys.argv)==1:
        file_name = get_gui_filename("Select File to Mute")

    if mute:
        ext_crypt = EXT_CRYPT(file_name,dest_file_type.lower())
        output_file_name = ext_crypt.operate()
    else:
        ext_dec = EXT_DECRYPT(file_name)
        output_file_name = ext_dec.operate()

    if DEBUG:
        print(f"I: Writing output file {output_file_name} finished")

if __name__=="__main__":
    main()
