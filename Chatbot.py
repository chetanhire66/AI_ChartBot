import google.generativeai as genai

API_KEY = "AIzaSyCcRmcdgNLe5UZP0RyDXL6ow23fuyEDzXU"
genai.configure(api_key=API_KEY)

gemini_model = genai.GenerativeModel(
    'gemini-1.5-flash',
    system_instruction="You are a helpful assistant."
)

gemini_chat = gemini_model.start_chat(history=[])

def gemini(text_input):
    try:
        response = gemini_chat.send_message(text_input)
        response_text = response.text.strip()
        print("Gemini:", response_text)
        return response_text  
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg:
            response_text = "Daily limit reached. Try tomorrow or upgrade plan."
        else:
            response_text = "Sorry, something went wrong with Gemini."
        
        print("Gemini Error:", error_msg)
        return response_text  
