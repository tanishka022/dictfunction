def most_frequent():
    str = input("Input: Please enter a string (in uppercase) - ")

    finalstr = {i : str.count(i) for i in set(str)}

    sortedstr = sorted(finalstr.items(), key = lambda x: x[1], reverse = True)

    print("Output: ", end = "")
    for y in sortedstr:
        print(y[0],"=", y[1], end = "\t")

most_frequent()