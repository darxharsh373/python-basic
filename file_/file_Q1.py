'''
Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’. 


'''
st="Hey Harsh you are amazing.\n" \
"Have you read a famous poem in your childhood that is twinkle twinkle "
# f=open("poems.txt","w")
# f.write(st)
f=open("poems.txt","r")
content=f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")
else:
    print("The word twinkle is not present")

f.close()