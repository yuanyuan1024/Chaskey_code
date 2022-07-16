Rn=2
ws_str=32
bound=7
def Round(ai0,ai1,ai2,ai3,ai10,ai11,ai12,ai13,x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,z0,z1,z2,z3):
    file.write("(assert (= ((_ extract 31 31) "+z0+" ) (_ bv0 1)))\n")
    file.write("(assert (= "+z0+" (bvxor (bvlshr (bvxor "+ai1+" "+x0+" "+x1+") #x0001) (bvlshr "+z0+" #x0001))))\n")
    file.write("(assert (= (bvxor "+x1+" "+ai1+") (bvand (bvxor "+x1+"  "+ai1+") "+z0+")))\n")
    file.write("(assert (= (bvxor "+x1+" "+x0+") (bvand (bvxor "+x1+"  "+x0+") "+z0+")))\n")

    file.write("(assert (= ((_ extract 31 31) "+z1+") (_ bv0 1)))\n")
    file.write("(assert (= "+z1+" (bvxor (bvlshr (bvxor "+x8+" "+x4+" "+x9+") #x0001) (bvlshr "+z1+" #x0001))))\n")
    file.write("(assert (= (bvxor "+x9+" "+x4+") (bvand (bvxor "+x9+"  "+x4+") "+z1+")))\n")
    file.write("(assert (= (bvxor "+x9+" "+x8+") (bvand (bvxor "+x9+"  "+x8+") "+z1+")))\n")

    file.write("(assert (= ((_ extract 31 31) "+z2+") (_ bv0 1)))\n")
    file.write("(assert (= "+z2+" (bvxor (bvlshr (bvxor "+ai2+" "+x6+" "+x7+") #x0001) (bvlshr "+z2+" #x0001))))\n")
    file.write("(assert (= (bvxor "+x7+" "+ai2+") (bvand (bvxor "+x7+"  "+ai2+") "+z2+")))\n")
    file.write("(assert (= (bvxor "+x7+" "+x6+") (bvand (bvxor "+x7+"  "+x6+") "+z2+")))\n")

    file.write("(assert (= ((_ extract 31 31) "+z3+") (_ bv0 1)))\n")
    file.write("(assert (= "+z3+" (bvxor (bvlshr (bvxor ((_ rotate_left 16) "+x3+") "+x10+" "+x11+") #x0001) (bvlshr "+z3+" #x0001))))\n")
    file.write("(assert (= (bvxor "+x11+" "+x10+") (bvand (bvxor "+x11+"  "+x10+") "+z3+")))\n")
    file.write("(assert (= (bvxor "+x11+" ((_ rotate_left 16) "+x3+")) (bvand (bvxor "+x11+"  ((_ rotate_left 16) "+x3+")) "+z3+")))\n")

    file.write("(assert (= "+ai0+" (bvxor ((_ rotate_right 5)"+x2+") "+x0+")))\n")
    file.write("(assert (= "+x1+" (bvxor "+x2+" "+x3+")))\n")
    file.write("(assert (= "+x7+" (bvxor "+x5+" "+x8+")))\n")
    file.write("(assert (= "+x11+" (bvxor "+ai13+" "+ai11+")))\n")
    file.write("(assert (= "+x2+" (bvxor ((_ rotate_right 7)"+ai10+") "+x4+")))\n")
    file.write("(assert (= "+x9+" (bvxor ((_ rotate_right 16)"+ai12+") "+ai10+")))\n")
    file.write("(assert (= "+ai3+" (bvxor ((_ rotate_right 8)"+x5+") "+x6+")))\n")
    file.write("(assert (= "+x5+" (bvxor ((_ rotate_right 13)"+ai13+") "+x10+")))\n")

file=open("Chaskey_rlinear.smt2","w")
file.write("(set-info :smt-lib-version 2.0)\n")
file.write("(set-logic QF_BV)\n")
file.write("(set-option :produce-models true)\n")
file.write("\n")

#define hamming weight
file.write("(define-fun bvhamw1 ((x (_ BitVec 32))) (_ BitVec 32)\n")
file.write("(bvadd (bvlshr (bvand x #xaaaaaaaa) #x00000001) (bvand x #x55555555)))\n")
file.write("(define-fun bvhamw2 ((x (_ BitVec 32))) (_ BitVec 32)\n")
file.write("(bvadd (bvlshr (bvand x #xcccccccc) #x00000002) (bvand x #x33333333)))\n")
file.write("(define-fun bvhamw3 ((x (_ BitVec 32))) (_ BitVec 32)\n")
file.write("(bvadd (bvlshr (bvand x #xf0f0f0f0) #x00000004) (bvand x #x0f0f0f0f)))\n")
file.write("(define-fun bvhamw4 ((x (_ BitVec 32))) (_ BitVec 32)\n")
file.write("(bvadd (bvlshr (bvand x #xff00ff00) #x00000008) (bvand x #x00ff00ff)))\n")
file.write("(define-fun bvhamw5 ((x (_ BitVec 32))) (_ BitVec 32)\n")
file.write("(bvadd (bvlshr (bvand x #xffff0000) #x00000010) (bvand x #x0000ffff)))\n")
file.write("(define-fun bvhamw32_b ((x (_ BitVec 32))) (_ BitVec 32)\n")
file.write("(bvhamw5 (bvhamw4 (bvhamw3 (bvhamw2 (bvhamw1 x))))))\n")
file.write("(define-fun bvhamw ((x (_ BitVec " + str(ws_str) + "))) (_ BitVec 16)\n")
file.write("((_ extract 15 0) (bvhamw32_b x)))\n")

