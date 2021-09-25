from django.db import models
from django.core.validators import validate_comma_separated_integer_list


class Evident(models.Model):
    input_values = models.CharField(validators=[
                                    validate_comma_separated_integer_list], max_length=200, blank=True, null=True, default='')
    start_datetime = models.DateTimeField('Start Date', null=True, blank=True)
    end_datetime = models.DateTimeField('End Date', null=True, blank=True)

    def __str__(self):
        """String for representing the model object."""
        return self.input_values
