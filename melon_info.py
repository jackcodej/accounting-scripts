"""Print out all the melons in our inventory."""


from melons import melons

def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, melon_attributes in melons.items():
        print(melon_name.upper())

        for attribute, value in melon_attributes.items():
            print(f"{attribute}: {value}")

print_melon(melons)