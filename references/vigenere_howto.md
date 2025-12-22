# Vigenère Cipher — How-To Guide

## Overview
The Vigenère cipher is a polyalphabetic substitution cipher. It uses a repeating key to shift letters in the plaintext.

## Example
Plaintext:  A T T A C K A T D A W N  
Key:        L E M O N L E M O N L E  
Ciphertext: L X F O P V E F R N H R

## Steps
1. Align the repeating keyword with the message.
2. Convert the key letter to a shift value (A=0, ..., Z=25).
3. Shift the message letter forward by that value.
4. Wrap around at Z.

## Decryption
Subtract the key value instead of adding.
