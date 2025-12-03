## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)
# tests/test_image.py
## /images/ (GET)
**Test** 🟥
```python
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
```
**Checks** 🟩

1- Images page loads successfully

2- Database image entry appears in the list

3- Shows either the Japanese word or pronunciation

4-  User-specific image is visible
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)