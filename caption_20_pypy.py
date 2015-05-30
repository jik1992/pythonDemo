import profile


def profileTest():
    total = 1
    for i in range(10):
        total *= i + 1
        print total
    return total


if __name__ == "__main__":
    profile.run("profileTest()")


#brew install pypy
