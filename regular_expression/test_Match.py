import re
pattern = re.compile(r'(\w+) (\w+) (?P<word_group>.*)')
match = pattern.match('I love you!')

print "match.string:", match.string
print "match.re:", match.re
print "match.pos:", match.pos
print "match.endpos:", match.endpos
print "match.lastindex:", match.lastindex
print "match.lastgroup:", match.lastgroup

print "match.group(1,2):", match.group(1, 2)
print "match.groups():", match.groups()
print "match.groupdict():", match.groupdict()
print "match.end(2):", match.end(2)
print "match.span(2):", match.span(2)
print "match.exoand(r'\2 \1\3'):", match.expand(r'\2 \1 \3')


# print results:
# match.string: I love you!
# match.re: <_sre.SRE_Pattern object at 0x10f6886c0>
# match.pos: 0
# match.endpos: 11
# match.lastindex: 3
# match.lastgroup: word_group
# match.group(1,2): ('I', 'love')
# match.groups(): ('I', 'love', 'you!')
# match.groupdict(): {'word_group': 'you!'}
# match.end(2): 6
# match.span(2): (2, 6)
# match.exoand(r' '): love I you!