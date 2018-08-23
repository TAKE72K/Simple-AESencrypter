from Crypto.Cipher import AES
import os
import base64

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
        try:
            data = cipher.decrypt_and_verify(ciphertext, tag)
        except ValueError:
            return 1
        else:
            pass
    with open(filename, 'wb') as wobj:
        wobj.write(data)
    return 0

def RenameFile(dir,filename):
    filename_bytes = filename.encode('utf-8')
    filename_bytes_base64 = base64.encodestring(filename_bytes)
    
    filename_bytes_base64 = filename_bytes_base64[::-1][1:]
    new_filename = filename_bytes_base64.decode('utf-8') + '.hyes'

    os.rename(os.path.join(dir, filename), os.path.join(dir,new_filename))
    
def ReserveFilename(dir, filename):
    f = filename
    filename = filename[::-1][5:][::-1]
    filename_base64 = filename[::-1] + '\n'
    filename_bytes_base64 = filename_base64.encode('utf-8')
    ori_filename = base64.decodestring(filename_bytes_base64).decode('utf-8')

    os.rename(os.path.join(dir, f),os.path.join(dir,ori_filename))
    
def aes(mode,filedir,password):

    dir_list=os.walk(filedir)
    for root, dirs, files in dir_list:
        if mode=='d':
            for f in files:
                filename = os.path.join(root, f)
                Encrypt(filename,password)
                RenameFile(root, f)
        elif mode=='e':
            for f in files:
                filename = os.path.join(root, f)
                de=Decrypt(filename,password)
                if de==1:
                    return de
                ReserveFilename(root, f)
    return 0
