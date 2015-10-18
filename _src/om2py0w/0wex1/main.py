from sys import argv
script,filename=argv
target=open(filename,'w')
line=raw_input(">")
target.write(line)
target_again=open(filename)
print target_again.read()
