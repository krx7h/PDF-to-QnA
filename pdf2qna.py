from PyPDF2 import PdfReader
import requests

def pdf2text():
    reader = PdfReader(r"C:\Users\krishna_bhat\Projects\Document.pdf")
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    return full_text

def QnA(comptext):
    API_KEY = "YOUR API KEY"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"give me a list of important questions from this text: {comptext}"}
    ]
    data = {
        "model": "llama3-70b-8192",
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        content = response.json()
        reply = content['choices'][0]['message']['content']
        print("AI Response:", reply)
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    text = pdf2text()
    QnA(text)
