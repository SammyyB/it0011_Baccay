A = {'a', 'b', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'h', 'i', 'j', 'k'}

A_and_B = A & B
print("a. Number of elements in A and B:", len(A_and_B))

B_not_A_C = B - (A | C)
print("b. Number of elements in B that are not in A or C:", len(B_not_A_C))

set_i = C - (A | B)
print("c.i:", set_i)

set_ii = (A | C) - B
print("c.ii:", set_ii)

set_iii = A & B & C
print("c.iii:", set_iii)

set_iv = A - (B | C)
print("c.iv:", set_iv)

set_v = C - (A | B)
print("c.v:", set_v)

set_vi = B - (A | C)
print("c.vi:", set_vi)