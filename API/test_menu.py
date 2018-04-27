from menu import *
import unittest
import json

class Testmenu(unittest.TestCase):
  
  def setUp(self):
    app.testing = True
    self.app = app.test_client()


  def create_menu(self):
    create_menu = {"name": "Coconut Rice",
            "price": "300",

            }
    res = self.app.post('/api/v1/auth/menu',
      data = json.dumps(new_menu_item),
      content_type='application/json')
    return res

  def test_get_menu(self):
    res = self.app.get('/api/v1.0/menu')
    self.assertEqual(res.status_code, 201)
    self.assertEqual(res.status_code, 200)
    self.assertIn('View menus', str(result.data))


  def test_delete_menu(self):

    res = self.app.get('/api/v1.0/menu')
    self.assertEqual(res.status_code, 201)
    res_del = self.app.delete('/api/v1.0/menu')
    self.assertEquals(res.status_code, 200)



  def test_edit_menu(self):
    
    res = self.app.get('/api/v1.0/menu')
    self.assertEqual(res.status_code, 201)
    
    change_res = self.app.put('/api/v1.0/menu',
            {"name": "Matoke Beef",
            "price": "300"
            }
)
    
    self.assertEqual(change_res.status_code, 200)
    self.assertIn('Updated menu', str(result.data))
            

  

if __name__ == "__main__":
  unittest.main()

