from unittest import TestCase
import ps1
#TODO If quick and dirty infinite loop tests are desired, see PS2.

#TODO Unit tests are supposed to test individual units right?
# So how do I test functions that call other function? If the deeper call
# fails, the shallower call shouldn't necessarily.



class TestGetGCF(TestCase):
  
  def test_both_even(self):
    gcf = ps1.get_gcf(4,8)
    self.assertEqual(gcf, 4)
    
  def test_neither_even(self):
    gcf = ps1.get_gcf(9, 12)
    self.assertEqual(gcf, 3)
    
  def test_coprime(self):
    gcf = ps1.get_gcf(49, 81)
    self.assertEqual(gcf, 1)
    
  def test_reverse_order(self):
    gcf = ps1.get_gcf(3, 9)
    self.assertEqual(gcf, 3)
    
  def test_zero(self):
    gcf = ps1.get_gcf(8, 0)
    self.assertEqual(gcf, 8)
    


class TestLargest(TestCase):

  def test_all_zeros(self):
    l = ps1.largest(0, 0, 0, 0)
    self.assertEqual(l, 0)
    
  def test_all_smae(self):
    l = ps1.largest(5, 5, 5, 5)
    self.assertEqual(l, 5)
    
  def test_positive_negative(self):
    l = ps1.largest(-3, 0, 100, 6)
    self.assertEqual(l, 100)
    
  def test_all_positive(self):
    l = ps1.largest(20, 900, 34, 1)
    self.assertEqual(l, 900)
    
  
  
class TestEightBall(TestCase):

  def test_correct_type(self):
    t = type(ps1.magic_eight_ball())
    self.assertEqual(t, str)
  
  # Technically this test could fail on a good function, but 1000 is high enough
  # that it won't in practice.
  def test_nine_answers(self):
    replies = []
    for i in range(1000):
      rep = ps1.magic_eight_ball()
      if rep not in replies:
        replies.append(rep)
        
    numReplies = len(replies)
    
    self.assertEqual(numReplies, 9)
    
  
  
class TestAsciiName(TestCase):
  
  def test_correct_type(self):
    t = type(ps1.ascii_name())
    self.assertEqual(t, str)
    
  def test_multiple_lines(self):
    name = ps1.ascii_name()
    numLines = len(name.splitlines())
    self.assertTrue(numLines > 1)
    
  
  
class TestAlphaOrder(TestCase):

  def test_forward(self):
    ans = ps1.alpha_order("ape", "banana")
    self.assertEqual(ans, "ape banana")
    
  def test_backwards(self):
    ans = ps1.alpha_order("cathedral", "hOOk")
    self.assertEqual(ans, "cathedral hOOk")
    
  def test_one_empty(self):
    ans = ps1.alpha_order("", "donkey")
    self.assertEqual(ans, " donkey")
    
  def test_both_empty(self):
    ans = ps1.alpha_order("", "")
    self.assertEqual(ans, " ")
    


class TestZipStrings(TestCase):

  def test_shorter_first(self):
    ans = ps1.zip_strings("bill", "TED")
    self.assertEqual(ans, "bTiElDl")
    
  def test_longer_first(self):
    ans = ps1.zip_strings("no", "definitely")
    self.assertEqual(ans, "ndoefinitely")
    
  def test_one_empty(self):
    ans = ps1.zip_strings("", "cheer")
    self.assertEqual(ans, "cheer")
    
  def test_both_empty(self):
    ans = ps1.zip_strings("", "")
    self.assertEqual(ans, "")
    
    
    
class TestEveryOther(TestCase):

  def test_even(self):
    ans = ps1.every_other("Monkey")
    self.assertEqual(ans, "Mne")
    
  def test_odd(self):
    ans = ps1.every_other("I like cheese")
    self.assertEqual(ans, "Ilk hee")
    
  def test_empty(self):
    ans = ps1.every_other('')
    self.assertEqual(ans, '')
    
    
    
class TestCountLower(TestCase):
  
  def test_all_caps(self):
    n = ps1.count_lower("HELLO")
    self.assertEqual(n, 0)
    
  def test_all_lower(self):
    n = ps1.count_lower("hello")
    self.assertEqual(n, 5)
    
  def test_mixed(self):
    n = ps1.count_lower("What's Up Doc?")
    self.assertEqual(n, 7)
    
  def test_empty(self):
    n = ps1.count_lower("")
    self.assertEqual(n, 0)
    
  def test_all_special(self):
    n = ps1.count_lower("!#$^@#%%&@  ^#$&%$\n\t\a!$ )+=-/?.>,<\"'")
    self.assertEqual(n, 0)
    
    
    
class TestXCipher(TestCase):

  def test_empty(self):
    pT = ps1.x_cipher('')
    self.assertEqual(pT, '')
  
  def test_no_message(self):
    pT = ps1.x_cipher("dhbaowybgqorgb")
    self.assertEqual(pT, '')
  
  def test_final_x(self):
    pT = ps1.x_cipher("oudibfxHwqenfienxepiwudfnqiwbnxlxlpuibsdfipbxox")
    self.assertEqual(pT, "Hello")
  
  def test_x_in_message(self):
    pT = ps1.x_cipher("xmxaxxbewoxirgbeixmoiyvbqeroiubxueiqubwixm")
    self.assertEqual(pT, 'maximum')
  
  def test_normal_message(self):
    pT = ps1.x_cipher("xpkvu xyhubkbxtxhqf rgqrexon xnewr rewg")
    self.assertEqual(pT, "python")
    
  def test_three_xs_in_a_row(self):
    pT = ps1.x_cipher("rwgergxmxixxxefjbwdifijxdojb")
    self.assertEqual(pT, "mixed")
    
  def testt_final_message_x(self):
    pT = ps1.x_cipher("qfowienxtwqeofinqwxafweoiqgnxx")
    self.assertEqual(pT, "tax")
    
    
    
    
