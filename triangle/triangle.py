import unittest
def detect_triangle(a,b,c):
    if (type(a) not in [float, int, long]) or (type(b) not in [float, int, long]) or (type(c) not in [float, int, long]): 
        return "khong dung kieu"
    elif(a > 2**32 - 1) or (b > 2**32 - 1)or (c > 2**32 - 1) : return "gia tri ngoai khoang quy dinh"
    elif(a <0 or b<0 or c<0): return "gia tri ngoai khoang quy dinh"   
    elif (a + b <= c) or (b + c <= a) or (c + a <= b):
        return "khong la tam giac"
    elif (a == b) and (b == c):
        return "tam giac deu"
    elif (a == b) or (b == c) or (c == a):
        return "tam giac can"
    elif (a*a == b*b + c*c) or (b*b == c*c + a*a) or (c*c == a*a + b*b):
        return "tam giac vuong"
    else: return "tam giac thuong"
    
