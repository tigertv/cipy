#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.monosub import Monosub 
import unittest

class TestMonosub(unittest.TestCase):
	alphabet = (u"abcdefghijklmnopqrstuvwxyz",
		u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
		u"abcdefghijklmnopqrstuvwxyzäöüß",
		u"abcdefghijklmnñopqrstuvwxyz",
		(
			u"あいうえお"
			u"かきくけこ"
			u"がぎぐげご"
			u"さしすせそ"
			u"ざじずぜぞ"
			u"たちつてと"
			u"だぢづでど"
			u"なにぬねの"
			u"はひふへほ"
			u"ばびぶべぼ"
			u"ぱぴぷぺぽ"
			u"まみむめも"
			u"やゆよ"
			u"らりるれろ"
			u"わを"
			u"ん"
			u"ゃゅょぁぇ"
			u"じづ"
		)
	)

	key = (u"campfehgblutixydqzjrkvwnos",
		u"бвгдеёзийклмнопржстуфхцчшщъыьэюяа",
		u"bcdefghijklmnopqrstuvwxyzäöüßa",
		u"bcdefghijklmnñopqrstuvwxyza",
		(
			u"いうえお"
			u"かきくけこ"
			u"がぎぐげご"
			u"さしすせそ"
			u"ざじずぜぞ"
			u"たちつてと"
			u"だぢづでど"
			u"なにぬねの"
			u"はひふへほ"
			u"ばびぶべぼ"
			u"ぱぴぷぺぽ"
			u"まみむめも"
			u"やゆよ"
			u"らりるれろ"
			u"わを"
			u"ん"
			u"ゃゅょぁぇ"
			u"じづあ"
		)
	)

	plaintext = (u"text",
		u"текст",
		u"textnachtricht",
		u"unmensajedetexto",
		u"だやぎへぐゆぢ")

	ciphertext = (u"rfnr",
		u"уёмту",
		u"ufyuobdiusjdiu",
		u"vñnfñtbkfefufyup",
		u"ぢゆぐほげよづ")

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = Monosub().encrypt(self.key[i], self.plaintext[i], alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = Monosub().decrypt(self.key[i], self.ciphertext[i], alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
