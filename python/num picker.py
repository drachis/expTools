import random
def pickN(N):
    amount = random.randint(0,N)
    nums = range(0,N+1)
    numb = []
    for idx, n in enumerate(nums):
        n = random.randint(0,N)
        if n not in numb:
            numb.append(n)
        if idx > amount:
            break
    print sorted(numb)

if __name__ == "__main__":
    pickN(29)
