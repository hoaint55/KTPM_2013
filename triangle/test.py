import unittest
import triangle

class Test(unittest.TestCase):

    def testKhoangGiaTriCanh1(self):
        self.assertEqual(triangle.detect_triangle(2**32, 2, 2), "gia tri ngoai khoang quy dinh")
    def testKhoangGiaTriCanh2(self):
        self.assertEqual(triangle.detect_triangle(2, 2**32, 2), "gia tri ngoai khoang quy dinh")    
    def testKhoangGiaTriCanh3(self):
        self.assertEqual(triangle.detect_triangle(2, 2, 2**32), "gia tri ngoai khoang quy dinh")
    def testThamSoAm(self):
        self.assertEqual(triangle.detect_triangle(-4.0, -5.0, -5.0), "gia tri ngoai khoang quy dinh")
    def testKieu(self):
        self.assertEqual(triangle.detect_triangle('a', 4.0, 5.0), "khong dung kieu")
    def testKoLaTamGiac(self):
        self.assertEqual(triangle.detect_triangle(2.0, 3.0, 6.0),"khong la tam giac")
    def testKoLaTamGiac1(self):
        self.assertEqual(triangle.detect_triangle(2.0, 6.0, 3.0),"khong la tam giac")
    def testKoLaTamGiac2(self):
        self.assertEqual(triangle.detect_triangle(3.0, 2.0, 6.0),"khong la tam giac")
    def testKoLaTamGiac3(self):
        self.assertEqual(triangle.detect_triangle(3.0, 6.0, 2.0),"khong la tam giac")
    def testKoLaTamGiac4(self):
        self.assertEqual(triangle.detect_triangle(6.0, 3.0, 2.0),"khong la tam giac")
    def testKoLaTamGiac5(self):
        self.assertEqual(triangle.detect_triangle(6.0, 2.0, 3.0),"khong la tam giac")
    def testTamGiacCan(self):
        self.assertEqual(triangle.detect_triangle(3.0, 3.0, 5.0), "tam giac can")
    def testTamGiacCan1(self):
        self.assertEqual(triangle.detect_triangle(5.0, 3.0, 3.0), "tam giac can")
    def testTamGiacCan2(self):
        self.assertEqual(triangle.detect_triangle(3.0, 5.0, 3.0), "tam giac can")
    def testTamGiacDeu(self):
        self.assertEqual(triangle.detect_triangle(3.0, 3.0, 3.0), "tam giac deu")
    def testTamGiacVuong(self):
        self.assertEqual(triangle.detect_triangle(3.0, 4.0, 5.0), "tam giac vuong")
    def testTamGiacVuong1(self):
        self.assertEqual(triangle.detect_triangle(4.0, 5.0, 3.0), "tam giac vuong")
    def testTamGiacVuong3(self):
        self.assertEqual(triangle.detect_triangle(4.0, 3.0, 5.0), "tam giac vuong")
    def testTamGiacVuong2(self):
        self.assertEqual(triangle.detect_triangle(3.0, 5.0, 4.0), "tam giac vuong")
    def testTamGiacVuong4(self):
        self.assertEqual(triangle.detect_triangle(5.0, 3.0, 4.0), "tam giac vuong")
    def testTamGiacVuong5(self):
        self.assertEqual(triangle.detect_triangle(5.0, 4.0, 3.0), "tam giac vuong")
    def testTamGiacThuong(self):
        self.assertEqual(triangle.detect_triangle(2.0, 3.0, 4.0), "tam giac thuong")
    def testTamGiacThuong1(self):
        self.assertEqual(triangle.detect_triangle(2.0, 4.0, 3.0), "tam giac thuong")
    def testTamGiacThuong2(self):
        self.assertEqual(triangle.detect_triangle(3.0, 2.0, 4.0), "tam giac thuong")
    def testTamGiacThuong3(self):
        self.assertEqual(triangle.detect_triangle(3.0, 4.0, 2.0), "tam giac thuong")
    def testTamGiacThuong4(self):
        self.assertEqual(triangle.detect_triangle(4.0, 3.0, 2.0), "tam giac thuong")
    def testTamGiacThuong5(self):
        self.assertEqual(triangle.detect_triangle(4.0, 2.0, 3.0), "tam giac thuong")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testtriangle]
    unittest.main()
