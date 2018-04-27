from meals import *
import unittest
import json

class Testmeal(unittest.TestCase):
  
  def setUp(self):
    app.testing = True
    self.app = app.test_client()


  def create_meal(self):
    create_meal = {"name": "Coconut Rice",
            "price": "300"
            }
    res = self.app.post('/api/v1/auth/meal',
      data = json.dumps(new_meal_item),
      content_type='application/json')
    return res

  def test_get_meal(self):
    res = self.app.get('/api/v1.0/meal')
    self.assertEqual(res.status_code, 201)
    self.assertEqual(res.status_code, 200)
    self.assertIn('View Meals', str(result.data))


  def test_delete_meal(self):

    res = self.app.get('/api/v1.0/meal')
    self.assertEqual(res.status_code, 201)
    res_del = self.app.delete('/api/v1.0/meal')
    self.assertEquals(res.status_code, 200)



  def test_edit_meal(self):
    
    res = self.app.get('/api/v1.0/meal')
    self.assertEqual(res.status_code, 201)
    
    change_res = self.app.put('/api/v1.0/meal',
            {"name": "Matoke Beef",
            "price": "300"
            }
)
    
    self.assertEqual(change_res.status_code, 200)
    self.assertIn('Updated Meals', str(result.data))
            

  

if __name__ == "__main__":
  unittest.main()

