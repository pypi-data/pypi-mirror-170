# Dolby Vision Helpers

## System prerequisites

- [mediainfo](https://mediaarea.net/ru/MediaInfo)
- [mp4muxer](https://github.com/DolbyLaboratories/dlb_mp4base)
- [dovi_tool](https://github.com/quietvoid/dovi_tool)

## Usage

```text
Usage: python -m cli [OPTIONS] COMMAND [ARGS]...

  Command line interface for collection of scripts to convert MKV container
  into Dolby Vision 8.1 compatible MP4.

Options:
  --help  Show this message and exit.

Commands:
  demux     Demuxing MKV container into HEVC and AC3 streams.
  info      Gathering mediainfo data into cached file.
  mux       Muxing HEVC and AC3 streams into compatible MP4 container.
  pipeline  Command to chain info, demux and mux operations.
```
