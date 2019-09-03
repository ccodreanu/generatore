import re


def slug_creator(weird_string):
    """
    This creates slugs in the ASCII character space.
    """
    slug = weird_string.encode('ascii', 'ignore').lower().decode()
    slug = slug.replace(' ', '-')
    slug = re.sub(r'!|,|\*|\?|\.', r'', slug)

    return slug
