def pattern_search(pat,txt,case_sensitive=True):
    C = len(pat)
    V = len(txt)

    for f in range(V - C + 1):
        j=0
        
        while j < C:
            if case_sensitive == True:
                if txt[f + j] != pat[j]: # case insensitive
                    break
            else:
                if txt[f + j].lower() != pat[j].lower():
                    break

            j += 1

            if j == C:
                print(f"found at index {f}")

if __name__ == '__main__':
    pat="Recording"
    txt="The inside sotry of Recording metal gear solid at the recording studio here in Ohio."

    pattern_search(pat,txt)