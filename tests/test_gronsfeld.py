#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Gronsfeld
from secretpy import alphabets
import unittest


class TestGronsfeld(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.RUSSIAN,
        alphabets.GERMAN,
        alphabets.SPANISH,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (
        (14, 5, 9, 17, 16),
        (3, 17, 19, 7, 10),
        (24, 7, 9, 1, 0),
        (11, 6, 8, 14, 12),
        (2, 16, 1, 4, 15),
    )

    plaintext = (
        u"attackatdawn",
        u"текст",
        u"textnachtricht",
        u"unmensajedetexto",
        u"づじ",
    )

    ciphertext = (
        u"oycrsyfcuqks",
        u"ххэшь",
        u"nlcunyjqurcjqu",
        u"fstrydgqroozmlfz",
        u"どぬ",
    )

    cipher = Gronsfeld()

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = self.cipher.encrypt(self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = self.cipher.decrypt(self.ciphertext[i],
                                      self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
