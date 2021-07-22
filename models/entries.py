class Entries:
    """Class for creating an entries dictonary"""

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, time, concept, entry, mood_id):
        self.id = id
        self.time = time
        self.concept = concept
        self.entry = entry
        self.mood_id = mood_id
        self.mood = None
