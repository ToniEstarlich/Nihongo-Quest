import requests
from flask import Blueprint, render_template, request

# blueprint for manga routes
manga_routes = Blueprint('manga_routes', __name__)

# Manga search section
@manga_routes.route('/manga')
def manga():
    # Fetch manga data from Jikan API
    response = requests.get('https://api.jikan.moe/v4/manga')
    manga_data = response.json()['data']  # Get the 'data' key which contains the manga list

    # Pass manga data to the template
    return render_template('manga.html', manga_data=manga_data)

# Route for searching manga
@manga_routes.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')  # Get the search query from URL parameters
    if query:
        # Fetch search results from Jikan API based on the query
        response = requests.get(f'https://api.jikan.moe/v4/manga?q={query}')
        manga_data = response.json()['data']  # Get search results
    else:
        manga_data = []

    # Pass search results to the template
    return render_template('manga.html', manga_data=manga_data)
