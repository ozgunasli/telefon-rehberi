from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return "{0}".format(self.name)


class Guide(models.Model):
    firstname = models.CharField(verbose_name="Firstname", max_length=20)
    lastname = models.CharField(verbose_name="Lastname", max_length=20)
    pnumber = models.IntegerField(default=0, unique=True)
    email = models.EmailField(verbose_name="Email", max_length=100)
    group = models.ForeignKey(
        Group,
        verbose_name="Group",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{firstname} {lastname}'.format(
            firstname=self.firstname,
            lastname=self.lastname
        )