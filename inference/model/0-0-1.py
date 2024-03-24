import pickle
from lightfm import LightFM

from .abstract_model import AbstractModel


class Model(AbstractModel):
    model: LightFM

    def __init__(self):
        with open('learning/artifacts/0-0-1', 'rb') as file:
            self.model = pickle.load(file)

    def predict(self, embedding):
        self.model.predict()
