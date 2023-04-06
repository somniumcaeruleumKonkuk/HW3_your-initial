#question4

def question4(i):
    if(i == 0):
        return 1;
    return i * question4(i-1)

if __name__ == "__main__":
    for i in range(0, 15, 2):
        print(str(i)+"! =", question4(i))
