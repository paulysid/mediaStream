# Scripts

The repository does not download or publish external API data. The supported automation is the
`Build playlist` workflow, which combines the files in `streams/` into the root `index.m3u`
playlist whenever stream files change.

To check playlist syntax locally, run:

```shell
npm run playlist:lint
```
