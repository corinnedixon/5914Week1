from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from env import API_KEY

ASSISTANT_ID = 'a52b8938-8e7b-46cd-ad62-e990d7fb4272'

class IbmWatsonHelper():
    ASSISTANT_VERSION = "2021-06-14"

    ASSISTANT_SERVICE_URL = 'https://api.us-east.assistant.watson.cloud.ibm.com/instances/e41eae4f-7307-4fe7-8a35-d863659aedd3'

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
        
    def run(self):
        entity = []
        while len(entity) == 0:
            user_input = input("What are you up to today? ")
            response = self.assistant.message_stateless(
                assistant_id=ASSISTANT_ID,
                input={
                    'message_type': 'text',
                    'text': user_input
                }
            ).get_result()
            entity = response['output']['entities']
        print("Sounds like a", entity[0]['entity'])
            
        

ibm_watson_helper = IbmWatsonHelper()
ibm_watson_helper.run()
