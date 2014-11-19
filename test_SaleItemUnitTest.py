#!/usr/bin/python3

################################
# File Name:	test_SaleItemUnitTest.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Unittest for SaleItem
################################


import unittest
from SaleItem import SaleItem

class TestSaleItem(unittest.TestCase):
	
	
	def setUp(self):
		""" the text fixture, necessary setup for the tests to run
		"""
		self.theSaleItem = SaleItem(['10', '2', 'TestItem'])
		
		
	def tearDown(self):
		""" nothing to tear down here
		If your test created a database or built a network connection
		you might delete the database or close the network connection
		here. You might also close files you opened, close your
		TK windows if this is GUI program, or kill threads if this is
		a multithreaded application
		"""
		pass # nothing to do
		
	def test_GetCost(self):
		
		self.assertEqual(self.theSaleItem.getCost(), '10')
		
	def test_GetWeight(self):
		self.assertEqual(self.theSaleItem.getWeight(), '2')
		
	def test_GetTitle(self):
		self.assertEqual(self.theSaleItem.getTitle(), 'TestItem')
		
	def test_GetDetailsAsString(self):
		self.assertEqual(self.theSaleItem.getDetailsAsString(), 'TestItem $10')
		
	def test_GetID(self):
		self.assertEqual(self.theSaleItem.getID(), 5)

	def test_GetFreeShipping(self):
		
		# the default item in setUp() does not have free
		# shipping
		
		self.assertEqual(self.theSaleItem.getFreeShipping(), False)
		
		
		itemWithFreeShipping = SaleItem(['10', '2', 'FSTestItem', 'FS'])
		self.assertEqual(itemWithFreeShipping.getFreeShipping(), True)
