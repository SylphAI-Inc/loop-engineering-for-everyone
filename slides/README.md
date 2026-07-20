# Slides

Each file is one slide (`article.slide`).

## Reorder / enable

Edit `index.json` only:

```json
{
  "slides": [
    { "id": "1-title", "file": "1-title.html", "title": "Beyond Loop Engineering", "enabled": true, "number": 1 },
    { "id": "4-title", "file": "4-title.html", "title": "More Productive. More Drained.", "enabled": true, "number": 2 }
  ]
}
```

- **Order** = array order
- **enabled: false** = skip without deleting the file
- **number** = optional human label (loader renumbers live from enabled order)

## Edit a page

Open the matching `*.html` fragment under `slides/`.

## Preview

Serve the repo root over HTTP (fetch needs a server):

```bash
python3 -m http.server 8080
open http://localhost:8080/beyond-loop-engineering.html
```

Monolith backup: `beyond-loop-engineering.monolith.html`
