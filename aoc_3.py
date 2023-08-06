# opening the file in read mode
my_file = open("input_3.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
li = data.split("\n")
my_file.close()



count = 0
c = 0

def task_1():
    for word in range(len(li)):

        li1 = li[word][ 0 : (len(li[word])//2) ]  #First half of the word
        li2 = li[word][ len(li[word])//2 : ] #Second half of the word

        for letter in li1:
            flag = False
            for letter_2 in li2:
                if letter is letter_2:
                    if letter_2.islower():
                        count = count + ord(letter_2) - 96
                    if letter_2.isupper():
                        count = count + ord(letter_2) - 64+26
                    flag = True
                    break
            if flag is True:
                break

    #print(count)

def task_2():
    count = 0
    for i in range(0,len(li)-3,3):
        licom = []
        for letter_1 in li[i]:
            for letter_2 in li[i+1]:
                if letter_1 is letter_2:
                    licom.append(letter_1)
        for com in licom:
            flag = False
            for letter_3 in li[i+2]:
                if  com is letter_3:
                    if letter_3.islower():
                        count = count + ord(letter_3) - 96
                    if letter_3.isupper():
                        count = count + ord(letter_3) - 64+26
                    flag = True
                    break
            if flag is True:
                break
    print(count)                

task_2()
