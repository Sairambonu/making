from django.db import models

# Create your models here.

# class AnnotateLanguageUsers(models.Model):
# 	sno = models.AutoField(primary_key=True)
# 	email = models.EmailField()
# 	language = models.CharField(max_length=100)

class AnnotateLanguageUsers(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'your_table_name'
        unique_together = (('email', 'lang'),)

class Datasets(models.Model):
	sno = models.AutoField(primary_key=True)
	dataset_path = models.TextField()
	language = models.CharField(max_length=20)
	task_name = models.CharField(max_length=50)
	set_name = models.CharField(max_length=20)
	user_email = models.CharField(max_length=50)
	deadline = models.DateTimeField(blank=True, null=True)
	last_updated = models.DateTimeField(blank=True, null=True)
	status = models.CharField(max_length=10)

	def __str__(self):
		return self.dataset_path