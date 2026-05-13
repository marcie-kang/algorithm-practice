"""
Background information
The Hamming Code is used to correct errors, so-called bit flips, in data transmissions. Later in the description follows a detailed explanation of how it works.
In this Kata we will implement the Hamming Code with bit length 3; this has some advantages and disadvantages:

[ + ] It's simple to implement
[ + ] Compared to other versions of hamming code, we can correct more mistakes
[ - ] The size of the input triples
Task 1: Encode function
Implement the encode function, using the following steps:

convert every letter of the text to its ASCII value; (ASCII value of space is 32)
convert ASCII values to 8-bit binary;
triple every bit;
concatenate the result;
For example:

input: "hey"
--> 104, 101, 121                  // ASCII values
--> 01101000, 01100101, 01111001   // binary
--> 000111111000111000000000 000111111000000111000111 000111111111111000000111  // tripled
--> "000111111000111000000000000111111000000111000111000111111111111000000111"  // concatenated
Task 2: Decode function:
Check if any errors happened and correct them. Errors will be only bit flips, and not a loss of bits:

111 --> 101 : this can and will happen
111 --> 11 : this cannot happen
Note: the length of the input string is also always divisible by 24 so that you can convert it to an ASCII value.

Steps:

Split the input into groups of three characters;
Check if an error occurred: replace each group with the character that occurs most often, e.g. 010 --> 0, 110 --> 1, etc;
Take each group of 8 characters and convert that binary number;
Convert the binary values to decimal (ASCII);
Convert the ASCII values to characters and concatenate the result
For example:

input: "100111111000111001000010000111111000000111001111000111110110111000010111"
--> 100, 111, 111, 000, 111, 001, ...  // triples
-->  0,   1,   1,   0,   1,   0,  ...  // corrected bits
--> 01101000, 01100101, 01111001       // bytes
--> 104, 101, 121                      // ASCII values
--> "hey"
If you liked this kata, please try out some of my other katas:
Crack the PIN
Decode the QR-Code
Hack the NSA
"""
from collections import Counter

from six import binary_type

"""
"hey"
  ↓ 1단계: 각 글자를 ASCII 숫자로 변환
104, 101, 121
  ↓ 2단계: 각 숫자를 8자리 이진수로 변환
01101000, 01100101, 01111001
  ↓ 3단계: 모든 비트를 3번씩 반복
000 111 111 000 111 000 000 000   (104)
000 111 111 000 000 111 000 111   (101)
000 111 111 111 111 000 000 111   (121)
  ↓ 4단계: 전부 이어붙이기
"000111111000111000000000000111111000000111000111000111111111111000000111"
"""

from collections import Counter

def split_string(string, interval):
    copied_string = string
    splitted_string = []
    index = 0

    while index < len(string):
        splitted_string.append(copied_string[index:index+interval])
        index += interval

    return splitted_string

def encode(string):
    binary_value = [format(ord(chr), "08b") for chr in string]
    tripled_value = []

    for value in binary_value:
        tripled = ""
        for num in value:
            tripled = str(num) * 3
            tripled_value.append(tripled)

    return "".join(tripled_value)

def decode(bits):
    tripled_value = split_string(bits, 3)
    count_values = "".join([Counter(value).most_common(1)[0][0] for value in tripled_value])
    binary_value = split_string(count_values, 8)

    return "".join(chr(int(value, 2)) for value in binary_value)
