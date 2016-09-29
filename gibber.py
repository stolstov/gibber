#A gibberish generator.

import sys
import os
import math

#A phrase consists of the following reserved letters:
#c - one of 16 consonants (4 bits entropy)
#v - one of 4 vowels (2 bits entropy)
#y - one of 8 double vowels (3 bits entropy)
#d - one of 16 composite consonants from eastern european languages (4 bits entropy)
#z - 0 or 1 (1 bit entropy)
#n - one of 16 easy to remember two digit numbers (4 bits entropy)
#p - one of 8 punctuation signs (3 bits entropy)
#{ - reserved, see below
#} - reserved, see below
#The reserved symbols can be in the upper case, indicating an upper case symbol.
#Any other symbol (including a space) will be added as is.
#For example,
#Cvcvc dycv n a p
#may correspond to
#Faval frini 66 a ?
#or
#Muwol rvyujo 60 a *
#The opening and closing curly brackets are reserved to form a repeated word.
#For example,
#V{c}
# can make the following phrase, consisting of on vowel and different consonants (66 bits):
#Ojznjzksgnwhntggd
######################
#
class Gibber:
  def __init__(self):
    self.C="BDFGHJKLMNPSTVWZ" #16 characters - 4 bits entropy
    self.D=["Sh","Ch","Zh","Pr","Ts","Ph","Rv","Gn", "Kn","Zn","Zhd","Zv","Kr","Fr","Dr","Gr"] #16 characters - 4 bits entropy
    
    self.V=["A","U","O","I"] #vowels - 2 bits entropy
    self.Y=["A","U","O","I","Ya","Yo","Yu","Ye"] #extended vowels - 3 bits entropy
    self.Z="01" #a number 0 or 1 - 1 bit entropy
    self.EasyNum=["00","11","22","33","44","55","66","77","88","99","10","20","30","40","50","60"] #16 pairs - 4 bits entropy
    self.Punct="!.,?-+*%" # 8 bit entropy.
  def __helper(self, ch, src, v):
    c = src[v]
    if ch.islower():
      return c.lower()
    
    return c
  
  def generate(self, cur_, value, bits):
    g = ""
    self.total_bits = 0
    cur = cur_;
    i = 0
    rep = False
    while bits > 0:
      if i == len(cur):
        if rep:
          i = 0
        else:
          break
      
      cur_lower = cur[i].lower()
      b = 0
      if cur_lower == 'd':
        b = 4
        g += self.__helper(cur[i], self.D, value % (1<<b))
      elif cur_lower == 'v':
        b = 2
        g += self.__helper(cur[i], self.V, value % (1<<b))
      elif cur_lower == 'y':
        b = 3
        g += self.__helper(cur[i], self.Y, value % (1<<b))
      elif cur_lower == 'p':#punctuation
        b = 3
        g += self.Punct[value % 8]
      elif cur_lower == 'c':
        b = 4
        g += self.__helper(cur[i], self.C, value % (1<<b))
      elif cur_lower == 'n':#two digit number (from 16 possible)
        b = 4
        g += self.EasyNum[value % (1<<b)]
      elif cur_lower == 'z':#0 or 1
        b = 1
        g += self.Z[value % 2]
      elif cur_lower == '{':#backet
        j = cur.find('}', i + 1)
        if j == -1:
          raise Exception('} is expected')
        cur = cur[i + 1: j]
        i = 0
        rep = 1
        continue
      else:
        g += cur[i] #something we don't know, just add

      value //= 1 << b
      bits -= b
      self.total_bits += b
      i+=1
    return g

#the main method generates a gibber word from a given value of given bits count
  def rand(self, bits):
    bytes = (int(bits) + 7) // 8 #round bits up
    z=os.urandom(bytes) #https://docs.python.org/3/library/os.html#os.urandom
    v = 0
    for b in z:
        v = v * 256 + b;
    return v
#
##################



def usage():
  print("Usage:")
  print(">>gibber -h HEXVALUE [-p PHRASE]")
  print("Generates a gibberish where HEXVALUE is a hexadecimal value.")
  print(">>proquints.py -r NUM [-p PHRASE]")
  print("Generates a random gibberish from a random NUM bit integer.")
  print("Where PHRASE is the gibberish forming phrase.")
  print("For example, a proquint forming phraze: cvcvc{-cvcvc},")
  print("             some sentence phrase: Cvcvc a cvcv vcvc{ cvcvc},")
  print("             a phrase with a two digit number")
  print("             and punctuation (39 bits): CvcvcCvcvcnp.")
  exit()


####################

proq = Gibber()

phrase = "Dvcvc{Cvcvc}"
bits = -1
value = 0
hexvalue = ""
i = 1
while i < len(sys.argv):
  if sys.argv[i] == "-r":
    bits = int(sys.argv[i+1])
    value = proq.rand(bits)
    i += 2
  elif sys.argv[i] == "-h":
    hexvalue = sys.argv[i+1].lower()
    i += 2
  elif sys.argv[i] == "-p":
    phrase = sys.argv[i+1]
    i += 2
  else:
    usage()

if bits <= -1:
  # convert the command line hexadecimal argument to an integer (non hex literals are skipped)
  hex_letters=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
  s=hexvalue
  num = len(s)

  bits = 0
  value = int(0);
  for i in range(num):
    try:
      ind = hex_letters.index(s[i])
      value = value * 16 + ind
      bits += 4
    except ValueError:
      i

  print ("fixed gibber from: " + hex(value))
else:
  print("random gibber: " + hex(value))

print("bits: "+str(bits))

print (proq.generate(phrase, value, bits))
print ("result bits: " + str(proq.total_bits))
