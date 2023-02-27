data = [0,2,2,1,3,3,2]
if len(data) % 2==0:
    m1 = data[len(data)//2]
    m2 = data[len(data)//2 -1]
    median = (m1 + m2) / 2
else:
    median = data [len(data)//2]
    print(data)
    print("nilai median: ", median)
