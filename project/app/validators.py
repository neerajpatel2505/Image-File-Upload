from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os
from django.core.exceptions import ValidationError

def validate_file(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path + filename
    supported_extensions = ['.pdf','.docx']
    if ext.lower() not in supported_extensions:
        raise ValidationError(_('Unsupported file extension. Only PDF files are allowed.'))

    file_size = value.size
    max_file_size = 5 * 1024 * 1024  # 5 MB
    if file_size > max_file_size:
        raise ValidationError(_('The maximum file size that can be uploaded is 5MB.'))

def validate_image(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path + filename
    supported_extensions = ['.jpg' , '.jpeg', '.png']
    if ext.lower() not in supported_extensions:
        raise ValidationError(_('Unsupported file extension. Only .jpg, .jpeg, .png images are allowed.'))

    file_size = value.size
    max_image_size = 1 * 1024 * 1024  # 5 MB  
    if file_size > max_image_size:
        raise ValidationError(_('The maximum image size that can be uploaded is 1MB.'))