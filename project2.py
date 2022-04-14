#step1 printing questions
#step2 printing opions
#step3 ask user to answer
#step4 check the answer is correct

questions=["the longest bone in our body is.",
           "shoulder girdle is also known as."
]


options=[["femur",
         "humerus",
         "ulna",
         "radius"],
        ["plevic",
         "pulmonary girdle"
         "cardiac girdle"
         "pectoral girdle"]]


answers=[1,4]
print(questions[0])
for option in options[0]:
    print(option)
answer=input("enter your answer")
if answer==answers[0]:
    print("your answer is correct")
else:
    print("your answer is wrong")
