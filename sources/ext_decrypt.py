import os
import io
import sys
import random

from check_and_predict import *

class EXT_DECRYPT:
    def __init__(self,file_name):
        self.enc_file = file_name

        if not os.path.exists(self.enc_file):
            if DEBUG:
                print(f"E: File {self.enc_file} not found")
            tk.messagebox.showerror("ERROR!!","File Not Found !!")
            sys.exit(-1)

        self.magic_file_dict = initialize_dict()
        self.supported_file_types = list(self.magic_file_dict.keys())

    def predict_extension(self,first_50_bytes,matched_bytes):
        out_filename_ext = predict_extension(self.magic_file_dict,first_50_bytes,len(matched_bytes))
        if out_filename_ext == "NOT FOUND":
            if DEBUG:
                print(f"E: File extension could not be determined")
            tk.messagebox.showerror("ERROR!!","Extension Could Not Be Determined")
            sys.exit(-1)

        if DEBUG:
            print(f"I: predicted extension is {out_filename_ext}")

        return out_filename_ext

    def revert(self, file_to_revert):
        # this function reverses the operation and save a file named
        # .. {self.input_file}+"rec"+{self.i_type}

        # open the output file
        in_here = open(file_to_revert,"rb")
        extsn_here = file_to_revert.split(".")[-1]
        possible_magic_list = self.magic_file_dict[extsn_here][0]
        
        first_50_bytes = in_here.read(50)
        check_modified,matched_bytes = check_bytes(first_50_bytes,possible_magic_list)

        if not check_modified:            
            if DEBUG:
                print(f"E: .. file might be already modified, will add capability later")
            messagebox.showerror("ERROR !!","File modified!! Cannot operate")
            sys.exit(-1)
        else:
            if DEBUG:
                print(f"I: .. file extension confirms, matched bytes is {matched_bytes}, len={len(matched_bytes)}")

        in_here.seek(0,0)
        # just ignore the first matched_bytes from the file
        in_here.read(len(matched_bytes))

        # this might be tricky to find the extension about the file to be written
        out_filename_ext = self.predict_extension(first_50_bytes,matched_bytes)

        out_file_name = "".join(file_to_revert.split(".")[:-1:])+"_recovered."+out_filename_ext
        # out_file_name = "".join(file_to_revert.split(".")[:-2:])+"_rec."+out_filename_ext
        out_here = open(out_file_name,"wb")

        if DEBUG:
            print(f"I: Writing to the output file {out_file_name}")

        while out_here.write(in_here.read(4096*4096)):
            pass

        out_here.close()
        in_here.close()

        tk.messagebox.showinfo("Info!!","Reverting File Finished")
        return out_file_name

    def operate(self):
        return self.revert(self.enc_file)
