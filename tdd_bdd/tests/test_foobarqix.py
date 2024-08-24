from foobarqix import compute
import unittest

class FooBarQixTest(unittest.TestCase):
    def test_print_number(self):
        self.assertEquals(compute(1), "1")
    
    def test_print_foo(self):
        self.assertEquals(compute(9), "Foo")
    
    def test_print_foofoo(self):
        self.assertEquals(compute(3), "FooFoo")
    
    def test_print_bar(self):
        self.assertEquals(compute(10), "Bar*")
    
    def test_print_barbar(self):
        self.assertEquals(compute(5), "BarBar")
    
    def test_print_qix(self):
        self.assertEquals(compute(14), "Qix")
    
    def test_print_qixqix(self):
        self.assertEquals(compute(7), "QixQix")
        
    def test_digit_count(self):
        self.assertEquals(compute(33), "FooFooFoo")
        
    def test_print_barfoo(self):
        self.assertEquals(compute(53), "BarFoo")
        
    def test_print_zero_and_number(self):
        self.assertEquals(compute(101), "1*1")
        
    def test_zero_trace_and_foobarqix(self):
        self.assertEquals(compute(105), "FooBarQix*Bar")
        
    def test_zero_trace_fooqix(self):
        self.assertEquals(compute(10101), "FooQix**")

        