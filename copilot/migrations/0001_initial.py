# Generated by Django 5.0.3 on 2024-05-28 03:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Authors",
            fields=[
                (
                    "authorid",
                    models.AutoField(
                        db_column="AuthorID", primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(db_column="Name", max_length=255)),
                (
                    "birthdate",
                    models.DateField(blank=True, db_column="Birthdate", null=True),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, db_column="Country", max_length=100, null=True
                    ),
                ),
            ],
            options={
                "db_table": "authors",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Books",
            fields=[
                (
                    "bookid",
                    models.AutoField(
                        db_column="BookID", primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(db_column="Title", max_length=255)),
                (
                    "publishedyear",
                    models.TextField(blank=True, db_column="PublishedYear", null=True),
                ),
                (
                    "genre",
                    models.CharField(
                        blank=True, db_column="Genre", max_length=100, null=True
                    ),
                ),
            ],
            options={
                "db_table": "books",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Loans",
            fields=[
                (
                    "loanid",
                    models.AutoField(
                        db_column="LoanID", primary_key=True, serialize=False
                    ),
                ),
                ("loandate", models.DateField(db_column="LoanDate")),
                (
                    "returndate",
                    models.DateField(blank=True, db_column="ReturnDate", null=True),
                ),
            ],
            options={
                "db_table": "loans",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Members",
            fields=[
                (
                    "memberid",
                    models.AutoField(
                        db_column="MemberID", primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(db_column="Name", max_length=255)),
                (
                    "email",
                    models.CharField(db_column="Email", max_length=255, unique=True),
                ),
                ("joindate", models.DateField(db_column="JoinDate")),
            ],
            options={
                "db_table": "members",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "userid",
                    models.BigAutoField(
                        db_column="UserID", primary_key=True, serialize=False
                    ),
                ),
                ("username", models.CharField(db_column="Username", max_length=255)),
                ("password", models.CharField(db_column="Password", max_length=255)),
                ("email", models.CharField(db_column="Email", max_length=255)),
                ("role", models.CharField(db_column="Role", max_length=6)),
            ],
            options={
                "db_table": "users",
                "managed": False,
            },
        ),
    ]
