#!/usr/bin/python3

################################
# File Name:	test_ShippingLogicUnitTest.py
# Author:		Josh Haymond
# Date:			11/19/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Unittest for ShippingLogic
################################


import unittest
from ShippingLogic import *
from basket import Basket
from SaleItem import SaleItem

class TestShippingLogic(unittest.TestCase):
	
	
	def setUp(self):
		""" the text fixture, necessary setup for the tests to run
		"""
		self.theLogic = ShippingLogic()
		
	def tearDown(self):
		""" nothing to tear down here
		If your test created a database or built a network connection
		you might delete the database or close the network connection
		here. You might also close files you opened, close your
		TK windows if this is GUI program, or kill threads if this is
		a multithreaded application
		"""
		pass # nothing to do



	def test_GetName(self):
		""" Test the getName function for ShippingLogic and subclasses.
		The default shipping object in this test class is the standard 
		logic. The sale logic should return a different name.
		"""
		
		self.assertEqual(self.theLogic.getName(), 'Standard')
		
		
		saleLogic = SaleShippingLogic()
		self.assertEqual(saleLogic.getName(), 'Sale')
	
	def test_CalcCostForShippingByWeight(self):
		""" 
		"""
		self.assertEqual(self.theLogic.calcCostForShippingByWeight(.01), 5)
		self.assertEqual(self.theLogic.calcCostForShippingByWeight(1), 7)
		self.assertEqual(self.theLogic.calcCostForShippingByWeight(5), 10)
		self.assertEqual(self.theLogic.calcCostForShippingByWeight(100), 0)
	
	def test_CalcWeightForCost(self):
		"""
		"""
		theBasket = Basket()
		
		self.assertEqual(self.theLogic.calcWeightForCost(theBasket), 0)
		
		theBasket.addItem((1, SaleItem(['10', '2', 'TestItem'])))
		self.assertEqual(self.theLogic.calcWeightForCost(theBasket), 2)
