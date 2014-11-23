#!/usr/bin/python3

################################
# File Name:	test_basketUnitTest.py
# Author:		Joey OOka
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	WillametteShippingCalculator-Group2
# Purpose:		Unittest for Basekt
################################


import unittest
from basket import Basket
from SaleItem import SaleItem
from ShippingLogic import ShippingLogic

class TestBasket(unittest.TestCase):
	
	
	def setUp(self):
		""" the text fixture, necessary setup for the tests to run
		"""
		
		self.theBasket = Basket()
		
		
	def tearDown(self):
		""" nothing to tear down here
		If your test created a database or built a network connection
		you might delete the database or close the network connection
		here. You might also close files you opened, close your
		TK windows if this is GUI program, or kill threads if this is
		a multithreaded application
		"""
		pass # nothing to do

	def test_addItem(self):
		""" add an item (qty, SaleItem)
		
		If the item already exists, add the specified quantity
		of the item to the existing entry in the basket
		"""
		item = SaleItem(['50', '4', "Python in a Nutshell"])
		if self.theBasket.contains(item.getID()):
			self.theBaseket.merge(item.getID(), 1)
			
		
		else:
			self.theBasket._items.append(item)
		
		self.assertEqual(self.theBasket.contains(item.getID()), item.getID(), True)
		
	def test_items(self):
		""" walk through the items"""
		for item in self.theBasket._items:
			yield item
		idem = SaleItem(['50', '4', "Python in a Nutshell"])
		self.assertEqual(item.getID(), idem.getID(), True)

	#def test_getTotalShipping(self):
	#	""" use the given logic to determine weight and cost
	#	"""
	#	sLogic = 
	#	weight = sLogic.calcWeightForCost(self.theBasket)
	#	cost = sLogic.calcCostForShippingByWeight(weight.theBasket)
	#	return cost
		
	#	self.assertEqual(cost, 7, True)
