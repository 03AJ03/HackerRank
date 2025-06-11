if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    first = max(arr)  
    new_arr = [x for x in arr if x != first]
    runner_up = max(new_arr)  # find the next highest score
    print(runner_up)
