from django.test import TestCase
from django.urls import reverse

from .models import Book


# Create your tests here.

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="TestingBook2",
            subtitle="PHP_for_rookies",
            author="Davlatbek Ushurbakiev",
            isbn="12345678990"
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "TestingBook2")
        self.assertEqual(self.book.subtitle, "PHP_for_rookies")
        self.assertEqual(self.book.author, "Davlatbek Ushurbakiev")
        self.assertEqual(self.book.isbn, "12345678990")

    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestingBook")
        self.assertTemplateUsed(response, "books/book_list.html")
