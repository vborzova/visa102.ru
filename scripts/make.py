cntries = open("flags.txt","rb").readlines()
template= open("template","rb").read()
for c in cntries:
	name, domain = c.rstrip().split(",")
	out = open(domain+".md","wb")
	out.write(template.format(name, domain))