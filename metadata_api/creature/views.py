import random

from django.http import JsonResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist

from .utils import add_attribute, compose_image
from .models import Token, Contract


def creature(request, token_id):
    token = Token(token_id=token_id)

    token.first_name = random.choice(Token.FIRST_NAMES)
    token.last_name = random.choice(Token.LAST_NAMES)
    token.description = 'Friendly OpenSea Creature that enjoys long swims in the ocean.'

    base = random.choice(Token.BASES)
    eyes = random.choice(Token.EYES)
    mouth = random.choice(Token.MOUTH)
    token.image = compose_image(
        [
            'images/bases/base-%s.png' % base,
            'images/eyes/eyes-%s.png' % eyes,
            'images/mouths/mouth-%s.png' % mouth,
        ],
    )

    token.save()

    attributes = []
    add_attribute(attributes, 'Base', Token.BASES, token_id)
    add_attribute(attributes, 'Eyes', Token.EYES, token_id)
    add_attribute(attributes, 'Mouth', Token.MOUTH, token_id)
    add_attribute(attributes, 'Level', Token.INT_ATTRIBUTES, token_id)
    add_attribute(attributes, 'Stamina', Token.FLOAT_ATTRIBUTES, token_id)
    add_attribute(attributes, 'Personality', Token.STR_ATTRIBUTES, token_id)
    add_attribute(attributes, 'Aqua Power', Token.BOOST_ATTRIBUTES, token_id, display_type='boost_number')
    add_attribute(attributes, 'Stamina Increase', Token.PERCENT_BOOST_ATTRIBUTES, token_id, display_type='boost_percentage')
    add_attribute(attributes, 'Generation', Token.NUMBER_ATTRIBUTES, token_id, display_type='number')

    return JsonResponse({
        'name': token.full_name,
        'description': token.description,
        'image': token.image.url,
        'external_url': 'http://127.0.0.1:8000/%s' % token_id,
        'attributes': attributes
    })


def creature_box(request, token_id):
    token = Token(token_id=token_id)

    token.first_name = 'Creature Loot Box'
    token.description = 'This lootbox contains some OpenSea Creatures! It can also be traded!'
    token.image = compose_image(
        ['images/box/lootbox.png'],
    )

    token.save()

    attributes = []
    add_attribute(attributes, 'number_inside', [3], token_id)

    return JsonResponse({
        'name': token.full_name,
        'description': token.description,
        'image': token.image.url,
        'external_url': 'http://127.0.0.1:8000/%s' % token_id,
        'attributes': attributes
    })


def creature_factory(request, token_id):
    token = Token(token_id=token_id)
    attributes = []

    if token_id == 0:
        token.first_name = 'One OpenSea creature'
        token.description = 'When you purchase this option, you will receive a single OpenSea creature of a random variety. ' \
                            'Enjoy and take good care of your aquatic being!'
        token.image = compose_image(
            ['images/factory/egg.png'],
        )
        add_attribute(attributes, 'number_inside', [1], token_id)
    elif token_id == 1:
        token.first_name = 'Four OpenSea creatures'
        token.description = 'When you purchase this option, you will receive four OpenSea creatures of random variety. ' \
                            'Enjoy and take good care of your aquatic beings!'
        token.image = compose_image(
            ['images/factory/four-eggs.png'],
        )
        add_attribute(attributes, 'number_inside', [4], token_id)
    elif token_id == 2:
        token.first_name = 'One OpenSea creature lootbox'
        token.description = 'When you purchase this option, you will receive one lootbox, which can be opened to reveal three ' \
                            'OpenSea creatures of random variety. Enjoy and take good care of these cute aquatic beings!'
        token.image = compose_image(
            ['images/box/lootbox.png'],
        )
        add_attribute(attributes, 'number_inside', [3], token_id)

    token.save()

    return JsonResponse({
        'name': token.full_name,
        'description': token.description,
        'image': token.image.url,
        'external_url': 'http://127.0.0.1:8000/%s' % token_id,
        'attributes': attributes
    })


def accessory(request, token_id):
    try:
        token = Token.objects.get(token_id=token_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No such token')

    attributes = []
    add_attribute(attributes, 'Aqua Boost', Token.ACCESSORIES_ATTS_INT, token_id, display_type='boost_number')
    add_attribute(attributes, 'Stamina Increase', Token.ACCESSORIES_ATTS_PERCENT, token_id, display_type='boost_percentage')
    add_attribute(attributes, 'Location', Token.ACCESSORIES_ATTS_LOCATION, token_id)
    add_attribute(attributes, 'Depth', Token.ACCESSORIES_ATTS_DEPTH, token_id)
    add_attribute(attributes, 'Rarity', Token.ACCESSORIES_ATTS_RARITY, token_id)
    add_attribute(attributes, 'Generation', Token.ACCESSORIES_ATTS_GENERATION, token_id, display_type='number')

    accessory_name = Token.ACCESSORIES_NAMES[token_id]

    return JsonResponse({
        'name': accessory_name,
        'description': 'A fun and useful accessory for your friendly OpenSea creatures.',
        'image': token.image.url,
        'external_url': 'http://127.0.0.1:8000/accessory/%s' % token_id,
        'attributes': attributes
    })


def accessory_box(request, token_id):
    token = Token(token_id=token_id)

    token.first_name = 'Accessory Loot Box'
    token.description = 'This lootbox contains some OpenSea Creature accessories! It can also be traded!'
    token.image = compose_image(
        ['images/box/lootbox.png'],
    )
    token.save()

    attributes = []
    add_attribute(attributes, 'number_inside', [3], token_id)

    return JsonResponse({
        'name': token.full_name,
        'description': token.description,
        'image': token.image.url,
        'external_url': 'http://127.0.0.1:8000/box/accessory/%s' % token_id,
        'attributes': attributes
    })


def accessory_factory(request, token_id):
    token = Token(token_id=token_id)
    attributes = []

    if token_id == 0:
        token.first_name = 'One OpenSea creature accessory'
        token.description = 'When you purchase this option, you will receive a single OpenSea creature accessory of a random variety. ' \
                      'Enjoy and take good care of your aquatic being!'
        token.image = compose_image(
            ['images/factory/egg.png'],
        )
        add_attribute(attributes, 'number_inside', [1], token_id)
    elif token_id == 1:
        token.first_name = 'Four OpenSea creature accessories'
        token.description = 'When you purchase this option, you will receive four OpenSea creature accessories of random variety. ' \
                      'Enjoy and take good care of your aquatic beings!'
        token.image = compose_image(
            ['images/factory/four-eggs.png'],
        )
        add_attribute(attributes, 'number_inside', [4], token_id)
    elif token_id == 2:
        token.first_name = 'One OpenSea creature accessory lootbox'
        token.description = 'When you purchase this option, you will receive one lootbox, which can be opened to reveal three ' \
                      'OpenSea creature accessories of random variety. Enjoy and take good care of these cute aquatic beings!'
        token.image = compose_image(
            ['images/box/lootbox.png'],
        )
        add_attribute(attributes, 'number_inside', [3], token_id)

    token.save()

    return JsonResponse({
        'name': token.full_name,
        'description': token.description,
        'image': token.image.url,
        'external_url': 'http://127.0.0.1:8000/%s' % token_id,
        'attributes': attributes
    })


def contract(request, contract_name):
    if contract_name not in Contract.CONTRACT_URI_METADATA_AVAILABLE:
        HttpResponseNotFound('Resource not found')
    return JsonResponse(Contract.CONTRACT_URI_METADATA[contract_name])
