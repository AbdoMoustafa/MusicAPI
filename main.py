import json
import requests as r
import secrets


def main():
    artist_name = input("Enter an artist to view their top songs: ")
    songs, artists = search(artist_name)
    index = int(input("What song number would you like lyrics for? "))
    get_lyrics(songs[index-1])

    display_albums = int(input("\n\nEnter 1 if you would like to see all the artist's albums, otherwise enter any other number :"))

    if display_albums == 1:
        print(f"\n\nArtist's Albums/Tapes\n")
        get_albums(artists[index-1])
    return


def search(name):
    url = "https://genius-song-lyrics1.p.rapidapi.com/search"

    querystring = {"q": name, "per_page": "50", "page": "1"}

    headers = {
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com",
        "X-RapidAPI-Key": "8fb30a6f84msh304f7b132f6155cp101c24jsnb5cf49b26e0e"
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

    return songs, artist


def get_lyrics(api_path):
    url = f"https://genius-song-lyrics1.p.rapidapi.com{api_path}/lyrics"

    headers = {
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com",
        "X-RapidAPI-Key": "8fb30a6f84msh304f7b132f6155cp101c24jsnb5cf49b26e0e"
    }

    response = r.get(url, headers=headers).json()
    obj = response['response']['lyrics']['lyrics']['body']['plain']
    print(obj)


def get_albums(api_path):
    url = f"https://genius-song-lyrics1.p.rapidapi.com{api_path}/albums"

    headers = {
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com",
        "X-RapidAPI-Key": "8fb30a6f84msh304f7b132f6155cp101c24jsnb5cf49b26e0e"
    }
    response = r.get(url, headers=headers).json()
    #print(response)

    for album in response["response"]["albums"]:
        print(f"{album['full_title']} \nRelease Date : {album['release_date_components']['day']}/"
              f"{album['release_date_components']['month']}/"
              f"{album['release_date_components']['year']}\n"
              f"Cover Art : {album['cover_art_thumbnail_url']}\n")




if __name__ == '__main__':
    main()
