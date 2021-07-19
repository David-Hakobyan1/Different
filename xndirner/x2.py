from re import match,search,findall,split,sub,compile
# gtnum e toxi skzbum exac bar@
bar = match("av","av amen ban")
print(bar.group())
bar = search("ban","ev sksvec amen ban")
print(bar.group())
bar = findall("am","amen angam amanorin aman chaman")
print(bar)
bar = split("ay","barev im hay exabayr",maxsplit=1)
print(bar)
bar = sub("ashxarh","erkir","kangnir ashxarh ijnox ka")
print(bar)
b = compile("av")
bar=b.findall("amen aravot avton nstum")
print(bar)

