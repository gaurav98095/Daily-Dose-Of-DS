from ragie import Ragie

client = Ragie(auth="<RAGIE_API_KEY>")

with open("goals.mp4", "rb") as video:
    response = client.documents.create(
        request={
            "file": {"file_name": "goals.mp4", "content": video},
            "mode": {"video": "audio_video", "audio": True}
        }
    )

retrieval = client.retrievals.retrieve(
    request={"query": "Moments when Messi scored a goal"}
)
