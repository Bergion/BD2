import psycopg2
from Application.Models.Customuser import Customuser
from Application.Models.Blog import Blog
from Application.Models.Post import Post
from Application.Models.Rate import Rate
from Application.settings import CONNECTION_STRING, SEED_USERS, SEED_BLOGS, SEED_POSTS, SEED_RATES
from faker import Faker
from faker.providers import profile, lorem, python, date_time
import time
import random

fake = Faker()
fake.add_provider(profile)
fake.add_provider(lorem)
fake.add_provider(python)
fake.add_provider(date_time)

class StartController():
    @staticmethod
    def get_tables_list():
        with psycopg2.connect(CONNECTION_STRING) as connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute("""SELECT table_name FROM information_schema.tables
                        WHERE table_schema = 'public'""")
                except psycopg2.Error as e:
                    return e.pgerror
                return cursor.fetchall()

    @staticmethod
    def seed_data():
        users = StartController.create_users()
        blogs = StartController.create_blogs(users[0:SEED_BLOGS])
        posts = StartController.create_posts(blogs)
        StartController.create_rates(users, posts)

    @staticmethod 
    def create_users():

        user_table = Customuser()
        i = 0
        ids = []
        while(i < SEED_USERS):
            fake_profile = fake.profile(fields=None, sex=None)
            name = fake_profile['name'].split(' ')
            id = fake.pyint(min=0, max=9999, step=1)
            ids.append(id)
            data = {
                'id': id,
                'password': fake.pystr(min_chars=None, max_chars=20),
                'is_superuser': random.choice(('f', 't')),
                'username': fake_profile['username'],
                'first_name': name[0],
                'last_name': name[1],
                'email': fake_profile['mail']
            }
            status = user_table.create_single(**data)
            if status == 'Created':
                i += 1
        return ids
    
    @staticmethod 
    def create_blogs(users):

        blog_table = Blog()
        i = 0
        ids = []
        while(i < SEED_BLOGS):
            id = fake.pyint(min=0, max=9999, step=1)
            ids.append(id)
            data = {
                'id': id,
                'name': fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None),
                'created': fake.iso8601(tzinfo=None, end_datetime=None), 
                'user_id': users[i]
            }
            status = blog_table.create_single(**data)
            if status == 'Created':
                i += 1
        return ids

    @staticmethod
    def create_posts(blogs):
        post_table = Post()
        i = 0
        ids = []
        while(i < SEED_POSTS):
            id = fake.pyint(min=0, max=9999, step=1)
            ids.append(id)
            data = {
                'id': id,
                'title': fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None),
                'content': fake.text(max_nb_chars=200, ext_word_list=None),
                'pub_date': fake.iso8601(tzinfo=None, end_datetime=None), 
                'blog_id': random.choice(blogs)
            }
            status = post_table.create_single(**data)
            if status == 'Created':
                i += 1
        return ids

    @staticmethod
    def create_rates(users, posts):
        rate_table = Rate()
        i = 0
        while(i < SEED_RATES):
            data = {
                'id': fake.pyint(min=0, max=9999, step=1),
                'value': random.choice(('L', 'D')),
                'user_id': random.choice(users),
                'post_id': random.choice(posts)
            }
            status = rate_table.create_single(**data)
            if status == 'Created':
                i += 1
