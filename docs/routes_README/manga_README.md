## Comeback [README](../README.md)

# Routes/manga_routes.py

**Purpose:**
Show a manga list and allow searching using the **Jikan API** (MyAnimeList free API)
https://api.jikan.moe/v4/manga

###  /manga (GET)
Fetch manga data from ``Jikan API``

**Routes** 🟩 
  ```python
    @manga_routes.route('/manga')
    def manga():
        response = requests.get('https://api.jikan.moe/v4/manga')
        manga_data = response.json()['data']
    return render_template('manga.html', manga_data=manga_data)
  ```

### /search (GET)
Fetch search results from Jikan API based on the query

**Routes** 🟩 
  ```python
  @manga_routes.route('/search', methods=['GET'])
  def search():
    ... # Searching Query and  results from Jikan API
  return render_template('manga.html', manga_data=manga_data) 
  ```
**HTML** 🟧 
  ```html
      <form action="/search" method="get">
            <input type="text" name="query" placeholder="Search for manga..." required>
            <button type="submit">検索</button>
      </form>
  ``` 
**Jinja** ⬜
  ```html
  {% for manga in manga_data %}
  <img src="{{ manga.images.jpg.image_url }}">
  {{ manga.title }}
  {{ manga.synopsis[:200] if manga.synopsis else 'No synopsis available' }}
  <a href="{{ manga.url }}" target="_blank">More Info</a>
  {% endfor %}
  ```

  **Summary**

1- Calls Jikan API to fetch manga list or search results.

2- Extracts the data field from the JSON response.

3- Passes the list to the template as manga_data.

4- HTML loops through results and displays titles, images, etc.
  ## Comeback [README](../README.md)
