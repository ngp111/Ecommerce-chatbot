import dialogflow
import os
from google.api_core.exceptions import InvalidArgument

project_id = "ambient-nuance-301517"
language_code = "en"
session_id = "me"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/intel123/ecommerce-chatbot/private_key.json'

msg = "Hello"
session_client = dialogflow.SessionsClient()
session = session_client.session_path(project_id, session_id)

query = dialogflow.types.TextInput(text=msg, language_code = language_code)
query = dialogflow.types.QueryInput(text=query)

try :
	response = session_client.detect_intent(session = session, query_input=query)
except InvalidArgument :
	raise
	
print(query)
print(response)

