from django.forms import ModelForm
from .models import Robot

class RobotUploadForm(ModelForm):
    class Meta:
        model = Robot
        fields = ['team_number', 'year', 'name', 'image', 'image2', 'image3', 'image4', 'image5']
        
