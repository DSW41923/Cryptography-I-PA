import gmpy2
from gmpy2 import mpfr, mpz


gmpy2.set_context(gmpy2.context())
gmpy2.get_context().precision = 5000
# Factoring challenge #1
N = 179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581
N1 = mpfr(N)
sqrt_N = gmpy2.sqrt(N1)
A = gmpy2.rint_ceil(sqrt_N)
x = gmpy2.sqrt(gmpy2.sub(gmpy2.square(A), N))
p1 = gmpy2.sub(A, x)
q1 = gmpy2.add(A, x)
print "Challenge 1:"
print p1, p1.is_integer(), gmpy2.is_prime(mpz(str(p1).split('.')[0]))
print q1, q1.is_integer(), gmpy2.is_prime(mpz(str(q1).split('.')[0]))
print p1 < q1
print gmpy2.mul(p1, q1) == N
# Factoring challenge #2
N = 648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877
N = mpfr(N)
sqrt_N = gmpy2.sqrt(N)
A = gmpy2.rint_ceil(sqrt_N)
x = gmpy2.sqrt(gmpy2.sub(gmpy2.square(A), N))
p = gmpy2.sub(A, x)
q = gmpy2.add(A, x)
while gmpy2.mul(p, q) != N or not p.is_integer() or not q.is_integer():
    A = gmpy2.add(A, 1)
    x = gmpy2.sqrt(gmpy2.sub(gmpy2.square(A), N))
    p = gmpy2.sub(A, x)
    q = gmpy2.add(A, x)
print "Challenge 2:"
print p, p.is_integer(), gmpy2.is_prime(mpz(str(p).split('.')[0]))
print q, q.is_integer(), gmpy2.is_prime(mpz(str(q).split('.')[0]))
print p < q
print gmpy2.mul(p, q) == N
# Factoring challenge #3
N = 720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929
N = mpfr(N)
sqrt_6N = gmpy2.sqrt(gmpy2.mul(6, N))
A = gmpy2.rint_ceil(sqrt_6N)
A = gmpy2.sub(A, 0.5)
x = gmpy2.sqrt(gmpy2.sub(gmpy2.square(A), gmpy2.mul(6, N)))
p = gmpy2.sub(A, x)
q = gmpy2.add(A, x)
if gmpy2.div(gmpy2.sub(A, x), 2).is_integer():
    p = gmpy2.div(gmpy2.add(A, x), 3)
    q = gmpy2.div(gmpy2.sub(A, x), 2)
else:
    p = gmpy2.div(gmpy2.sub(A, x), 3)
    q = gmpy2.div(gmpy2.add(A, x), 2)
print "Challenge 3:"
print p, p.is_integer(), gmpy2.is_prime(mpz(str(p).split('.')[0]))
print q, q.is_integer(), gmpy2.is_prime(mpz(str(q).split('.')[0]))
print p < q
print gmpy2.mul(p, q) == N
# Factoring challenge #4
# Challenge ciphertext (as a decimal integer):
CT = 22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540
CT = mpz(CT)
e = mpz(65537)
N4 = mpz(str(N1).split('.')[0])
p4 = mpz(str(p1).split('.')[0])
q4 = mpz(str(q1).split('.')[0])
phi_N = gmpy2.mul(gmpy2.sub(p4, 1), gmpy2.sub(q4, 1))
d = gmpy2.invert(e, phi_N)
msg = gmpy2.powmod(CT, d, N4)
print "Challenge 4:"
print msg
MSG = hex(msg).split('x')[-1]
MSG = '0' + MSG
print MSG.decode('hex')
