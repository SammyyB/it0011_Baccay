A = {'a', 'b', 'c', 'd', 'g', 'f'}
B = {'l', 'm', 'o', 'b', 'c', 'h'}
C = {'i', 'j', 'k', 'h', 'c', 'd', 'f'}

A_and_B = A | B
print("a. Number of elements in A and B:", len(A_and_B))

B_not_A_C = B - (A | C)
print("b. Number of elements in B that are not in A or C:", len(B_not_A_C))

#H, I, J, K
set_i = C - (A | B) | (B & C) - (A & B & C)
print("c.i:", set_i)

#C, D, F
set_ii = (C & A) | (C & B & A)
print("c.ii:", set_ii)

#B, C, H
set_iii = (C & B & A) | (A & B) | (C & B)
print("c.iii:", set_iii)

#D, F
set_iv = (A & C) - (C & B & A)
print("c.iv:", set_iv)

#C
set_v = (C & B & A)
print("c.v:", set_v)

set_vi = B - (A | C)
print("c.vi:", set_vi)