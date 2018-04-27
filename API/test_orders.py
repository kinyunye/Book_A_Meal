from orders import *
import unittest
import json

class Testorders(unittest.TestCase):
  
  def setUp(self):
    app.testing = True
    self.app = app.test_client()


  def create_orders(self):
    create_orders = {"name": "Coconut Rice",
            "price": "300",
            "quantity":"4"
            }
    res = self.app.post('/api/v1/auth/orders',
      data = json.dumps(new_orders_item),
      content_type='application/json')
    return res

  def test_get_orders(self):
    res = self.app.get('/api/v1.0/orders')
    self.assertEqual(res.status_code, 201)
    self.assertEqual(res.status_code, 200)
    self.assertIn('View orderss', str(result.data))


  def test_delete_orders(self):

    res = self.app.get('/api/v1.0/orders')
    self.assertEqual(res.status_code, 201)
    res_del = self.app.delete('/api/v1.0/orders')
    self.assertEquals(res.status_code, 200)



  def test_edit_orders(self):
    
    res = self.app.get('/api/v1.0/orders')
    self.assertEqual(res.status_code, 201)
    
    change_res = self.app.put('/api/v1.0/orders',
            {"name": "Matoke Beef",
            "price": "300",
            "quantity":"3",
            }
)
    
    self.assertEqual(change_res.status_code, 200)
    self.assertIn('Updated orderss', str(result.data))
            

  

if __name__ == "__main__":
  unittest.main()

