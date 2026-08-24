if __name__ == '__main__':
    n = int(input())
    arr =list( map(int, input().split()))

max1=max(arr)
runner_up=None    
for i in arr:
    if ((runner_up is None or i > runner_up) and i!=max1):
        runner_up=i
        
print(runner_up)
