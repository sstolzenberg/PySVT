#!/usr/bin/python

# PySVT - a Smarter Vocabulary Trainer for Python
#
# Copyright (c) 2020 Sebastian Stolzenberg
# for any feedback or questions, please contact the author:
# Sebastian Stolzenberg <ss629@cornell.edu>
#
# This software has been thoroughly tested, but comes with no warranty.
# It is freely available under the L-GPL license.
#
# For help, type in
# python Vocab_Trainer.py --help

import pandas as pd
import numpy as np
np.random.seed()
import os, sys

import argparse
parser = argparse.ArgumentParser(description="Vocabulary Trainer using registers:\n\
- First prepare your vocabulary list into an xlsx sheet (just like in the example)\n\
- For the first run (--is_first_run 1), the registers of all vocabularies are set to 1\n\
- For every run after that, you have to have saved your changes\n\
"+"  "+"(with \"x\" into a \"*.restart.xlsx\" file)\n\
"+"  "+"which it then reloads\n\
- For every practice session you first pick a register (e.g. --register 1)\n\
- Every time you correctly answer a vocabulary during practice,\n\
"+"  "+"the register of this vocabulary is increased by one,\n\
"+"  "+"but if you answer its incorrectly, the vocabulary's register is set to 0\n\
- With this register system, you can practice the vocabularies more often, which you tend to forget\n\
- Every 10th vocabulary, the program automatically saves an emergency bakup into bakup.xlsx", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-i','--infilename',               help='Input Vocabulary Excel Sheet (xlsx)', required=True)
parser.add_argument('-s','--col2show',                 help='What Vocabulary Column to show, if \"all\" then show all columns (default: \"all\"', default=None)
parser.add_argument('-a','--col2ask',                  help='What Vocabulary Column to ask (practice)',  default=None)
parser.add_argument('-r','--register',     type = int, help='Register Index to Practice in', default=0)
parser.add_argument('-f','--is_first_run', type = int, help='First Time Running the Vocab List? (Place all vocabulary words into register 0)', default=1)
args = parser.parse_args()
 
#import matplotlib
#import matplotlib.pyplot as plt

def practice(infilename, col2show = None, col2ask = None, register = 0, is_first_run = True, ):
    if (col2show is None) or (col2ask is None):
        col2show = "all"
        print("Showing all entries")
    if is_first_run:
        df_hsk = pd.read_excel(infilename + ".xlsx")
        df_hsk["register"] = 1
    else:
        df_hsk = pd.read_excel(infilename + ".restart.xlsx")
        if "register" not in df_hsk:
            raise ValueError("register tab not found! Try setting is_first_run = True!")
    if col2show != "all":
        if (col2show not in df_hsk.columns):
            raise ValueError("col2show = \"%s\" not vocabulary!" % col2show)
        if (col2ask not in df_hsk.columns):
            raise ValueError( "col2ask = \"%s\" not vocabulary!" % col2ask)

    col2delete = df_hsk.columns[np.flatnonzero(np.core.defchararray.find(df_hsk.columns.values.astype(str), "Unnamed")!=-1)]
    df_hsk.drop(columns = col2delete, inplace = True)
    #print(df_hsk)
    l_ind = df_hsk.query("register == %d" % register).index.tolist()
    print("(Found %s words in register %d)" % (len(l_ind), register))
    print("")
    for i, myind in enumerate(np.random.choice(l_ind, size = len(l_ind), replace=False)):
        #clear_output()
        print("Word %d out of %d in register %d" % (i+1, len(l_ind), register))
        #plt.figure()
        #plt.plot()
        if col2show == "all":
            for j, mycol in df_hsk.drop(columns = "register").iteritems():
                print(j, ":", mycol.loc[myind,])
            #print(df_hsk.drop(columns = "register").loc[myind])
            #print(df_hsk.loc[myind].to_frame().drop(columns = "register"))
            #plt.text(0,0, df_hsk.loc[myind, "Pinyin"] + "\n" +
            #              str(df_hsk.loc[myind, "English"]) + "\n",
            #         fontdict = { "fontweight" : "bold",
            #                      "fontsize"   : 20})
            #plt.show()
        myprompt = ""
        while myprompt == "":
            if col2show == "all":
                myprompt = input("Did you know? (y - yes, n - no, s - skip, q - quit, x - quit and save): ")
            else:
                #print(df_hsk.loc[myind, col2show])
                #print(col2show)
                #print(col2ask)
                myprompt = input("\"%s\" in %s ? (or type \"\" - (check answer directly), s - skip, q - quit, x - quit and save): " % (df_hsk.loc[myind, col2show],
                                                                                                  col2ask))
            if myprompt == "s":
                print("(Skipping current word)")
                break
            elif myprompt == "q":
                print("(Quit without Saving)")
                return
            elif myprompt == "x":
                print("(Quit with Saving to \"" + infilename + ".restart.xlsx\")")
                df_hsk.to_excel(infilename + ".restart.xlsx", index = False)
                return
            elif col2show == "all":
                if myprompt   == "y":
                    df_hsk.loc[myind, "register"] += 1
                    print("(word moved up one to register %d)" % df_hsk.loc[myind, "register"])
                    break
                elif myprompt == "n":
                    df_hsk.loc[myind, "register"] = 0
                    print("(word moved back to register %d)"   % df_hsk.loc[myind, "register"])
                    break
                else:
                    print("(Error: Input not understood, please try again)")
                    myprompt = ""
            else:
                if myprompt == "":
                    print("Correct answer: \"%s\"" % (df_hsk.loc[myind, col2ask]))
                    myprompt2 = "____"
                    while myprompt2 == "____":
                        myprompt2 = input("Did you know? ([Enter] - yes, n - no): ")
                        if myprompt2   == "":
                            df_hsk.loc[myind, "register"] += 1
                            print("(word moved up one to register %d)" % df_hsk.loc[myind, "register"])
                            break
                        elif myprompt2 == "n":
                            df_hsk.loc[myind, "register"] = 0
                            print("(word moved back to register %d)"   % df_hsk.loc[myind, "register"])
                            break
                        else:
                            print("(Error: Input not understood, please try again)")
                            myprompt2 = "____"
                    break
                elif (myprompt == df_hsk.loc[myind, col2ask]):
                    df_hsk.loc[myind, "register"] += 1
                    print("(Correct, word moved up one to register %d)" % df_hsk.loc[myind, "register"])
                    break
                else:
                    df_hsk.loc[myind, "register"]  = 0
                    print("No, correct answer: \"%s\"\n(word moved back to register %d)" % (df_hsk.loc[myind, col2ask],
                                                                                 df_hsk.loc[myind, "register"]))
                    break
        
        if (i % 10) == 0:
            df_hsk.to_excel("bakup.xlsx", index = False)
        print("\n")
    myprompt = ""
    while myprompt not in ["q", "x"]:
       myprompt = input("Vocabulary Practice Done. What to do next? (q - quit, x - quit and save): ")
       if myprompt == "q":
           print("(Quit without Saving)")
           return
       elif myprompt == "x":
           print("(Quit with Saving to \"" + infilename + ".restart.xlsx\")")
           df_hsk.to_excel(infilename + ".restart.xlsx", index = False)
           return

if __name__ == "__main__":
    practice( infilename    = args.infilename, 
              col2show      = args.col2show,
              col2ask       = args.col2ask,
              is_first_run  = args.is_first_run,
              register      = args.register)
