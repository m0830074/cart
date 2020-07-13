from django.test import TestCase

# Create your tests here.
class FormTestCase(TestCase):
    def test_email_one(self):
        c = self.client
        resp = c.post('/cartok/', {'CustomerName':'123','CustomerPhone':'123','CustomerAddress':'123','CustomerEmail':'123'})
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, "/cartorder/")
    
    def test_email_2(self):
        c = self.client
        resp = c.post('/cartok/', {'CustomerName':'123','CustomerPhone':'123','CustomerAddress':'123','CustomerEmail':'123@123.com'})
        self.assertEqual(resp.status_code, 200)
    
    def test_email_3(self):
        c = self.client
        resp = c.post('/cartok/', {'CustomerName':'123','CustomerPhone':'123','CustomerAddress':'123','CustomerEmail':'@com.tw'})
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, "/cartorder/")
        
    def test_email_4(self):
        c = self.client
        resp = c.post('/cartok/', {'CustomerName':'123','CustomerPhone':'123','CustomerAddress':'123','CustomerEmail':'1584.dwsqad@com.tw'})
        self.assertEqual(resp.status_code, 200)
