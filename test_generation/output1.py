import unittest
import re
import itertools
import input


def check_int(st):
    if len(st) == 0:
        return False
    elif (st[0] == '-'):
        return st[1:].isdigit()
    else:
        return st.isdigit()


#kiem tra mien dau vao co hop le khong
def valid(arr):
    check = 0
    for i in range(len(arr)):
        n = len(arr[i])/2
        for j in range (n):
            for k in range(j+1, n):
                if(arr[i][2*j] <= arr[i][2*k] and arr[i][2*j+1] >= arr[i][2*k]) or (arr[i][2*j] >= arr[i][2*k] and arr[i][2*j+1] <= arr[i][2*k]):
                    check +=1
    if(check == 0):
        return True
    else:
        return False
def read():
    doc = input.main.__doc__
    
    docs = (doc.split( ))
    num = len(docs) 
    final_array = [] 
    
    for i in range(num):
        strv = re.split('[:;\]\[]', docs[i])
        k = 0
        final_array.append([])
        for j in range(len(strv)):
            if(check_int(strv[j])):
                final_array[i].append(int(strv[j]))
                k += 1
    if(valid(final_array)):
        d = [] 
        for i in range(num):
            d.append([])
            n = len(final_array[i])/2
            for j in range(n):
                gt = (final_array[i][2*j] + final_array[i][2*j+1])/2
                d[i].append(gt)
        return d
    else:
        return False
class Test(unittest.TestCase):
    pass

def test_generator(a):
    def test(self):
        self.assertEqual(input.main(*a),'','') 
    return test

def main():
    if (read() != False):
        
        tb = read()
        arr = []
        i = 0
        for element in itertools.product(*tb):
            arr[len(arr):]=[element]
            i= i+1
            
            
        j = 0

        for t in arr:
            test_name = 'test_%s' % str(j)
            test = test_generator(t)
            setattr(Test, test_name, test)
            j=j+1
        unittest.main()
    else:
        raise Exception ('wrong input')
    
if __name__ == '__main__':
    main()

    
