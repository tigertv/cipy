#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Monosub

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = u"dabcghijokzlmnpqrstuvfwxyäöeüß"

cipher = Monosub();
print(plaintext)

enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext  = u"thisisasecretmessage"
alphabet = u"abcdefghijklmnopqrstuvwxyz"
key      = u"dabcghijokzlmnpqrstuvfwxye"

print(plaintext)
enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)
