def search(pat,txt):
    M = len(pat)
    N = len(txt)

    print(f" M: {M}")
    print(f" N: {N}")

    for i in range(N - M):
        j = 0
       
        while j < M:
            # print(f"j: {j} and i: {i}")
            if txt[i + j] != pat[j] :
                break
            j += 1

        if(j == M):
            print("Pattern found at index ", i)


if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)
