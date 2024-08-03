def add_dot(character, trait, maximum):
    trait_value = getattr(character, trait, None)
    if trait_value is not None and trait_value < maximum:
        setattr(character, trait, trait_value + 1)
        character.save()
        return True
    return False
