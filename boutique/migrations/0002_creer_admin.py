from django.db import migrations

def creer_admin(apps, schema_editor):
    from django.contrib.auth.models import User
    if not User.objects.filter(username='aicha').exists():
        User.objects.create_superuser(
            username='aicha',
            email='aicha@gmail.com',
            password='Delice2026!'
        )

class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(creer_admin),
    ]