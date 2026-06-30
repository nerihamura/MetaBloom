# test_metabloom.py
"""
Tests for MetaBloom module.
"""

import unittest
from metabloom import MetaBloom

class TestMetaBloom(unittest.TestCase):
    """Test cases for MetaBloom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaBloom()
        self.assertIsInstance(instance, MetaBloom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaBloom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
