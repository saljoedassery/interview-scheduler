from collections import namedtuple

from scheduler.models import CustomUser

UserModel = namedtuple("User", ["username", "password", "email", "role"])
users_list = [
    UserModel("john", "john123", "john@gmail.com", "candidate"),
    UserModel("smith", "smith123", "smith@gmail.com", "interviewer"),
    UserModel("mariya", "mariya123", "mariya@gmail.com", "interviewer"),
    UserModel("julia", "julia123", "julia@gmail.com", "hr")
]


def create_users():
    for user in users_list:
        u, created = CustomUser.objects.get_or_create(username=user.username,
                                                      defaults={"password": user.password, "email": user.email,
                                                                "role": user.role})
        if created:
            u.set_password(user.password)
            u.save()
