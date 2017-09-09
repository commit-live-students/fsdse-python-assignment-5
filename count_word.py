"""
Write a function that should count word occurance in file.
Define function 'countWord' which will accept two arguments, filepath and word to find inside file.
You can create your own file or you can use given testfile.txt inside files directory.
Calculate word occurance. Function should return count.
Function should pass all test cases.
Instructions:

Program should be written in file count_word.py
Function name should be countWord.
Input
 File = Learning from machine, machine learning.

 Type:  File path and string
 Value: Word = learning
Expected Output
  Type:  Integer
  Value: 2
 """
def countWord(filename,word):
    count = 0
    f = open(filename,'r')
    for line in f:
        if word in line:
            count+=1
    f.close()
    return count
