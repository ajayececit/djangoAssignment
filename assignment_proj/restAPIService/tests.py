from django.test import TestCase
from models import User
# Create your tests here.

class TestAddMethod(TestCase):

    def setup(self):
        print(123)
        resp.status_code = 200

    
    def test_delete_with_standard_permission(self):

        print(123)
        # Creates mock objects
        user = User()
        user.firstName= "ajay"
        user.lastName= "balakumaran"
        user.email = "test1@gmail.com"
        if not User.objects.filter(email=user.email).exists():
            user.save()
            self.assertEqual(resp.status_code, 200)

        else:
            pass
        #self.assertEqual(204, resp.status_code, "Should delete the list from database.")
        #self.assertEqual(current_list_amount, List.objects.count() - 1, "Should have delete a list from the database.")