
def init(start_length=5):
    rows = range(0, start_length + 1)[::-1] #reverse the number
    for row in rows:
        print("x " * row)
    
if __name__ == '__main__':
    init()

    """
        output
        -----------
        x x x x x 
        x x x x 
        x x x 
        x x 
        x 
    """