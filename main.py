import random

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("1〜100の数字を当ててください: "))
    if guess < number:
        print("もっと大きいです")
        if number - guess < 10:
            print("かなり近い！")
    elif guess > number:
        print("もっと小さいです")
        if guess - number < 10:
            print("かなり近い！")
    else:
        print("正解！")

