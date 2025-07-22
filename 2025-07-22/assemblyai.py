import requests
import time

API_KEY = 'your_assemblyai_api_key'
audio_url = 'https://example.com/audio.mp3'  # Replace with your audio file URL

# Step 1: Upload audio (if not already hosted, use AssemblyAI’s upload endpoint)

# Step 2: Start transcription with LLM features
headers = {
    'authorization': API_KEY,
    'content-type': 'application/json'
}

json_data = {
    'audio_url': audio_url,
    'summarization': True,
    'summary_type': 'bullets',
    'auto_chapters': True,
    'entity_detection': True,
    'iab_categories': True
}

response = requests.post(
    'https://api.assemblyai.com/v2/transcript',
    json=json_data,
    headers=headers
)

transcript_id = response.json()['id']
print("Transcription started:", transcript_id)

# Step 3: Poll for result
while True:
    polling_response = requests.get(
        f'https://api.assemblyai.com/v2/transcript/{transcript_id}',
        headers=headers
    )
    status = polling_response.json()['status']
    if status == 'completed':
        break
    elif status == 'error':
        raise RuntimeError(polling_response.json()['error'])
    time.sleep(5)

result = polling_response.json()

# Step 4: Output results
print("\n🔤 Transcription Text:\n", result['text'])
print("\n📝 Summary:\n", result.get('summary'))
print("\n📌 Topics:\n", result.get('iab_categories_result', {}).get('summary', []))
