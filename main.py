from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from env import API_KEY


class IbmWatsonHelper():
    ASSISTANT_VERSION = "2021-06-14"

    ASSISTANT_SERVICE_URL = 'https://api.us-east.assistant.watson.cloud.ibm.com'

    def __init__(self):
        self.assistant = self.get_ibm_assistant_v2()

    def get_ibm_assistant_v2(self) -> AssistantV2:
        authenticator = IAMAuthenticator(API_KEY)
        assistant = AssistantV2(
            version=self.ASSISTANT_VERSION,
            authenticator=authenticator
        )

        assistant.set_service_url(self.ASSISTANT_SERVICE_URL)
        return assistant

ibm_watson_helper = IbmWatsonHelper()
