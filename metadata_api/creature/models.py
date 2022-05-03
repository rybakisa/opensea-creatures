from django.db import models


class Contract(models.Model):
    CONTRACT_URI_METADATA = {
        'opensea-creatures': {
            'name': 'OpenSea Creatures',
            'description': 'Friendly creatures of the sea.',
            'image': 'https://example.com/image.png',
            'external_link': 'https://github.com/ProjectOpenSea/opensea-creatures/'
        },
        'opensea-erc1155': {
            'name': 'OpenSea Creature Accessories',
            'description': "Fun and useful accessories for your OpenSea creatures.",
            'image': 'https://example.com/image.png',
            'external_link': 'https://github.com/ProjectOpenSea/opensea-erc1155/'
        }
    }
    CONTRACT_URI_METADATA_AVAILABLE = CONTRACT_URI_METADATA.keys()


class Token(models.Model):
    FIRST_NAMES = ['Herbie', 'Sprinkles', 'Boris', 'Dave', 'Randy', 'Captain']
    LAST_NAMES = ['Starbelly', 'Fisherton', 'McCoy']

    BASES = ['jellyfish', 'starfish', 'crab', 'narwhal', 'tealfish', 'goldfish']
    EYES = ['big', 'joy', 'wink', 'sleepy', 'content']
    MOUTH = ['happy', 'surprised', 'pleased', 'cute']

    INT_ATTRIBUTES = [5, 2, 3, 4, 8]
    FLOAT_ATTRIBUTES = [1.4, 2.3, 11.7, 90.2, 1.2]
    STR_ATTRIBUTES = [
        'Happy',
        'Sad',
        'Sleepy',
        'Boring'
    ]
    BOOST_ATTRIBUTES = [10, 40, 30]
    PERCENT_BOOST_ATTRIBUTES = [5, 10, 15]
    NUMBER_ATTRIBUTES = [1, 2, 1, 1]

    ACCESSORIES_IMAGES = [
        'Bamboo-flute.png',
        'Life-ring.png',
        'Message-in-a-bottle.png',
        'Pearl.png',
        'Scuba-mask.png',
        'Trident.png',
    ]
    ACCESSORIES_NAMES = [
        a.replace('-', ' ').replace('.png', '')
        for a in ACCESSORIES_IMAGES
    ]
    ACCESSORIES_ATTS_INT = [200, 11, 3, 41, 9, 172]
    ACCESSORIES_ATTS_PERCENT = [5, 10, 1, 20, 15, 25]
    ACCESSORIES_ATTS_LOCATION = ['Head', 'Body', 'Held', 'Held', 'Head', 'Held']
    ACCESSORIES_ATTS_RARITY = [
        'Common',
        'Rare',
        'Legendary',
        'Epic',
        'Divine',
        'Hidden',
    ]
    ACCESSORIES_ATTS_DEPTH = [
        'beach',
        'shore',
        'shallows',
        'deeps',
        'shore',
        'deeps',
    ]
    ACCESSORIES_ATTS_GENERATION = [1, 1, 2, 1, 1, 3]

    token_id = models.IntegerField(
        unique=True,
        null=False,
    )
    first_name = models.CharField(
        max_length=255,
        blank=False,
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
    )
    description = models.TextField()
    image = models.ImageField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name