#define variables
a=[]
for i in range(Rn+1):
    s=[" a_"+str(i)+"_"+str(j) for j in range(4)]
    a.append(s)

x=[]
x.append([])
for i in range(1,Rn+1):
    s=[" x_"+str(i)+"_"+str(j) for j in range(12)]
    x.append(s)

z=[]
z.append([])
for i in range(1,Rn+1):
    s=[" z_"+str(i)+"_"+str(j) for j in range(4)]
    z.append(s)

for p in a:
    for q in p:
        file.write("(declare-fun "+q+" () (_ BitVec 32))\n")

for p in x:
    for q in p:
        file.write("(declare-fun "+q+" () (_ BitVec 32))\n")

for p in z:
    for q in p:
        file.write("(declare-fun "+q+" () (_ BitVec 32))\n")


for i in range(1,Rn+1):
    Round(a[i-1][0],a[i-1][1],a[i-1][2],a[i-1][3],a[i][0],a[i][1],a[i][2],a[i][3],x[i][0],x[i][1],x[i][2],x[i][3],x[i][4],x[i][5],x[i][6],x[i][7],x[i][8],x[i][9],x[i][10],x[i][11],z[i][0],z[i][1],z[i][2],z[i][3])


aa=[]
for i in range(Rn+1):
    s=[" aa_"+str(i)+"_"+str(j) for j in range(4)]
    aa.append(s)

xx=[]
xx.append([])
for i in range(1,Rn+1):
    s=[" xx_"+str(i)+"_"+str(j) for j in range(12)]
    xx.append(s)

zz=[]
zz.append([])
for i in range(1,Rn+1):
    s=[" zz_"+str(i)+"_"+str(j) for j in range(4)]
    zz.append(s)

for p in aa:
    for q in p:
        file.write("(declare-fun "+q+" () (_ BitVec 32))\n")

for p in xx:
    for q in p:
        file.write("(declare-fun "+q+" () (_ BitVec 32))\n")

for p in zz:
    for q in p:
        file.write("(declare-fun "+q+" () (_ BitVec 32))\n")


for i in range(1,Rn+1):
    Round(aa[i-1][0],aa[i-1][1],aa[i-1][2],aa[i-1][3],aa[i][0],aa[i][1],aa[i][2],aa[i][3],xx[i][0],xx[i][1],xx[i][2],xx[i][3],xx[i][4],xx[i][5],xx[i][6],xx[i][7],xx[i][8],xx[i][9],xx[i][10],xx[i][11],zz[i][0],zz[i][1],zz[i][2],zz[i][3])


file.write("(assert (= "+aa[0][0]+" ((_ rotate_right 1) "+a[0][0]+") ))\n")
file.write("(assert (= "+aa[0][1]+" ((_ rotate_right 1) "+a[0][1]+") ))\n")
file.write("(assert (= "+aa[0][2]+" ((_ rotate_right 1) "+a[0][2]+") ))\n")
file.write("(assert (= "+aa[0][3]+" ((_ rotate_right 1) "+a[0][3]+") ))\n")
file.write("(assert (= "+aa[Rn][0]+" ((_ rotate_right 1) "+a[Rn][0]+") ))\n")
file.write("(assert (= "+aa[Rn][1]+" ((_ rotate_right 1) "+a[Rn][1]+") ))\n")
file.write("(assert (= "+aa[Rn][2]+" ((_ rotate_right 1) "+a[Rn][2]+") ))\n")
file.write("(assert (= "+aa[Rn][3]+" ((_ rotate_right 1) "+a[Rn][3]+") ))\n")

file.write("(assert (= (bvadd")
for i in range(1,Rn+1):
    for j in range(4): 
        file.write(" (bvhamw "+z[i][j]+")  (bvhamw" +zz[i][j]+")")
file.write(") (_ bv"+str(bound)+" 16) ))\n")
file.write("(check-sat)\n")
file.write("(get-value (("+a[Rn][0]+") ("+a[Rn][1]+") ("+a[Rn][2]+") ("+a[Rn][3]+")))\n")
file.write("(exit)\n")

