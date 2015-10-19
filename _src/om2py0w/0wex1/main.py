from sys import argv
script,filename=argv
target=open(filename,'w')
line=raw_input(">")
target.write(line)
target.close()
f=open(filename,'r')
file_contents=f.read()
print file_contents
