from Crypto.Cipher import AES
import os


def Encrypt(filename,key):
    data = ''
    key=bytes(key,'utf-8')
    with open(filename, 'rb') as f:
        data = f.read()
    with open(filename, 'wb') as out_file:
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(data)
        out_file.write(nonce)
        out_file.write(tag)
        out_file.write(ciphertext)
def Decrypt(filename,key):
    key=bytes(key,'utf-8')
    with open(filename, 'rb') as fobj:
        nonce,tag,ciphertext=[ fobj.read(x) for x in (16, 16, -1) ]
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
    with open(filename, 'wb') as wobj:
        wobj.write(data)
def main():
    a=input("jj")
    file=input('file')
    password=input('16byte')
    dir_list=os.walk(file)
    for root, dirs, files in dir_list:
        if a=='0':
            for f in files:
                filename = os.path.join(root, f)
                Encrypt(filename,password)
        else:
            for f in files:
                filename = os.path.join(root, f)
                Decrypt(filename,password)
    
if __name__ == '__main__':

    main()