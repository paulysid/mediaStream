# Stream entries

Use an `#EXTINF` line followed by the stream URL:

```m3u
#EXTINF:-1 tvg-id="ExampleTV.us",Example TV (720p)
https://example.com/playlist.m3u8
```

Useful optional attributes include `tvg-id`, `tvg-name`, `tvg-logo`, and `group-title`.
HTTP headers can be supplied with VLC directives when a provider requires them:

```m3u
#EXTINF:-1 tvg-id="ExampleTV.us",Example TV
#EXTVLCOPT:http-referrer=https://example.com/
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://example.com/stream.m3u8
```
