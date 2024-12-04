# file=open('myfile.txt')
# content=file.read()
# print(content)
# file.close()

with  open('c:/Users/snrpc/Desktop/Python/100 Days/Day24/myfile.txt', mode='r') as file:
  content=file.read()
  print(content)
  


with  open('c:/Users/snrpc/Desktop/Python/100 Days/Day24/myfile.txt', mode='a') as file:
  content=file.write('New line added')
  
  

with  open('c:/Users/snrpc/Desktop/Python/100 Days/Day24/myfile.txt', mode='r') as file:
  content=file.read()
  print(content)