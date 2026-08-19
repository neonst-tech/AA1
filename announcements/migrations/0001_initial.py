from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Announcement",
            fields=[
                (
                    "id",
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("title", models.CharField(max_length=200)),
                ("department", models.CharField(max_length=100)),
                ("summary", models.TextField()),
                ("content", models.TextField()),
                ("publish_date", models.DateField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-publish_date", "-created_date"],
            },
        ),
    ]
