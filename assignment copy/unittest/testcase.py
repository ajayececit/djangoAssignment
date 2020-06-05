from django.test import TestCase
from .restAPIService.models import User
class TestsAPIListDetailView(TestCase):



    def test_delete_with_standard_permission(self):

        # Creates mock objects
        user = User.objects.create(email='person@example.com', firstName='Test user', lastName="Test last")
        print(user)
        if not User.objects.filter(email=user.email).exists():
            user.save()
        
        else:
            pass
        self.assertEqual(204, resp.status_code, "Should delete the list from database.")
        #self.assertEqual(current_list_amount, List.objects.count() - 1, "Should have delete a list from the database.")