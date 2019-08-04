from supported_file_info import *

DEBUG = False

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
