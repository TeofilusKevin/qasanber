import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.ChromiumEdge()
        
    def test_a_success_login(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("karimun1@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("123123")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)


        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_a_failed_login_with_empty_password(self): 
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("karimun1@gmail.com") 
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() 
        time.sleep(1)


        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_a_failed_login_with_empty_email_and_password(self): 
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() 
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_failed_signup(self): 
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() 
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() 
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("Oops...", response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_success_signup(self): 
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() 
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("Teong") 
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("karimun5@gmail.com") 
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("123123") 
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() 
        time.sleep(1) 

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("berhasil", response_data)
        self.assertEqual(response_message, 'created user!')


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()