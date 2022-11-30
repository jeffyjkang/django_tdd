from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from .forms import HashForm
import hashlib
from .models import Hash
from django.core.exceptions import ValidationError
import time

class FunctionalTestCase(TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def test_there_is_homepage(self):
    self.browser.get('http://localhost:8000')
    self.assertIn('Enter hash here:', self.browser.page_source)

  def test_hash_of_hello(self):
    self.browser.get('http://localhost:8000')
    text = self.browser.find_element(By.ID, 'id_text')
    text.send_keys('hello')
    self.browser.find_element(By.NAME, 'submit').click()
    self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

  def test_hash_ajax(self):
    self.browser.get('http://localhost:8000')
    text = self.browser.find_element(By.ID, 'id_text')
    text.send_keys('hello')
    time.sleep(5)
    self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

  def tearDown(self):
    self.browser.quit()

class UnitTestCase(TestCase):

  def test_home_homepage_template(self):
    res = self.client.get('/')
    self.assertTemplateUsed(res, 'hashing/home.html')

  def test_hash_form(self):
    form = HashForm(data={'text': 'hello'})
    self.assertTrue(form.is_valid())

  def test_hash_func_works(self):
    text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
    self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash)

  def save_hash(self):
    hash = Hash()
    hash.text = 'hello'
    hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
    hash.save()
    return hash

  def test_hash_object(self):
    hash = self.save_hash()
    pulled_hash = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
    self.assertEqual(hash.text, pulled_hash.text)

  def test_viewing_hash(self):
    hash = self.save_hash()
    res = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
    self.assertContains(res, 'hello')

  def test_bad_data(self):
    def badHash():
      hash = Hash()
      hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b982411111'
      hash.full_clean()
    self.assertRaises(ValidationError, badHash)
