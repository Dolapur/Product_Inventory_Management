from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductInventoryTests(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(
            name='Test Product 1',
            description='This is a test product.',
            price= 9.99
        )
        self.product2 = Product.objects.create(
            name='Test Product 2',
            description='This is another test product.',
            price= 19.99
        )

    def test_product_display(self):
        response = self.client.get(reverse('product_display'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product2.name)

    def test_product_creation(self):
        new_product = {
            'name': 'New Product',
            'description': 'This is a new product.',
            'price': 29.99
        }
        response = self.client.post(reverse('product_creation'), data=new_product, follow=True)
        self.assertEqual(response.status_code, 200)

        # Verify if the new product is in the product list
        self.assertContains(response, new_product['name'])
        self.assertContains(response, new_product['description'])
        self.assertContains(response, new_product['price'])

    def test_product_update(self):
        updated_product = {
            'name': 'Updated Product',
            'description': 'This is an updated product.',
            'price': 39.99
        }
        url = reverse('product_update', args=[self.product1.pk])
        response = self.client.post(url, data=updated_product, follow=True)
        self.assertEqual(response.status_code, 200)

        # Verify if the product details have been updated
        self.assertContains(response, updated_product['name'])
        self.assertContains(response, updated_product['description'])
        self.assertContains(response, updated_product['price'])

    def test_product_delete(self):
        url = reverse('product_delete', args=[self.product2.pk])
        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)

        # Verify if the product has been deleted
        self.assertNotContains(response, self.product2.name)
        self.assertNotContains(response, self.product2.description)
        self.assertNotContains(response, str(self.product2.price))

    def test_invalid_product_creation(self):
        invalid_data = {
            'name': 'Invalid Product',
            'description': 'This is an invalid product.',
            'price': 'abc'  # Invalid price format
        }
        response = self.client.post(reverse('product_creation'), data=invalid_data)
        self.assertEqual(response.status_code, 200)

        # Verify if form validation errors are displayed
        self.assertFormError(response, 'form', 'price', 'Enter a number.')

    def test_invalid_product_update(self):
        invalid_data = {
            'name': '',
            'description': 'This is an invalid product.',
            'price': 99.99
        }
        url = reverse('product_update', args=[self.product1.pk])
        response = self.client.post(url, data=invalid_data)
        self.assertEqual(response.status_code, 200)

        # Verify if form validation errors are displayed
        self.assertFormError(response, 'form', 'name', 'This field is required.')
