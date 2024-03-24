from faust import App
from grifon.video_analysis.schema import VideoAnalyseMessage
from config import settings


app = App('my_faust_service', broker='kafka://localhost:9092')

input_video_analise = app.topic(settings.VIDEO_ANALYSIS_TOPIC, value_type=VideoAnalyseMessage)

output_recommendation = app.topic(settings.RECOMMENDATION_TOPIC, value_type=VideoAnalyseMessage)
