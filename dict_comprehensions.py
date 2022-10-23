def run():
#    my_dict = {}

#    for i in range(1,101):
#        if i % 3 !=0:
#            my_dict[i] = i**3 
    import numpy as np
    from numpy import sqrt
    my_dict ={i: np.sqrt(i) for i in range(1,1001) if i % 3 !=0}

    print(my_dict)




if __name__ == "__main__":
    run()