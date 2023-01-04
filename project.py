#part1
def func(file):
    with open(file,"w+") as file:
        file.write("The Text:\n")
        file.write("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'\n")
        file.write("J.U.U.U Kmltin.\n")
        file.write("mmps iks nmk eio; ---> hkmu")
        file.seek(0)
        data = file.read().lower()
        dict1 = {}
        for char in data:
            if char.isalpha():
                if char not in dict1:
                    dict1[char] = 1
                else:
                    dict1[char] += 1
        max_k = sorted(dict1 , key =dict1.get,reverse = True)
        _list=[]
        for i in range(4):
            _list.append(max_k[i])
        list_common = ["e","t","o","r"]
        global d1
        d1 = dict(zip(_list, list_common))
        d2 = dict(zip(list_common, _list))
        d1.update(d2)
        print(d1)
func("file4.txt")


#part2
_txt = """'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'
J.U.U.U Kmltin.
mmps iks nmk eio; ---> hkmu"""

def refunc(input_st):
    input_st = input_st.lower()
    d1_keys = list(d1.keys())
    result = ""
    for letter in input_st:
        if letter in d1_keys:
            result+= d1[letter]
        else:
            result+= letter
    print(result)
    return result
refunc(_txt)

#part3
def funcpath(txt):
    with open("file4.txt", "a") as file:
        file.write(" \n")
        file.write(" \n")
        file.write("The encryption for the above text is: \n ")
        file.write(refunc(_txt))
    with open("result.txt", "w+") as f:
        f.write(refunc(_txt))
        f.seek(0)
funcpath(("result.txt"))
#funcpath("C:/Users/windows11/PycharmProjects/myProject/result.txt")


def longfunc(txt):
    global list_long
    longest_word = ""
    list_long = []
    longest_word = longest_word.strip(" ,.'->")
    with open ("result.txt", "r") as f:
        r = f.read().split()
        for word in r:
            word = word.strip(",.'->")
            if len(word) > len(longest_word):
                longest_word = word
        list_long.append(longest_word)
        print(list_long)
    return(list_long)
longfunc(("result.txt"))
#longfunc("C:/Users/windows11/PycharmProjects/myProject/result.txt")

def lincount(txt):
    global counter
    counter=0
    with open ("result.txt", "r") as files:
        lines = files.readlines()
        for i in lines:
            counter += 1
        print(counter)
lincount("result.txt")
#lincount("C:/Users/windows11/PycharmProjects/myProject/result.txt")

def funcend(txt):
        with open("result.txt", "a") as file:
            file.write(" \n")
            file.write(" \n")
            file.write((list_long[0]+" ")*counter)
funcend(("result.txt"))
#funcend("C:/Users/windows11/PycharmProjects/myProject/result.txt")