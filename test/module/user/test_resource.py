import os

from run import app


def test_asr_post():
    """
    测试音频转写
    """
    with app.test_client() as client:
        with open(os.path.join(item_path, 'test_audio.wav'), 'rb') as audio:
            response = client.post("/asr", data={"audio": audio, "service_id": 514})

        print(f"response:${response.data}")
        assert 200 <= response.status_code <= 299
