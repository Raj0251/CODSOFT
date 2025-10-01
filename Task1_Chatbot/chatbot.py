# chatbot.py
import re

def chatbot_response(user_input: str) -> str:
    text = user_input.lower().strip()
    if re.search(r'\b(hi|hello|hey|hai)\b', text):
        return "Hello! I'm CODSOFT Bot — how can I help you today?"
    if re.search(r'\b(thanks|thank you|thx)\b', text):
        return "You're welcome! Anything else I can do?"
    if re.search(r'\bbye|goodbye|see you\b', text):
        return "Goodbye — good luck with your internship!"
    if 'internship' in text and 'start' in text:
        return "The internship starts on 01 September 2025 and ends on 30 September 2025."
    if 'tasks' in text or 'projects' in text:
        return "You must complete at least 3 AI tasks: chatbot, tic-tac-toe AI, image captioning, recommendation system, face detection."
    if 'github' in text:
        return "Create a repository named 'CODSOFT' and push each task in its own folder."
    return "I didn't understand that fully — could you rephrase?"

if __name__ == '__main__':
    print("🤖 CODSOFT Chatbot (type 'bye' to quit)")
    while True:
        user_input = input("> You: ")
        reply = chatbot_response(user_input)
        print("Bot:", reply)
        if "Goodbye" in reply:
            break
