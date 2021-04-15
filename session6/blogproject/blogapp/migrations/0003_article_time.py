from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]