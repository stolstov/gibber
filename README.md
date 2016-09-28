#Gibber

A simple generator of a memorizable gibberish phrase.
The phrase can be generated either from a random number of given entropy (i.e. a bit count) or 
from a given number.

Based on the idea of proquints (http://arXiv.org/html/0901.4016).

Usage:

python gibber.py -r BITCOUNT

Generates a random phrase of atleast BITCOUNT bit entropy
(uses os.urandom to generate the random number)

python gibber.py -h HEXNUM

Converts given hexadecimal number (for example, 8ABEF00B) into a phrase.

The generated gibberish will have a capital letter, a number and a character.

A phrase consists of the following reserved letters:
* c - one of 16 consonants (4 bits entropy)
* v - one of 4 vowels (2 bits entropy)
* y - one of 8 double vowels (3 bits entropy)
* d - one of 16 composite consonants from eastern european languages (4 bits entropy)
* z - 0 or 1 (1 bit entropy)
* n - one of 16 easy to remember two digit numbers (4 bits entropy)
* p - one of 8 punctuation signs (3 bits entropy)
* { - reserved, see below
* } - reserved, see below

* The reserved symbols can be in the upper case, indicating an upper case symbol.

* Any other symbol (including a space) will be added as is.


For example,

python gibber.py -r 66 -p "Cvcvc dycv n a p"

may correspond to

Faval frini 66 a ?

or

Muwol rvyujo 60 a *

The opening and closing curly brackets are reserved to form a repeated word.

For example,

python gibber.py -r 66 -p V{c}

can make the following phrase, consisting of on vowel and different consonants (66 bits):

Ojznjzksgnwhntggd

To generate a standard proquint of 64 bit entropy use this phrase:

python gibber.py -r 64 -p cvcvc{-cvcvc}


##Licensing

MIT License

Copyright (c) 2016 Sergey Tolstov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

