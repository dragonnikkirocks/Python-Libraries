import math

if __name__=="__main__":
    print("Generating pi till given input ")
    num = int(input("Please give input number till which you want to display pi"))
    b='{:.'+ str(num) + 'f}'
    print('PI = ' + b.format(math.pi))
    
