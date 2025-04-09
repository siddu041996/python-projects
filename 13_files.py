# File I/O Ops

# Python can be used to do ops on FileExistsError

# Types of files:

# 1.text files....txt,docs,log.....etc
# 2.binary files....mp4,.png,.jpeg....etc

# open file:

f = open("apf-doc","r")   # mode .... r=read w=write  default=r

data = f.read()
# print(data)
print(type(data))
f.close()