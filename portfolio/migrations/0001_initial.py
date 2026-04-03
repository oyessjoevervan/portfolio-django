from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('career_goals', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('github', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('behance', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile/')),
            ],
            options={'verbose_name': 'Profile'},
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(
                    choices=[
                        ('design_tools', 'Design Tools'),
                        ('uiux', 'UI/UX Design'),
                        ('other', 'Other'),
                    ],
                    default='design_tools', max_length=20)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order', 'name']},
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('technologies', models.CharField(help_text='Comma-separated list of tools/technologies', max_length=300)),
                ('github_link', models.URLField(blank=True)),
                ('live_link', models.URLField(blank=True)),
                ('behance_link', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('order', models.IntegerField(default=0)),
                ('featured', models.BooleanField(default=False)),
            ],
            options={'ordering': ['order', 'title']},
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('field_of_study', models.CharField(blank=True, max_length=200)),
                ('year_start', models.IntegerField()),
                ('year_end', models.IntegerField(blank=True, help_text='Leave blank if currently enrolled', null=True)),
                ('description', models.TextField(blank=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order', '-year_start']},
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={'ordering': ['-sent_at']},
        ),
    ]
