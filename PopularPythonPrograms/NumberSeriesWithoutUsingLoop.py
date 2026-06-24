def print_series(N, K):
    if N <= 0:
        print(N, end=" ")
        return
    print(N, end=" ")
    print_series(N - K, K)
    print(N, end=" ")

N = 20
K = 6
print_series(N, K)