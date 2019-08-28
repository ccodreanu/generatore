def slug_creator(weird_string):
    """
    This creates slugs starting in the ASCII character space.
    """
    slug = weird_string.encode('ascii', 'ignore').lower().decode()
    slug = slug.replace(' ', '-')

    return slug
