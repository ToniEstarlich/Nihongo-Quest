import pytest
from models.image import Image
from extensions import db

def test_image_list(client, create_user, logged_in_user):
    user = logged_in_user

    img = Image(
        image_path="uploads/test_image.png",
        category="food",
        japanese_word="すし",
        pronunciation="sushi",
        user_id=user.id
    )
    db.session.add(img)
    db.session.commit()

    response = client.get('/images/')

    assert response.status_code == 200
    assert ("すし".encode('utf-8') in response.data) or (b"sushi" in response.data)
