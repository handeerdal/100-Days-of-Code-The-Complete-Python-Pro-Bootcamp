import string

print('''
  ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_| 
      ''')


list_lower=list(string.ascii_lowercase)
list_upper=list(string.ascii_uppercase)


def encode(shift,msg):
    """
    encodes the caesar encryption (docstring )
    """
    tempmsg=''
    for i in msg:
        if i in string.ascii_lowercase:
            shiftedposition=list_lower.index(i)+shift
            if shiftedposition>len(list_lower):
                shiftedposition=shiftedposition-len(list_lower)            
            tempmsg+=list_lower[shiftedposition]

        elif i in string.ascii_uppercase:
            shiftedposition=list_upper.index(i)+shift
            if shiftedposition>len(list_upper):
                shiftedposition=shiftedposition-len(list_upper) 
            tempmsg+=list_upper[shiftedposition]


        else:
            tempmsg+=i

    return tempmsg

def decode(shift,msg):
    tempmsg=''
    for i in msg:
        if i in string.ascii_lowercase:
            shiftedposition=list_lower.index(i)-shift
            if shiftedposition<0:
                shiftedposition=shiftedposition+len(list_lower)            
            tempmsg+=list_lower[shiftedposition]

        elif i in string.ascii_uppercase:
            shiftedposition=list_upper.index(i)+shift
            if shiftedposition<0:
                shiftedposition=shiftedposition+len(list_upper) 
            tempmsg+=list_upper[shiftedposition]


        else:
            tempmsg+=i

    return tempmsg




while True:
    get=int(input('Press 1 for encode or press 2 for decode. press 0 for leave'))
    if get==0:
        break
    msg=input('Type your message')
    shift=int(input('Type your shift number'))
    if get==1:
        print(f'Message is {encode(shift,msg)}')
    elif get==2:
        print(f'Message is {decode(shift,msg)}')
    else:
        print('smt is wrong')