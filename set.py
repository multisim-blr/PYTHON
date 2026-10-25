""" # sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

age = [22, 19, 24, 25, 26, 24, 25, 24]


print(len(it_companies))
it_companies.add("Twitter")

it_companies.update(["openai","anthropic","sarvam"])


it_companies.remove("openai")
print(it_companies)


 """

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.intersection(B))

print(A.union(B))

print(A.issubset(B))
print(A.isdisjoint(B)and B.isdisjoint(B))

print(A.union(B))

print(B.union(A))


print(A.symmetric_difference(B))

del A



age = [22, 19, 24, 25, 26, 24, 25, 24]


setage=set(age)

setlen=len(setage)
agelen=len(age)

maxi=max(setlen,agelen)

print(setlen)
print(agelen)
print(maxi)

str1="I am a teacher and I love to inspire and teach people."

strset=set(str1)

print(len(strset))