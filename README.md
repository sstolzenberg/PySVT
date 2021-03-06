# PySVT
a Smarter Vocabulary Trainer for Python

# Licence

Copyright (c) 2020 Sebastian Stolzenberg
for any feedback or questions, please contact the author:

Sebastian Stolzenberg <ss629@cornell.edu>

This software has been thoroughly tested, but comes with no warranty.
It is freely available under the L-GPL license.

# Introduction

PySVT - a Smarter Vocabulary Trainer for Python:
This Vocabulary Trainer uses a vocabulary list (in .xlsx format)

and an internal register system

(as in https://upload.wikimedia.org/wikipedia/commons/7/7a/Leitner_system_de.png)

to efficiently learn vocabularies that are difficult to remember.

The flexible command-line interface allows to focus the study

on different parts of a vocabulary:

E.g., a Mandarin vocabulary consists of
- the Chinese character,
- its pronunciation in the Pinyin language, and
- its actual meaning
Memorizing all three parts of many vocabularies at once may be less efficient
because inter-vocabulary similarities may be difficult to grasp

I have personally started to learn Mandarine by just learning the Pinyin
pronunciation first, and later the "Pinyin<->English" meaning.
In the final step, I will also memorize the Chinese characters
in connection to their Pinyin pronunciation and their English meaning.

# Content
- README.md   - this documentation file
- PySVT.py    - Python script for Python 3
- input       - optional input folder containing an exemplary vocabulary list (.xlsx)

To learn Chinese Mandarine, I recommend searching the internet for "HSK Excel", which will lead you to complete Excel vocabulary lists

# Installation Instructions for Windows 10
Install https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

Open "Start"->"Programs"->"Anaconda3 (64-Bit)

```conda install pandas numpy xlrd openpyxl```

press "y" and "Enter"
exit

Whenever you want to start the PySVT:
Open "Start"->"Programs"->"Anaconda3 (64-Bit)

```cd C:\Users/.../Downloads\PySVT```

(whereever you "git clone-ed the PySVT repository)

```python PySVT.py --infilename input/simple_vocab_list --col2show "English" --col2ask "Pinyin" --register 0 --is_first_run 1```

i.e.:
the Python program execute a python script named PySVT.py with some command line options
for an explanation of the Vocabulary Trainer, type in

```python PySVT.py --help```

# Installation Instructions for MacOS (or similarly, Linux)
Install https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg
for example into ~/miniconda3

GoTo "Applications"->"Utilities"
and place the "Terminal" app onto your app board (bottom of the screen, e.g. next to "Finder")
execute "Terminal" type in

```cd ~/miniconda3
conda init
exit
```

restart the "Terminal" App again

```conda install pandas numpy xlrd openpyxl```

press "y" and "Enter"
exit

Whenever you want to start the PySVT:
Open "Start"->"Programs"->"Anaconda3 (64-Bit)

```cd ~/Downloads\PySVT ```

(whereever you "git clone-ed the PySVT repository)


Open "Start"->"Programs"->"Anaconda3 (64-Bit)

```cd ~/Downloads\PySVT ```


```cd ~/Downloads\PySVT (whereever you extracted PySVT.zip)```

```python PySVT.py --infilename input/simple_vocab_list --col2show "English" --col2ask "Chinese" --register 0 --is_first_run 1```

i.e.:
the Python program execute a python script named PySVT.py with some command line options
for an explanation of the Vocabulary Trainer, type in

```python PySVT.py --help```
