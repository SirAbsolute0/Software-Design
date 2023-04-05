class FibonacciTests:

  def test_canary(self):
    self.assertTrue(True)    


  def test_fibonacci_positions(self):
    responses = [[0, 1], 
                 [1, 1],
                 [2, 2],
                 [5, 8],
                 [30, 1346269]]
    
    for test in responses:
      position, value = test
      with self.subTest():
        self.assertEqual(value, self.fibonacci_implementation()(position))
  
    with self.assertRaises(ValueError):
      self.fibonacci_implementation()(-1)
