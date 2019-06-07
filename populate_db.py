from models import *
from mongoengine import *


def reset_db(*documents):
    for doc in documents:
        doc.objects.delete()


reset_db(User, Post)


ross = User(email='ross@friends.com', first_name='Ross',
            last_name='Lawley').save()

john = User(email='john@friends.com', first_name='John',
            last_name='Bawler').save()


post1 = TextPost(title='Fun with MongoEngine', author=john)
post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
post1.tags = ['mongodb', 'mongoengine']
post1.save()

post2 = LinkPost(title='MongoEngine Documentation', author=ross)
post2.link_url = 'http://docs.mongoengine.com/'
post2.tags = ['mongoengine']
post2.save()


print(User.objects.count())
print(Post.objects.count())

users = User.objects.all()

result = [{user.email: user.first_name} for user in users]

print(result)


class Query(QuerySet):

    def get_all_users():
        return User.objects.all()

    def get_user_where_first_name_is(name):
        return User.objects(first_name__exact=name)


for user in Query.get_user_where_first_name_is('Ross'):
    print(user.first_name, user.last_name, user.email)
