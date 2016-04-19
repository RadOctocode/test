start_string= raw_input('Type Encrypted Message:')
def Decrypt(string):
    string.lower()
    currentkey=''
    lastkeyvalue=0
    shiftvalue=0
    array={}
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    finalMes=[]
    for i in string:
		if i not in array:
		    array[i]=1
		else:
		    array[i]=array[i]+1
    for key in array:
        if array[key]>lastkeyvalue:
            lastkeyvalue=array[key]
            currentkey=key
    print currentkey
    for x in letters:
        if currentkey==x:
            shiftvalue=letters.index('e')-letters.index(currentkey)
    print shiftvalue
    for x in string:
        for let in letters:
            if let==x:
                finalLet=letters[letters.index(let)+shiftvalue]
                finalMes.append(finalLet)
    myString = " ".join(finalMes)
    print myString
Decrypt(start_string)
#recommit
pass