# FileMutate

This is another attempt to hide the information a file. 

## Usage

The sources are placed inside [`sources`](sources) folder. The main script is [`fileMutate.py`](sources/fileMutate.py). 

* **To Mute**

```
py fileMutate [filename] [desired extension]
```

Arguments `[filename]` and `[desired extension]`	are optional arguments

* **To Unmute**

`py fileMutate -r [mutated file]`

Arguments `[mutated file]` is optional arguments.

## Requirements

* python version 3.6 or later
* [tkinter](https://docs.python.org/3/library/tkinter.html) installed (hope python installation comes with `tkinter` installed)

## v1: Released Aug,03'019

* Reads the file types of any kinds, but the output file types are only accepted ones. The accepted files are listed in [`names.csv`](sources/names.csv).
  * You can add the magic values in the files [`names.csv`](sources/names.csv). You can modify the existing magic values if you think there is any mistake. But **Please Run [`read_file_types.py`](sources/read_file_types.py)**. This script modifies [`supported_file_info.py`](sources/supported_file_info.py).
* This version simply adds a magic number of the newer file type in the beginning of the file. The output file is saved with the same name as the input file, but with new extension.
* The threat model is a naïve user who simply double clicks for opening the file. This solution will prevent any naïve user to know the content of file just by double clicking it or in any other straight forward way.

## v2: 

* TODO: Plan for encryption
