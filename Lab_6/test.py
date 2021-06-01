import pickle
mesage=["Wow\n","What the hell is this\n"]
mesage=pickle.dumps(mesage)
msg=pickle.loads(mesage)
for i in msg:
    test=input(i)
    print(test)