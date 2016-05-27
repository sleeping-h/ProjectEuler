class M(dict):
	def __missing__(self,key):
		return 0
m=M()
def c(b):
	if m[b]:
		return m[b]
	if b==3:
		return 2
	if b<3:
		return 1
	m[b]=sum([c(b-i-1) for i in [0]+range(3,b+1)])
	return m[b]
print c(50)
