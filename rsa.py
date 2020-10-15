import math
import codecs
from math import gcd as bltin_gcd
import base64 as b6
import struct


def coprime2(a, b):
    return bltin_gcd(a, b) == 1

def split(word): 
    return [char for char in word]  

def prime(n):
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def keys(p,q):
    if p == q:

        print("p and q cant be the same try again")

    elif prime(p) and prime(q):

        n = p * q #find this thing step 2 
        print("n = ", n)

        ellerfunc = (p - 1) * (q - 1) # step 3

        print("φ =", ellerfunc)
        e = 2
        while e < ellerfunc: 
            e+=1
            if coprime2(e, ellerfunc):
                temp = e
        e = temp # step 4
        print("e =", e)

        d = 0
        while ((d * e) % (ellerfunc)) != 1:
            d +=1
        print("d =", d) #step 4

    else:
        print("not prime numbers")

    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

def rsa_encrypt(message, pub_key):
    e = pub_key[0]
    n = pub_key[1]
    en_m = []
    for i in message:
        i = ord(i)
        encoded = (i ** e ) % n
        en_m.append(encoded)
    return en_m 

def rsa_decrypt(message, private_key):
    d = private_key[0]
    n = private_key[1]
    de_m = []
    for i in message:
        i = int(i)
        decoded = (i ** d ) % n
        decoded = chr(decoded)
        de_m.append(decoded)
    return de_m 


def encrypt_base64(message):
    enc = []
    for i in message:
        b64 = b6.b64encode(bytes(str(i), 'ascii'))
        enc.append(b64)
    return enc

def decrypt_base64(message):
    enc = []
    for i in message:
        b64 = b6.b64decode(i)
        enc.append(b64)
    return enc

def concat(message):
    done = ""
    for i in message:
        i = str(i)
        done += i
    return done


############## main work ###########

print("pick two prime numbers")
p = int(input("choose prime integer: p = "))
q = int(input("choose other (different) prime integer: q = ")) # choose two numbers

(public_key, private_key) = keys(p, q) 

def please_work():
    message = 'Hello'   
    list_message = split(message)
    crypto = rsa_encrypt(list_message, public_key)
    print("Encrypted message: ", concat(crypto))
    encode_64 = encrypt_base64(crypto)
    print("Base64: ", concat(encode_64))
    decode_64 = decrypt_base64(encode_64)
    print("Decoded base64: ", concat(decode_64))
    message = rsa_decrypt(decode_64, private_key)
    print("Decoded RSA: ", concat(message))


please_work()