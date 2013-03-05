##Tangent law
import time

T = time.time()

W = WeylGroup("A3",prefix="s")
[s0,s1,s2] = W.simple_reflections()
w0 = W.long_element(); w0
e = s0*s0
e_w0 = W.bruhat_interval(e,w0); e_w0

for i in (e_w0):
    print "These are reduced expressions for ", i , " : ", i.reduced_words() 
###the above gives all reduced words for elements in S_4


#R1 = PolynomialRing(ZZ,'y',4)
#F1 = FractionField(R1)
#R2 = PolynomialRing(F1,'x',4)
#F2 = FractionField(R2)
##Inject the variables so can use names
#R1.injvar()
#R2.injvar()
#PP = PositiveIntegers() ##The positive integers
#schur = SymmetricFunctions(ZZ).s() ##Define the ring of symmetric functions L
#I =R2.ideal([R2(schur([n]).expand(4,alphabet='x'))-R2(schur([n]).expand(4,alphabet='y')) for n in range(1,5)])
#S = R2.quotient(I)

##cohomology
var('z00,z01,z02,z03,z10,z11,z12,z13,z20,z21,z22,z23,z30,z31,z32,z33,u01,u10,u12,u21,u23,u32,u02,u20,u13,u31,u03,u30')
var('a,b')
#def oplus(a,b):
#    return (a + b)/(1 + a*b)
#z00 = oplus(x0,-y0)
#z01 = oplus(x0,-y1)
#z02 = oplus(x0,-y2)
#z03 = oplus(x0,-y3)
# z10 = oplus(x1,-y0)
# z11 = oplus(x1,-y1)
# z12 = oplus(x1,-y2)
#z13 = oplus(x1,-y3)
# z20 = oplus(x2,-y0)
# z21 = oplus(x2,-y1)
# z22 = oplus(x2,-y2)
#z23 = oplus(x2,-y3)
#z30 = oplus(x3,-y0)
#z31 = oplus(x1,-y1)
# u01 = oplus(x0,-x1)
# u10 = oplus(x1,-x0)
# u12 = oplus(x1,-x2)
# u21 = oplus(x2,-x1)
# u23 = oplus(x2,-x3)
# u32 = oplus(x3,-x2)


def T1(P):
        temp(z00,z01,z02,z03,z10,z11,z12,z13,z20,z21,z22,z23,z30,z31,z32,z33,u01,u10,u12,u21,u23,u32,u02,u20,u13,u31,u03,u30) = P
		return temp(z10,z11,z12,z13,z00,z01,z02,z03,z20,z21,z22,z23,z30,z31,z32,z33,u10,u01,u02,u20,u23,u32,u12,u21,u03,u30,u13,u31)
def T2(P):
		temp(z00,z01,z02,z03,z10,z11,z12,z13,z20,z21,z22,z23,z30,z31,z32,z33,u01,u10,u12,u21,u23,u32,u02,u20,u13,u31,u03,u30) = P
		return temp(z00,z01,z02,z03,z20,z21,z22,z23,z10,z11,z12,z13,z30,z31,z32,z33,u02,u20,u21,u12,u13,u31,u01,u10,u23,u32,u03,u30)
def T3(P):
		temp(z00,z01,z02,z03,z10,z11,z12,z13,z20,z21,z22,z23,z30,z31,z32,z33,u01,u10,u12,u21,u23,u32,u02,u20,u13,u31,u03,u30) = P
		return temp(z00,z01,z02,z03,z10,z11,z12,z13,z30,z31,z32,z33,z20,z21,z22,z23,u01,u10,u13,u31,u32,u23,u03,u30,u12,u21,u02,u20)
def A1(P):
        return (P/u01 + T1(P)/u10).simplify_full()
def A2(P):
        return (P/u12 + T2(P)/u21).simplify_full()
def A3(P):
        return (P/u23 + T3(P)/u32).simplify_full()
        
D = [A1,A2,A3]
#def Demazure(list, P):
#		for i in range(len(list)):
#			temp = D[list[i]-1](P)
#		return temp.simplify_full()
		
Pempty = (z00*z01*z02*z10*z11*z20)
##Test case 2: s2*s3*s2  :  [[2, 3, 2], [3, 2, 3]]
#print (A2(A3(A2(Pempty))) - A3(A2(A3(Pempty)))).simplify_full()
##Test case 3: s1*s2*s3*s1*s2*s1  :  [1, 2, 3, 1, 2, 1], [1, 2, 1, 3, 2, 1]
# print (A1(A2(A3(A1(A2(A1(Pempty))))))-A1(A2(A1(A3(A2(A1(Pempty))))))).simplify_full()
# =0
##Test case 4: s1*s2*s3*s1*s2*s1  :  [1, 2, 3, 1, 2, 1],[2, 1, 2, 3, 2, 1]
#print (A1(A2(A3(A1(A2(A1(Pempty))))))-A2(A1(A2(A3(A2(A1(Pempty))))))).simplify_full()
# = something horrible. for the long word it takes about 7 minutes.

AList = []

for i in (e_w0):
		AList+= i.reduced_words() 
AList.reverse()
print AList
RList = [Pempty]
for i in AList[1:]:
		itemp = i[1:]
		P = RList[AList.index(itemp)]
		RList.append(D[i[0]-1](P).simplify_full())		


for i in range(len(AList)):
		print "Z", AList[i] , " = ", RList[i]
	
print "Took ", time.time() - T