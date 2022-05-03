from io import BytesIO
from PIL import Image

from django.core.files.uploadedfile import InMemoryUploadedFile


def add_attribute(existing, attribute_name, options, token_id, display_type=None):
    trait = {
        'trait_type': attribute_name,
        'value': options[token_id % len(options)]
    }
    if display_type:
        trait['display_type'] = display_type
    existing.append(trait)


def compose_image(image_files):
    composite = None
    for image_file in image_files:
        foreground = Image.open(image_file).convert('RGBA')

        if composite:
            composite = Image.alpha_composite(composite, foreground)
        else:
            composite = foreground

    # Create a file-like object to write thumb data (thumb data previously created
    # using PIL, and stored in variable 'thumb')
    thumb_io = BytesIO()
    composite.save(thumb_io, format='PNG')

    # Create a new Django file-like object to be used in models as ImageField using
    # InMemoryUploadedFile.  If you look at the source in Django, a
    # SimpleUploadedFile is essentially instantiated similarly to what is shown here
    file = InMemoryUploadedFile(
        field_name='',
        name='img.png',
        content_type='img/png',
        file=thumb_io,
        size=None,
        charset=None,
    )

    return file
