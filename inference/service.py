from logging import log, error
from grifon.recommendation.schema import CreateUserRecommendationMessage

from ..config import settings
from .model.abstract_model import AbstractModel


class RecommenderService:
    model: AbstractModel

    def __init__(self):
        self.model = getattr(__import__(f'.model.{settings.version}'), 'Model')()

    def handle_create_user_recommendation_message(self, message: CreateUserRecommendationMessage):
        try:
            log(0, f'Creating recommendations for message: {message}')

            self.model.predict(message.embedding)

            log(0, f'Successfully generated recommendations for message: {message}')
        except Exception as e:
            error(e)


if __name__ == '__main__':
    service = RecommenderService()
    service.handle_create_user_recommendation_message(
        CreateUserRecommendationMessage(
            embedding=[0, 0, 0],
        )
    )
