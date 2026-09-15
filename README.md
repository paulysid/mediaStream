# Personal Stream Playlist

This repository contains a personal collection of publicly available English-language live stream
links. Explicitly marked NSFW entries are retained regardless of language.

## Use the playlist

Open this URL in VLC or another M3U-compatible player:

```text
https://raw.githubusercontent.com/paulysid/mediaStream/main/index.m3u
```

The combined English-language `index.m3u` file is rebuilt automatically whenever a file under
`streams/` changes. The builder prioritizes English-primary source groups (`US`, `UK`, `CA`,
`AU`, `NZ`, and `IE`) and retains clearly identified international English channels. Explicitly
marked NSFW entries remain an exception.

## Organize streams

Stream files are grouped under `streams/`, generally by country or provider. Edit the relevant
`.m3u` file, then commit and push the change. The build workflow combines all stream files into
the root playlist. The build excludes non-English source groups and entries with clear non-English language markers
or religious markers while retaining explicitly marked NSFW entries unless they are also marked
as religious. Source files remain available for reference and future selection.

Each entry should include an `#EXTINF` line followed by a playable stream URL. Keep metadata such
as `tvg-id`, `tvg-name`, `tvg-logo`, and `group-title` when it is available.

## Limitations

The repository stores links, not video files. Stream availability, geographic restrictions,
authentication, and provider rate limits are outside this repository's control.
