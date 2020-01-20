# Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex)
# some regular expression practice

import re

'''
special regex characters
. - any charchter except new line
\d - digits
\D - not digits
\w - word characters including digits and _
\W - not word character
\s - whitespace
\S - not white space

Anchors
\b - word boundary
\B - without word boundary
^ - Beginning of string
$ - End of string

'''
text = '''
daniel
nelly
Ernest

718-543-5454
123.432.4543

blabla@gmail.com


'''
sentence = 'Start a sentence and then bring it to an end, also abc'

pattern = re.compile(r'abc')

matches = pattern.search(sentence)

print(matches)
# for match in matches:
#     print(match) # shows that the span = (51, 54)
#     print(sentence[51:54]) # confirms it