import random

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("1〜100の数字を当ててください: "))
    if guess < number:
        print("もっと大きいです")
    elif guess > number:
        print("もっと小さいです")
    else:
        print("正解！")
