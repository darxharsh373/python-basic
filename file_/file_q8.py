
'''
Write a program to make a copy of a text file “this. txt” 
'''

with open("file.txt") as f:
    content=f.read()

with open ("file_copy.txt","w") as f:
    f.write(content)


'''
Q_9.
Write a program to find out whether a file is identical & matches the content of 
another file. 


'''
with open("file.txt") as f:
    content1=f.read()

with open("file_copy.txt") as f:
    content2=f.read()

if(content1==content2):
    print("Yes these files are identical")
else:
    print("no thee files are identical")
'''
Q_10.
Write a program to wipe out the content of a file using python. 

'''
with open ("file_copy.txt","w") as f:
    f.write("")
