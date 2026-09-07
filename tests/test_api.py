from fastapi.testclient import TestClient

from app.api import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "AI Documentation Assistant is running"
    }


def test_ask():
    response = client.post(
        "/ask",
        json={
            "question": "How do I run this project using Docker?"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert isinstance(data["answer"], str)
    assert len(data["answer"]) > 0