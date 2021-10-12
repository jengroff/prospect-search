from rest_framework.test import APIClient, APITestCase

from prospectdb.models import Prospect
from prospectdb.serializers import ProspectSerializer


class ViewTests(APITestCase):
    """
    This test (i) creates a record in the prospectdb database table;
    (ii) initializes a test client; (iii) makes a GET request to the prospects API;
    (iv) confirms that the response contains every record in the database.
    """
    fixtures = ['test_prospects.json']

    def setup(self):
        self.client = APIClient()

    def test_empty_query_returns_everything(self):
        response = self.client.get('/api/v1/prospectdb/prospects/')
        prospects = Prospect.objects.all()
        self.assertJSONEqual(response.content, ProspectSerializer(prospects, many=True).data)

    # def test_query_matches_id(self):
    #     response = self.client.get('/api/v1/prospectdb/prospects/?query=josh.engroff@gmail.com')
    #     self.assertEquals(1, len(response.data))
    #     self.assertEquals("743d1241-8b02-4729-b41d-23d1197cafd0", response.data[0]["id"])
