choose=input("Enter the 'E' or 'D' for encrytion or Decryption of the image: ")
if choose=='E' or choose=='e':
    path=input(r'Enter the path of the image:')
    key=int(input('Enter the key value: '))
    print("the path of the image: ",path)
    print("The key of the is Encryption:",key)
    file=open(path,'rb')
    #print(file)
    img=file.read()
    file.close()
    img=bytearray(img)
    for index,values in enumerate(img):
        img[index]=values^key
    file=open(path,'wb')
    file.write(img)
    file.close()
    print('Encryption done......')
elif choose=='D' or choose=='d':
    path=input(r'Enter the path of the image:')
    key=int(input('Enter the key value: '))
    print("the path of the image: ",path)
    print("The key of the is Decryption:",key)
    file=open(path,'rb')
    #print(file)
    img=file.read()
    file.close()
    img=bytearray(img)
    for index,values in enumerate(img):
        img[index]=values^key
    file=open(path,'wb')
    file.write(img)
    file.close()
    print('Decryption done......')
else:
    print("Enter the correct choice")
