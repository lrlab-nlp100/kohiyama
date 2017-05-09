def cipher(sent):
    return "".join(chr(219 - ord(str)) if str.islower() == True else str  for str in sent)
#return "".join(char(219 - ord(i)) if i.islower()== True else i for i in str)

sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(cipher(sent))
