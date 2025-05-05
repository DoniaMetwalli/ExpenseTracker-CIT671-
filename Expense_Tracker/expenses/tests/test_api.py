import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_expense_api():
    client = APIClient()
    response = client.post('/api/expenses/', {
        "title": "Caramel Latte",
        "amount": "5.00",
        "category": "Coffee"
    }, format='json')
    assert response.status_code == 201
    assert response.data['title'] == "Caramel Latte"
    assert 'date' in response.data
