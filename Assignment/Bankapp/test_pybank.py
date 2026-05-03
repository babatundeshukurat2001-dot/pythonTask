from unittest import TestCase

import pybank

class TestValidateEmail(TestCase):

    def test_that_validate_email_exists(self):
        pybank.validate_email("tyger@fred.com")
        
    def test_that_valid_email_length_is_minimum_of_8_characters(self):
        is_valid = pybank.validate_email("tyger@fred.com")
        self.assertTrue(is_valid)
        
    def test_that_valid_email_length_is_less_than_8_characters_return_false(self):
        is_valid = pybank.validate_email("ty@f.m")
        self.assertFalse(is_valid)
        
    def test_that_invalid_email_raise_value_error(self):
        self.assertRaises(ValueError, pybank.validate_email, "tygerfred.com")
        
    def test_that_valid_email_contains_special_character(self):
        is_valid = pybank.validate_email("tyger@fred.com")
        self.assertTrue(is_valid) 
        
         
    def test_that_valid_email_does_not_start_with_special_character(self):
        message = pybank.validate_email("@tygerfred.com")
        self.assertEqual(message, "Invalid email")
        
    def test_that_valid_email_does_not_end_with_special_character(self):
        message = pybank.validate_email("@tygerfred.com@")
        self.assertEqual(message, "Invalid email")   
        
        
class TestCalculateBalance(TestCase):   
    
    def test_that_calculate_balance_function_return_correct_balance(self):
        actual = pybank.calculate_balance([2500, 2000])
        expected = 4500
        self.assertEqual(actual, expected) 
    
        actual = pybank.calculate_balance([5000, 2000])
        expected = 7000
        self.assertEqual(actual, expected) 
        
        actual = pybank.calculate_balance([5000, -1000, 2000, -500])
        expected = 5500
        self.assertEqual(actual, expected)
        
    def test_that_calculate_balance_return_0_with_empty_transactions(self):
        actual = pybank.calculate_balance([])
        expected = 0
        self.assertEqual(actual, expected)
        
class TestStrongPassword(TestCase):

    def test_that_is_strong_password_return_true_with_minimum_of_8_characters(self):
        is_strong = pybank.is_strong_password("password")
        self.assertTrue(is_strong)
        
    def test_that_is_strong_password_return_false_with_minimum_of_8_characters(self):
        is_strong = pybank.is_strong_password("passwor")
        self.assertFalse(is_strong)
        
class TestApplyInterest(TestCase):   
    
    def test_that_apply_interest_function_return_correct_balance(self):
        actual = pybank.apply_interest(5000, 0.05, 10)
        expected = 8144.47
        self.assertEqual(actual, expected)
        
    def test_that_apply_interest_function_rate_can_not_be_negative(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(5000, -0.05, 10)
        
    def test_that_apply_interest_function_years_can_not_be_less_than_one(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(5000, 0.05, 0.2)

class TestGetTransactionSummary(TestCase):

    def test_that_get_transaction_summary_function_return_correct_summary(self):
        transactions = [["credit", 2000], ["debit", 500], ["credit", 1000]]
        actual = pybank.get_transaction_summary(transactions)
        expected = [["total_credits", 3000], ["total_debits", 500], ["net_balance", 2500], ["transaction_count", 3]]
        self.assertEqual(actual, expected)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
