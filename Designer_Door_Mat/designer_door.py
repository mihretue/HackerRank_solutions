if __name__ == '__main__':
    
    N, M = map(int, input().split())
    
    M = N * 3
    width = M
    
    for i in range(1, N, 2):
        pattern = '.|.' * i
        print(pattern.center(width,'_'))
        
    print('WELCOME'.center(width, '_'))
    
    for l in range(N-2, 0, -2):
        pattern = '.|.'* l
        print(pattern.center(width, '_'))
        
