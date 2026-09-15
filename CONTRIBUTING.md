# Contributing Guide

- [Introduction](#introduction)
- [How to?](#how-to)
- [Project Structure](#project-structure)

## Introduction

This repository contains publicly available links to live streams. Please keep changes focused on the playlist files and follow the formatting requirements below.

## How to?

### How to add a new stream link to a playlist?

You have several options:

1. Create a new request using this [form](https://github.com/iptv-org/iptv/issues/new?assignees=&labels=streams:add&projects=&template=1_streams_add.yml&title=Add%3A+) and, if approved, the link will automatically be added to the playlist on the next update.
2. Add the link to the playlist directly using a [pull request](https://github.com/iptv-org/iptv/pulls). See [Playlists](./docs/playlists.md).

Regardless of which option you choose, please perform the following checks before posting your request:

- Make sure you are using a valid [stream ID](./docs/stream-id.md).
- Make sure the channel is not on our blocklist. The easiest way to do this is through [iptv-org.github.io](https://iptv-org.github.io/).
- Make sure the link is not already in the playlist by [searching](https://github.com/search?q=repo%3Aiptv-org%2Fiptv+http%3A%2F%2Fexample.com&type=code) the repository.
- Make sure the link you want to add is stable and works properly. See [Stream Testing](./docs/stream-testing.md).
- Make sure the link is not [geo-blocked](./docs/geo-blocking.md). If it is, do not forget to mention this in your request.
- Make sure the link does not lead to a [Xtream Codes](./docs/xtream-codes.md) server. [Why don't you accept links to Xtream Codes servers?](./FAQ.md#why-dont-you-accept-links-to-xtream-codes-servers).
- Make sure the link is not [tokenized](./docs/tokenized-links.md).
- Make sure the link leads directly to the broadcast without unnecessary redirects.

If the broadcast only works in certain countries or is periodically interrupted, please indicate this in your request.

**IMPORTANT:** A request without a valid stream ID or a working stream link will be closed immediately.

### How to fix the stream description?

Stream descriptions are stored in the playlist entries under `streams/`.

So there are usually only two reasons for an incorrect description:

- **The stream has an incorrect ID:** In that case, all you need is to update the stream ID in the playlist using this [form](https://github.com/iptv-org/iptv/issues/new?assignees=&labels=streams%3Aedit&projects=&template=2_streams_edit.yml&title=Edit%3A+). A full list of all supported channels and their corresponding IDs can be found on [iptv-org.github.io](https://iptv-org.github.io/).

Once the changes are approved, the stream description will automatically update across all repositories.

### How to report a broken stream?

Fill out this [form](https://github.com/iptv-org/iptv/issues/new?assignees=&labels=streams:remove&projects=&template=3_streams_report.yml&title=Broken%3A+) and as soon as a working replacement appears, we will add it to the playlist or at least remove the non-working one.

The only thing before publishing your report is to make sure that:

- The link is still in our playlists. You can verify this by [searching](https://github.com/search?q=repo%3Aiptv-org%2Fiptv+http%3A%2F%2Fexample.com&type=code) the repository.
- The link is completely broken and is not just [geo-blocked](https://en.wikipedia.org/wiki/Geo-blocking). See [Stream Testing](./docs/stream-testing.md).

**IMPORTANT:** An issue without a valid stream link will be closed immediately.

### How to remove my channel from the playlist?

To request the removal of a channel link from the repository, please fill out this [form](https://github.com/iptv-org/iptv/issues/new?assignees=&labels=removal+request&projects=&template=6_copyright-claim.yml&title=Remove%3A+) and wait for the request to be reviewed (this usually takes less than 1 business day). If approved, links to the channel will be immediately removed from the repository.

Update or remove the affected playlist entry directly when a stream should no longer be included.

**IMPORTANT:** We only accept removal requests from channel owners and their official representatives. All other requests will be closed immediately.

## Project Structure

- `.github/`
  - `DISCUSSION_TEMPLATE/`: Contains discussion templates for the repository.
  - `ISSUE_TEMPLATE/`: Contains issue templates for the repository.
  - `workflows/`: Contains [GitHub Actions](https://docs.github.com/en/actions/quickstart) workflows. See [Workflows](./docs/workflows.md).
  - `CODE_OF_CONDUCT.md`: Rules you shouldn't break if you don't want to get banned.
- `.readme/`
  - `preview.png`: Image displayed in the `README.md`.
  - `template.md`: Template configuration for `PLAYLISTS.md`.
- `scripts/`: Contains internal utility scripts used in the repository. See [Scripts](./docs/scripts.md).
- `streams/`: Contains internal playlists with all streams. See [Playlist Structure](./docs/playlist-structure.md).
- `tests/`: Contains test suites to validate project scripts.
- `CONTRIBUTING.md`: The file you are currently reading.
- `PLAYLISTS.md`: Automatically updated list of available playlists.
- `README.md`: Project description and documentation overview.
