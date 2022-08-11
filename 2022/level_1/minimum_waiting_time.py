# O(nlogn) | O(1)
def solution(queries):
 
    queries.sort()  #sort out the queries | bigest at the end
    total = 0

    length = len(queries)
    for q in queries:
        length -= 1
        total = total + ( length * q)
        
    return total    
        
        
if __name__ == '__main__':
    
    #optimalMinimumWaitingTime = 17
    queries = [3,1,1,2,6] #[duration_1, duration_2, duration_3,....]
    minimalWaitingTime = solution(queries)
    print("minimalWaitingTime: ", minimalWaitingTime)
    