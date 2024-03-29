import random
__all__ = 'IdGenerator',


class IdGenerator:
    def __init__(self, seed=None):
        self.seed = seed if seed is not None else random.getrandbits(8)

    def set_seed(self, seed):
        self.seed = seed
        return self

    def get_id(self):
        seed, self.seed = str(self.seed), self.seed + 1

        return seed

    def __call__(self, *args, **kwargs):
        return self.get_id()

