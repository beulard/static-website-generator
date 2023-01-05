# static-website-generator

Generate static html pages from markdown source files containing blog-like
entries.

## Usage

To generate the pages, run
``` sh
python generate.py
```
This will create the `static/` directory containing the full website,
including html pages, the stylesheet and all the assets present in the
`content/` directory.

The generator currently supports images, syntax-highlighted code and
wiki-style links such as `[[index]]`.

To visualize the output, run a simple server with
``` sh
python server.py
```
and visit `http://localhost:8000`.