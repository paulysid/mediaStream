# Workflows

The `Build playlist` workflow runs when files in `streams/` change. It combines all stream
playlists into `index.m3u`, commits the result, and keeps the raw GitHub playlist URL current.
