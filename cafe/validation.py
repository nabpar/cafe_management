from django.core.validators import FileExtensionValidator, RegexValidator

# for the alphabet vlidations
isalphavalidator = RegexValidator(
    "^[a-z- A-z]+$",
    message="Invalid data format. Only alphabetic are allowed.",
    code="Invalid name",
)

# fro the alphanumerical validations.
isalphanumericalvalidator = RegexValidator(
    "^[a-z- A-z 0-9]+$",
    message="Invalid data format. Only letters, numbers, and hyphens are allowed.",
    code="Invalide name",
)

# for the contact validations
iscontactvalidator = RegexValidator(
    "((98)|(97))(\d){8}",
    message="Please enter a valid Nepali phone number starting with '98' or '97' and consisting of 10 digits.",
)
