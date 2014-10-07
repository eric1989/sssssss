import datetime
from mongoengine import *
from mongoengine.django.auth import User as Mongoengine_user
from django.utils.translation import ugettext_lazy as _
from config.settings import DBNAME

connect(DBNAME)

USERNAME_REGEX = r'[\w.@+-]+'
CONFIRMATION_TOKEN_VALIDITY = 5 # days
EDU_DOMAIN = 'edu'

class EmailConfirmationToken(EmbeddedDocument):
    value = StringField(max_length=20, required=True)
    created_time = DateTimeField(default=lambda: timezone.now(), required=True)

    def check_token(self, confirmation_token):
        if confirmation_token != self.value:
            return False
        elif (timezone.now() - self.created_time).days > CONFIRMATION_TOKEN_VALIDITY:
            return False
        else:
            return True

class User(Mongoengine_user):
    username = StringField(
        max_length=30,
        min_length=4,
        regex=r'^' + USERNAME_REGEX + r'$',
        required=True,
        verbose_name=_("username"),
        help_text=_("Minimal of 4 characters and maximum of 30. Letters, digits and @/./+/-/_ only."),
    )
    is_student = BooleanField(default=False);
    email_confirmed = BooleanField(default=False);
    email_confirmation_token = BooleanField();

    meta = {
        'allow_inheritance': True,
        'indexes': [
            {'fields': ['email'], 'unique': True}
        ]
    }

    @classmethod
    def create_user(self, username, email, password):
        now = datetime.datetime.now()
        is_student = False
        if not email:
            raise ValueError("The given email must be set")
		# Normalize the address by lowercasing the domain part of the email
        # address.
        try:
            email_name, domain_part = email.strip().split('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        domain_name, domain_type = domain_part.strip().split('.',1)
        if (domain_type == EDU_DOMAIN):
            is_student = True
        user = self(
            username=username,
            email=email,
            is_staff=False,
            is_active=True,
            is_superuser=False,
            is_student=is_student,
            last_login=now,
            date_joined=now,
        )
        user.set_password(password)
        user.save()
        return user


