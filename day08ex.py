#문제1


ls = [4,8,2,7,6]
for i in range(4):
    for j in range( i+1, 5):
        if ls[i] > ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
print(ls)

#문제2

score = [82,85,76,79,96]
rank = [1,1,1,1,1]
for i in range(5):
    for j in range(5):
        if score[i] < score[j]:
            rank[i] = rank[i] + 1
print(score,rank)

for i in range( len(rank) ):
    print(score[i],rank[i])
