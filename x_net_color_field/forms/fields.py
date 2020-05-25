import re

from django.core import exceptions
from django.forms import (
    fields,
)


###############################################################################
# COLOR

class ColorField(fields.CharField):
    default_error_messages = {
        "invalid": "Enter a valid color value: e.g. \"#FF0022\"",
    }

    def clean(self, *args, **kwargs):
        data = super().clean(*args, **kwargs)

        if not re.match("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", data):
            raise exceptions.ValidationError(
                self.error_messages["invalid"],
                code="invalid",
            )

        return data
