from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
import os

os.environ["GITHUB_TOKEN"] = "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"
client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

def get_llm_response(query: str) -> str:
    """Get response from Llama-3.3 model."""
    try:
        response = client.complete(
            messages=[
                SystemMessage("You are JARVIS, a highly advanced AI companion inspired by Iron Man’s trusty sidekick. Speak in a warm, clever, and conversational tone, blending wit with genuine assistance. Help with tasks like web searches, system control, reminders, or sharing useful info. Keep your replies sharp, lively, and to the point, sprinkling in a bit of humor or charm when it fits. Always focus on making the user’s life easier with clear, intuitive support."),
                UserMessage(query),
            ],
            model="Llama-3.3-70B-Instruct",
            temperature=0.8,
            max_tokens=2048,
            top_p=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return "Sorry, I couldn't process that request."