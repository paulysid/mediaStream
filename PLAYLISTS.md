# Playlists

The primary playlist is the root `index.m3u` file:

```text
https://raw.githubusercontent.com/paulysid/mediaStream/main/index.m3u
```

Individual source playlists are in the `streams/` directory. The `Build playlist` GitHub Actions
workflow combines them whenever stream files change. Clearly non-English entries are excluded;
English-primary source groups and clearly identified international English channels are included.
Religious entries are excluded, and explicitly marked NSFW entries are retained as an exception
unless they are also marked as religious.
