import uuid
import logging
from django.db import models
from django.conf import settings
from django.core.validators import MaxLengthValidator
from django.template import loader
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import transaction
from django.core.mail import EmailMessage
from easy_thumbnails.fields import ThumbnailerImageField
from premailer import Premailer
log = logging.getLogger('django')


class Permission(models.Model):
    name = models.CharField(_('Name'), max_length=30, unique=True)
    description = models.TextField(
        _("Description"),
        validators=[MaxLengthValidator(255)],
        blank=True
    )

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(_('Name'), max_length=30, unique=True)
    permissions = models.ManyToManyField(Permission, through='GroupPermission')

    def __str__(self):
        return self.name


class GroupPermission(models.Model):
    group = models.ForeignKey(
        Group,
        verbose_name=_('Group'),
        on_delete=models.CASCADE
    )
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return f'Group: {self.group.name} Permission: {self.permission.name}'


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """ Creates and saves a User with the given email """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """ Creates and saves a superuser with the given email and password. """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save()
        return user


def media_file_path(instance, filename):
    return 'avatar/{0}'.format(uuid.uuid4().hex.upper())


class User(AbstractBaseUser):
    email = models.EmailField(_('Email'), max_length=80, unique=True)
    first_name = models.CharField(_('First Name'), max_length=40, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=80, blank=True)
    is_active = models.BooleanField(_('Is Active'), default=True)
    is_staff = models.BooleanField(_('Is Staff'), default=True)
    is_admin = models.BooleanField(_('Is Admin'), default=False)
    last_login = models.DateTimeField(_('Last Login'), blank=True, null=True),
    full_photo = ThumbnailerImageField(
        _('Full Photo'),
        resize_source=dict(size=(150, 150)),
        upload_to=media_file_path,
        blank=True
    )
    small_photo = ThumbnailerImageField(
        _('Small Photo'),
        resize_source=dict(size=(29, 29)),
        upload_to=media_file_path,
        blank=True
    )
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'.strip()
        elif self.last_name:
            return self.last_name
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def username(self):
        return self.email

    @property
    def is_superuser(self):
        return self.is_admin

    @transaction.atomic
    def save(self):
        old = None
        if self.id is not None:
            old = User.objects.get(pk=self.id)
        super().save()
        if old is None:
            subject = _('New user is created')

            # create the email body with the Premailer (which can handle css also)
            body = Premailer(
                loader.render_to_string(
                    template_name='emails/new_user.html',
                    context={
                        'text': subject,
                        'subject': subject,
                        'email': self.email,
                    }
                )
            ).transform()

            # send the email to notify the admins regarding the new user
            msg = EmailMessage(
                subject=subject,
                body=body,
                to=[settings.ADMIN_EMAIL]
            )
            msg.content_subtype = "html"
            msg.send()

    @staticmethod
    def autocomplete_search_fields():
        return ("email__icontains",)


class UserPermission(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    permission = models.ForeignKey(
        Permission,
        verbose_name=_('Permission'),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'#{self.id} User: {self.user.email} Permission: #{self.permission.name}'


class Membership(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        related_name='membership_user'
    )
    group = models.ForeignKey(Group, verbose_name=_('Group'), on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'group')

    def __str__(self):
        return '%s %s' % (self.user.full_name, self.group.name)
