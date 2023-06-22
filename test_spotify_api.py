import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='1ff69d94deb24751b4e1a55c9bf9301d',client_secret='05f6def4895641848da6cfeaa6afceef'))

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Dhvani Bhanushali'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']


print(items[0])

results = spotify.artist_top_tracks(items[0]['uri'])

