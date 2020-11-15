# モジュール

"""
# import user
# from user import AdminUser
という書き方もできるが、それより次の通りに書くといい。
"""
from user import AdminUser, User

"""
そうすると、
# bob = user.AdminUser("bob", 23)
のように書く必要がなくなる。
"""
bob = AdminUser("bob", 23)

tom = User("tom")

print(bob.name)
bob.say_hi()
bob.say_hello()