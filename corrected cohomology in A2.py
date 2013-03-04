##Tangent law
import time

T = time.time()

W = WeylGroup("A2",prefix="s")
[s0,s1] = W.simple_reflections()
w0 = W.long_element(); w0
e = s0*s0
e_w0 = W.bruhat_interval(e,w0); e_w0

for i in (e_w0):
    print "These are reduced expressions for ", i , " : ", i.reduced_words() 
###the above gives all reduced words for elements in S_4


R1 = PolynomialRing(ZZ,'y',3)
F1 = FractionField(R1)
R2 = PolynomialRing(F1,'x',3)
F2 = FractionField(R2)
##Inject the variables so can use names
R1.injvar()
R2.injvar()
PP = PositiveIntegers() ##The positive integers
schur = SymmetricFunctions(ZZ).s() ##Define the ring of symmetric functions L
I =R2.ideal([R2(schur([n]).expand(3,alphabet='x'))-R2(schur([n]).expand(3,alphabet='y')) for n in range(1,5)])
S = R2.quotient(I)

##cohomology
var('a,b')
def oplus(a,b):
    return (a + b)
z00 = oplus(x0,-y0)
z01 = oplus(x0,-y1)
z02 = oplus(x0,-y2)
#z03 = oplus(x0,-y3)
z10 = oplus(x1,-y0)
z11 = oplus(x1,-y1)
z12 = oplus(x1,-y2)
#z13 = oplus(x1,-y3)
z20 = oplus(x2,-y0)
z21 = oplus(x2,-y1)
z22 = oplus(x2,-y2)
#z23 = oplus(x2,-y3)
#z30 = oplus(x3,-y0)
#z31 = oplus(x1,-y1)
u01 = oplus(x0,-x1)
u10 = oplus(x1,-x0)
u12 = oplus(x1,-x2)
u21 = oplus(x2,-x1)
#u23 = oplus(x2,-x3)
#u32 = oplus(x3,-x2)


def T1(P):
        temp(x0,x1,x2) = P
        return temp(x1,x0,x2)
def T2(P):
	temp(x0,x1,x2) = P
        return temp(x0,x2,x1)
#def T3(P):
#		temp(x0,x1,x2,x3) = P
#        return temp(x0,x1,x3,x2)
def A1(P):
        return (P/u01 + T1(P)/u10).simplify_full()
def A2(P):
        return (P/u12 + T2(P)/u21).simplify_full()
#def A3(P):
#        return (P/u23 + T3(P)/u32).simplify_full()
        
D = [A1,A2]
def Demazure(list, P):
                list.reverse()
                temp = P
		for i in range(len(list)):
                        print "applying", D[list[i]-1]
			temp = D[list[i]-1](temp)
                        print temp
		return temp.simplify_full()
		
Pempty = (z00*z01*z10)


AList = []

for i in (e_w0):
		AList+= i.reduced_words() 
AList.reverse()
print AList
for i in AList[1:]:
	print "Z", i  , " = ", Demazure(i,Pempty)
		
print time.time() - T