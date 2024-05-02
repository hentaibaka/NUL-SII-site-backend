from django.contrib.auth.models import User 


User.objects.create_superuser('superuser', 'admin@example.com', 'superuser')

