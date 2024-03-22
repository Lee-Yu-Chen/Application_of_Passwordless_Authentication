import hmac

key = 'leeyuchen0926'

msg = input('Please enter the message : \n')



hm = hmac.new(key.encode(),msg.encode(),digestmod='sha256')

hashvalue = hm.hexdigest()

print(hashvalue)
print('Lenght :',len(hashvalue))

