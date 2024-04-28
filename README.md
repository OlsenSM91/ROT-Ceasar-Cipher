# ROT/Ceasar Cipher

![Screenshot 2024-04-27 222540](https://github.com/OlsenSM91/ROT-Ceasar-Cipher/assets/130707762/3e363aa2-57e1-4a42-b296-2474455d5975)

## What is the ROT/Ceasar Cipher?
Essentially, think of it as the 26 character English alphabet, A thru Z. You can have ROT1-25 as ROT 0 and 26 would be plaintext and Anything over 26 would just be repeating the same cipher as 1-25.

This type of cipher is considered symmetric as you utilize the same key to decrypt and encrypt the secret message. An explaination of the ROT cipher is pretty simple, it's a rotation of the english characters based on the number. For example ROT1 would shift all of the letters by 1, A=B, B=C, C=D...Z=A. As you increase the number, the letter shift increases by that number.

As you can imagine, decyphering ROT is very trivial and can be accomplished in seconds as there's only 26 possible combinations so cracking the ROT cipher is extremely easy. As an example, I created this simple python application that can encrypt and decrypt text files in ROT/Ceasar Cipher, whether you know the key or not.
