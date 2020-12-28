import os 
from celery import Celery 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') 

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')   
# Load tasks from all registered apps 
app.autodiscover_tasks()