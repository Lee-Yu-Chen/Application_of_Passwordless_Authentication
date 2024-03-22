"https://www.askpython.com/python-modules/python-hashlib-module"

import hashlib as h


text=input()

encoded=text.encode()

hashobject=h.sha256(encoded)

hashvalue=hashobject.hexdigest()


#print('\n',hashobject)
print(hashvalue)
print("len : ",len(hashvalue),'\n')



'''
update and compare string

ho1=h.sha256("good morning".encode())

ho1.update(' good afternoon'.encode())

(h.sha256('good morning good afternoon'.encode()).hexdigest()==ho1.hexdigest())

'''
