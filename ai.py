'''

S = {fit, unfit}
A = {exercise, relax}

Your task is to write a program that given
a positive integer n, a γ-setting G (0 < G < 1), and a state s

returns the values

qn(s,exercise) and qn(s,relax)

'''

def startval(S, Action):
    index = 0
    if(S=="fit"):
        index = 0
    else:
        index = 2
    if(Action=="exercise"):
        return Exercise[index][0]*Exercise[index][1] + Exercise[index+1][0]*Exercise[index+1][1]
    else:
        return Relax[index][0]*Relax[index][1] + Relax[index+1][0]*Relax[index+1][1]

def qval(S, A, N):
    if(N==0):
        return startval(S,A)
    else:
        return startval(S,A) + y*( p(S,A,"fit")*V("fit",N-1)+p(S,A,"unfit")*V("unfit",N-1) ) 

def V(S,N):
    exercise = qval(S,"exercise",N)
    relax = qval(S,"relax",N)
    return max(exercise, relax)

def p(S,A,State):
    index = 0
    index2 = 0
    if(State=="unfit"):
	index2 = 1
    if(S=="unfit"):
        index = 2
    if(A=="exercie"):
        return Exercise[index+index2][0]
    else:
	return Relax[index+index2][0]

# variable values
n = 10
y = 0.5
s = 0 # s = {fit, unfit}, 0=fit 1=unfit
e = "exercise"
r = "relax"


assert(((y>0) and (y<1)) and ((s==0) or (s==1)))

Exercise = [[0.99, 8], [0.01, 8], [0.2, 0], [0.8, 0]]
Relax = [[0.7, 10], [3, 10], [0, 5], [1, 5]]

exerciseVal = qval(s,e,n)
relaxVal = qval(s,r,n)
