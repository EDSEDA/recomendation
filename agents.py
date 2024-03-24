from topics import app, input_video_analise, output_recommendation
from grifon.video_analysis.schema import VideoAnalyseMessage


@app.agent(input_video_analise)
async def get_person_for_prepare_recommendations(messages):
    async for message in messages:
        processed_message = VideoAnalyseMessage(message)
        await output_recommendation.send(value=processed_message)
