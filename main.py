from logging import info

import asyncio
import pickle

from config import settings as local_settings
from grifon.config import settings
from grifon.mqbroker.kafka_client import KafkaClient
from grifon.recommendation.schema import CreateUserRecommendationMessage, UserRecommendationMessage
from inference.model import Model

kafka_client = KafkaClient("localhost:9092")

# Сетапим модель
with open(f'./recommendation/{local_settings.version}.pickle', 'rb') as file:
    model: Model = pickle.load(file)


@kafka_client.register_topic_handler(settings.RECOMMENDATION_REQUEST_TOPIC, msg_class=CreateUserRecommendationMessage)
async def handle_create_user_recommendation_message(create_message: CreateUserRecommendationMessage):
    info(f'Creating recommendations: {create_message}')

    recommendations = model.get_recommendations(create_message.user_id)   # пока без параметров

    user_recommendation_message = UserRecommendationMessage(
        user_id=create_message.user_id,
        cash_register_id=create_message.cash_register_id,
        recommendations=recommendations
    )
    kafka_client.send_message(settings.RECOMMENDATION_RESPONSE_TOPIC, user_recommendation_message)
    kafka_client.flush()

    info(f'Recommendations generated: {create_message}')


async def main():
    await kafka_client.start_handling()

if __name__ == '__main__':
    asyncio.run(main())
