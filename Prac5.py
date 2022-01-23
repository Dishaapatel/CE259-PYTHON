#Swaping.

def swap_case(s):

    temp = []
    l = list(s)

    for i in l:
        j = ""
        #If string is in lower case .
        if i.islower():
          #Than it will convert in upper case.
            j = i.upper()
            #Else it will work vice versa.
        elif i.isupper():
            j = i.lower()
        else:
            temp.append(i)
        temp.append(j)
    
    r = ''.join(temp)
    
    return r

  #Enter String.
s = input()
result = swap_case(s)
print(result)
