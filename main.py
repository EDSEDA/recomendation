from logging import info, error
import pickle
import asyncio

from grifon.mqbroker.kafka_client import KafkaClient
from grifon.recommendation.schema import CreateUserRecommendationMessage, UserRecommendationMessage

from config import settings
from recommendation.inference.model import Model

# !!!!!! change me !!!!!!
topic_name = "my_topic"

kafka_client = KafkaClient("localhost:9092")

# Сетапим модель
with open(f'./recommendation/artifacts/{settings.version}.pickle', 'rb') as file:
    model: Model = pickle.load(file)


@kafka_client.register_topic_handler(topic_name)
def handle_create_user_recommendation_message(create_message: CreateUserRecommendationMessage):
    try:
        info(f'Creating recommendations: {create_message}')

        recommendations = model.get_recommendations() # пока без параметров

        user_recommendation_message = UserRecommendationMessage(
            user_id=create_message.user_id,
            cash_register_id=create_message.cash_register_id,
            recommendations=recommendations
        )
        kafka_client.send_message(topic_name, user_recommendation_message)
        kafka_client.flush()

        info(f'Recommendations generated: {create_message}')
    except Exception as e:
        error(e)


async def main():
    await kafka_client.start_handling()

if __name__ == '__main__':
    asyncio.run(main())
