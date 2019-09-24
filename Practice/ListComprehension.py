A = [1,2,3]

B = [1,2,3,4,5]

diff = [(a,b) for a in A for b in B if a!=b]
same = [(a,b) for a in A for b in B if a == b]

print( "Different sets are",diff)
print( "Same sets are",same)

