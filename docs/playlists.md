# Playlist format

Source playlists live under `streams/` and use the M3U format:

```m3u
#EXTM3U
#EXTINF:-1 tvg-id="ExampleTV.us",Example TV (720p)
https://example.com/playlist.m3u8
```

Files should use the `.m3u` extension, begin with `#EXTM3U`, and contain one stream URL after
each `#EXTINF` entry. Keep the existing metadata when editing an entry.

The `Build playlist` workflow combines these files into the root `index.m3u`, prioritizing
English-primary source groups and clearly identified international English channels. Non-English
source groups are excluded. Explicitly marked NSFW entries are retained as an exception.
