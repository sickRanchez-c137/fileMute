# This is a file obfuscator tool for you.
# It implements one of the most naiive method of information hiding by changing the magic number
#  .. or special keywords in a file with any random magic number picked from the list.
# This would gve the impression that the type of file is something else, while it is not
import os
import sys

# our other module, imoprt everything
from ext_crypt import *

try:
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    from Tkinter import filedialog
except:
    print(f"E: Import Error: Module \"tkinter\" not found")
    sys.exit(-1)

if __name__=="__main__":
    # name some variables
    file_name = ""
    dest_file_type = ""

    # read command line arguments
    if len(sys.argv)>1:
        file_name = sys.argv[1]
        # check for file availability, exit if not available
        if not os.path.isfile(file_name):
            print(f"E: file {file_name} not found")
            sys.exit(-1)

    # read if the user wants to specify the destination extension of file
    elif len(sys.argv)>2:
        dest_file_type = sys.argv[2]

    # if no argument provided, pop-up a dialog box
    elif len(sys.argv)==1:
        my_app = tk.Tk()
        my_app.withdraw()
        file_name = filedialog.askopenfilename()

    ext_crypt = EXT_CRYPT(file_name.lower(),dest_file_type.lower())
    ext_crypt.operate()
