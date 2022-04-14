print("Plastic Pollution Quiz")
questions=[
"What happens to plastic waste when left in the environment?",
"Why is plastic dangerous for marine life?",
"How many million tons of plastic are dumped in our oceans every year?",
"True or False: There are many alternatives to single use plastic products.",
"How many marine species are harmed by plastic pollution?"
]



options=[[
            "It is a biodegradable material so it eventually disintegrates",
            "It never fully goes away",
            "it just breaks into little pieces"
            ,"There is no such thing as plastic waste, all plastic is recycled"]

,[
    "They mistake it for food and cannot digest it",
    "They can get tangled in it which hinders their ability to swim",
    "Bacteria on plastic can give coral diseases",
    "A, B, and C"]
,[
    "1 million tons",
    "8 million tons",
    "20 million tons",
    "50 million tons"],
["true","False"],
["52","693","1,326","5,489"]]



answers=[2,4,2,1,2]

#question1
print(questions[0])
num=1
for i in options[0]:
    print(num,i)
    num=num+1
useranswer=int(input('enter your answer'))
if useranswer==answers[0]:
    print("congrats your answer is correct")
else:
    print("your answer is wrong")
    
#question1
print(questions[1])
num=1
for i in options[1]:
    print(num,i)
    num=num+1
useranswer=int(input('enter your answer'))
if useranswer==answers[1]:
    print("congrats your answer is correct")
else:
    print("your answer is wrong")
    
#question2
print(questions[2])
num=1
for i in options[2]:
    print(num,i)
    num=num+1
useranswer=int(input('enter your answer'))
if useranswer==answers[2]:
    print("congrats your answer is correct")
else:
    print("your answer is wrong")
    
#question3
print(questions[3])
num=1
for i in options[3]:
    print(num,i)
    num=num+1
useranswer=int(input('enter your answer'))
if useranswer==answers[3]:
    print("congrats your answer is correct")
else:
    print("your answer is wrong")
    
#question4
print(questions[4])
num=1
for i in options[4]:
    print(num,i)
    num=num+1
useranswer=int(input('enter your answer'))
if useranswer==answers[4]:
    print("congrats your answer is correct")
else:
    print("your answer is wrong")