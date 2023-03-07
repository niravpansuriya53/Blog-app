from django.test import TestCase
from myapp.models import Author, Blog, Comment
from datetime import date
from django.urls import reverse


# test case for author model
class AuthorModelTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='John Doe', birthdate=date(
            1990, 1, 1), about_author='Lorem ipsum dolor sit amet.')

    def test_author_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_author_birthdate_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('birthdate').verbose_name
        self.assertEqual(field_label, 'birthdate')

    def test_author_about_author_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('about_author').verbose_name
        self.assertEqual(field_label, 'about author')

    def test_author_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_author_birthdate(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.birthdate, date(1990, 1, 1))

    def test_author_about_author(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.about_author, 'Lorem ipsum dolor sit amet.')

    def test_author_object_name(self):
        author = Author.objects.get(id=1)
        get_object_name = author.name
        self.assertEqual(get_object_name, str(author))


# test vase for blog model
class BlogModelTestCase(TestCase):

    @classmethod
    def setUpTestData(self):
        self.author = Author.objects.create(name='John Doe', birthdate='1990-01-01',
                                            about_author='Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        self.blog = Blog.objects.create(author=self.author, title='Test blog post',
                                        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

    def test_blog_title_lable(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_blog_content_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("content").verbose_name
        self.assertEqual(field_label, "content")

    def test_blog_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field("title").max_length
        self.assertEqual(max_length, 70)

    def test_blog_content(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(
            blog.content, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

    def test_blog_object_name(self):
        blog = Blog.objects.get(id=1)
        get_object_name = f"{blog.author} - {blog.title}"
        self.assertEqual(get_object_name, str(blog))

    def test_blog_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        self.assertEquals(blog.get_absolute_url(), "/blog/blogs/")


# test case for comment model
class CommentModelTestCase(TestCase): 

    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(name='John Doe', birthdate='1990-01-01',
                                       about_author='Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        blog = Blog.objects.create(author=author, title='Test blog post',
                                   content='Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        cls.comment = Comment.objects.create(comment="Nice !!", blog=blog)
        cls.comment = Comment.objects.create(comment="Godd !!", blog=blog)

    def test_comment_content_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field("comment").verbose_name
        self.assertEqual(field_label, "comment")

    def test_blog_content(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(
            blog.content, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

    def test_comment_object_name(self):
        comment = Comment.objects.get(id=1)
        get_object_name = f"{comment.blog.author} - {comment.blog.title} "
        self.assertEqual(get_object_name, str(comment))

    def test_comment_get_absolute_url(self):
        comment = Comment.objects.get(id=1)
        self.assertEquals(comment.get_absolute_url(), "/blog/1/")


# test case for bloglist
class BlogListView(TestCase):

    @classmethod
    def setUpTestData(cls):
        number = 10
        for blog in range(0, number):
            author = Author.objects.create(name='John Doe', birthdate='1990-01-01',
                                           about_author='Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
            Blog.objects.create(
                title=f"Test Blog {blog}", author=author, content=f"Test Blog {blog}",)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/blog/blogs/")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("main:bloglist"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "myapp/blog_list.html")

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("main:bloglist"))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_fiv(self):
        response = self.client.get(reverse('main:bloglist'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blog_list']), 5)
