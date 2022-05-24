import requests as r
import secrets


def main():
    artist_name = input("Enter an artist to view their top songs: ")
    artist_songs = find_artist(artist_name)[0]
    song_lyrics = input("What song number would you like lyrics for? ")
    get_lyrics(artist_songs[int(song_lyrics) - 1])
    return


def find_artist(name):
    url = "https://genius-song-lyrics1.p.rapidapi.com/search"

    querystring = {"q": name, "per_page": "50", "page": "1"}

    headers = {
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com",
        "X-RapidAPI-Key": "67167d2a9cmshc58048f31e25f90p1e5d4cjsn132ef897bf0f"
    }

    response = r.get(url, headers=headers, params=querystring)
    print(response.json())
    hits = response.json()["response"]["hits"]
    artist = []
    songs = []

    for i, hit in enumerate(hits):
        artist.append(hit["result"]["primary_artist"]["api_path"])
        songs.append(hit["result"]["api_path"])
        print(f'{i + 1}. {hit["result"]["full_title"]}')

    return songs, artist_id


def get_lyrics(api_path):
    url = f"https://genius-song-lyrics1.p.rapidapi.com{api_path}/lyrics"

    headers = {
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com",
        "X-RapidAPI-Key": "67167d2a9cmshc58048f31e25f90p1e5d4cjsn132ef897bf0f"
    }

    response = r.get(url, headers=headers).json()
    obj = response['response']['lyrics']['lyrics']['body']['plain']
    print(obj)

#def get_album():


if __name__ == '__main__':
    main()
