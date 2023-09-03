KBC="Welcome in KBC"
Qs=["A.Who is your prime minister of India?","B.What is the capital of India?","C.What is the currency of India?","D,Which is the largest state in India by area?","E.Which is the largest river in India?"]
Option=["a.Narendra Modi    b.JL Nehru    c.MK Gandhi    d.Rajeev Gandhi","a.Kolkata     b.Mumbai     c.Jaipur    d.New Delhi","a.Rubble     b.USD      c.Indian Rupee      d.Euro","a.Rajasthan     b.UP     c.Jammu and Kashmir     d.Uttarakhand","a.Yamuna    b.Satluj    c.Ganges     d.Chenab"]
Ans=["a","d","c","a","c"]
Prize=["10000","20000","30000","40000","50000"]
print(KBC)
print(Qs[0])
print(Option[0])
answer0=input("Type your answer and enter:")
if answer0==Ans[0]:
    print("Congrats your answer is right and you won",Prize[0])
else:
    print("Sorry,your answer is wrong")
    print("Sorry you don't won any money\nNow you are out from this game\nTry next time\n Thank you")
    exit()
print(Qs[1])
print(Option[1])
answer1=input("Type your answer and enter:")
if answer1==Ans[1]:
    print("Congrats your answer is right and you won",Prize[1])
else:
    print("Sorry,your answer is wrong")
    print("You won total amount rs.10000\nNow you are out from this game\nTry next time\n Thank you")
    exit()
print(Qs[2])
print(Option[2])
answer2=input("Type your answer and enter:")
if answer2==Ans[2]:
    print("Congrats your answer is right and you won",Prize[2])
else:
    print("Sorry,your answer is wrong")
    print("You won total amount rs.30000 \n Now you are out from this game\n Try next time\n Thank you")
    exit()
print(Qs[3])
print(Option[3])
answer3=input("Type your answer and enter:")
if answer3==Ans[3]:
    print("Congrats your answer is right and you won",Prize[3])
else:
    print("Sorry,your answer is wrong")
    print("You won total amount rs.60000\n Now you are out from this game\n Try next time\n Thank you")
    exit()
print(Qs[4])
print(Option[4])
answer4=input("Type your answer and enter:")
if answer4==Ans[4]:
    print("Congrats your answer is right and you won",Prize[4])
else:
    print("Sorry,your answer is wrong")
    print("You won total amount rs.1 lakh\nNow you are out from this game\nTry next time\nThank you")
    exit()
print("You are the winner of this game and You won total amount rs. 1 Lakh 50 Thousand")
print("Thank you,for playing with us.... ")