names=[]

with open(r"C:\Users\snrpc\Desktop\Python\100 Days\Day24\Mail Merge Project Start\Input\Names\invited_names.txt",mode='r') as file:
    for x in file:
        names.append(x.strip())  


print(names)



with open(r"Python\100 Days\Day24\Mail Merge Project Start\Input\Letters\starting_letter.txt",mode='r') as normalletterfile:
    alltext=str(normalletterfile.read())
    for name in names:
        newletter=alltext.replace('[name]',name)
        with open(f"C:\\Users\\snrpc\\Desktop\\Python\\100 Days\\Day24\\Mail Merge Project Start\\Output\\ReadyToSend\\letter_for_{name}.txt",mode='w+') as namefile:
             namefile.write(newletter)





