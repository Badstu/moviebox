#coding:utf8
op =open("source.csv")
file = open("Avatar20091218.csv","w")

op1 = op.readlines()
for i in op1:
	i = i[:-1].split(",")
	file.write(i[1]+','+i[0]+'\n')
op.close()
file.close()