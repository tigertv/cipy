#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.rot13 import Rot13
import unittest

class TestRot13(unittest.TestCase):
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

	key = 0

	plaintext  = (u"whydidthechickencrosstheroad",
		u"текст",
		u"textnachtricht",
		u"unmensajedetexto",
		u"だやぎへぐゆぢ")

	ciphertext = (u"julqvqgurpuvpxrapebffgurebnq",
		u"вфъбв",
		u"etieüprwecxrwe",
		u"hzyqzfnvqpqgqkgb",
		u"をじぱおぴずん")

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = Rot13().encrypt(alphabet, self.key, self.plaintext[i])
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = Rot13().decrypt(alphabet, self.key, self.ciphertext[i])
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
