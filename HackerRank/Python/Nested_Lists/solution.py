if __name__ == '__main__':
    data = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])

    scores = sorted(set(score for name, score in data))
    second_lowest = scores[1]
    names = [name for name, score in data if score == second_lowest]
    for name in sorted(names):
        print(name)
