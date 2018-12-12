
def sort_list(x = []):
    
    if x[0] < x[1]:
        sorted_list = [x[0],x[1]]
        print(sorted_list)
        
    elif x[0] > x[1]:
        sorted_list = [x[1],x[0]]
        print(sorted_list)
        
    else:
        sorted_list = [x[0],x[1]]
        print(sorted_list)