import random

bulletsList = [
    [True, False, False, False],
    [True, True, False, False],
    [True, True, True, False],
    [True, True, False, False, False],
    [True, True, True, False, False],
    [True, True, True, False, False, False],
    [True, True, True, True, False, False],
    [True, True, False, False, False, False],
    [True, True, True, True, False, False, False],
    [True, True, True, False, False, False, False],
    [True, True, True, True, False, False, False, False],
    [True, True, True, False, False, False, False, False],
    [True, True, True, True, True, False, False, False]
]


def generateBulletList():
    randomBullet = bulletsList[random.randint(0, (len(bulletsList) - 1))]
    random.shuffle(randomBullet)
    realBullet = 0
    fakeBullet = 0
    for b in randomBullet:
        if b:
            realBullet += 1
        else:
            fakeBullet += 1
    return randomBullet, "Hay " + str(fakeBullet) + " balas falsas y " + str(realBullet) + " verdaderas."
