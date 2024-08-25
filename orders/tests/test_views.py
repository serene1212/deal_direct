import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestOrderCreateAPIView:
    def test_create_order_successfully(self, api_client, test_active_user, test_cart):
        api_client.force_authenticate(test_active_user)

        response = api_client.post(reverse("orders:order-create"))

        assert response.status_code == 201

        assert response.data["cart"] == test_cart.id
        assert response.data["status"] == "W"

    def test_create_user_with_no_cart(self, api_client, test_active_user):
        api_client.force_authenticate(test_active_user)

        response = api_client.post(reverse("orders:order-create"))
        print(response.data)

        assert response.status_code == 400
