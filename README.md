# **markob** - Web Highlighter for Obsidian

[![Docker image](https://github.com/Rooyca/markob/actions/workflows/deploy-image.yml/badge.svg?branch=main)](https://github.com/Rooyca/markob/actions/workflows/deploy-image.yml)


While reading your favorite articles you can highlight your texts and send them to your Obsidian vault and it will automatically create a file with the name of the page. Saving what interests you has never been easier*.

![highlighter](https://github.com/Rooyca/markob/blob/main/highlighter_obsidian.png)

## Extension Installation

### Firefox

#### Firefox Browser Addons

1. Go to [Firefox browser addons](https://addons.mozilla.org/en-US/firefox/addon/markob/)
2. Install the extension

#### Manual Installation

1. Download the latest version from [here](Install.zip)
2. Open `about:debugging` in Firefox
3. Click on "This Firefox"
4. Click on "Load Temporary Add-on"
5. Select the `Install.zip` file

## Running the server

**Enviorment variables**

| Variable | Description | Default |
| -------- | ----------- | ------- |
| `OBSIDIAN_PATH` | Path to your Obsidian vault | `/code/obsi/` |

- **Befor running the server make sure you export the `OBSIDIAN_PATH` variable by running `export OBSIDIAN_PATH=/path/to/your/obsidian/vault`.**


#### PIP

1. Install the package

```bash
pip install markob
```

2. Run the server

```bash
markob
```

#### Docker

If you dont have docker installed go [**here**](https://docs.docker.com/engine/install/) and follow the instructions.

1. Pull the image

```bash
docker pull ghcr.io/rooyca/markob:main
```

2. Run the image

```bash
docker run --rm -p 8888:8888 rooyca/markob:main
```

Where `/home/USER/Documents/Obsidian/Highlights/` is the path to your Obsidian vault. Make sure to create your `Highlights` folder in your vault.

It's that simple!

#### Docker build

If you want to build the docker image yourself you can do it by:

1. Clone the repo

```bash
git clone https://github.com/Rooyca/MarkOb
```

2. Build the image

```bash
docker build -t markob .
```

3. Run the image

```bash
docker run --rm -p 8888:8888 markob
```

#### Binary

Download the latest binary from the [release page](https://github.com/Rooyca/markob/releases/download/0.0.2/markob.bin), make it executable and run it.

```bash
chmod +x markob.bin
./markob
```

#### Python (FastAPI Version)

1. Clone the repo

```bash
git clone https://github.com/Rooyca/MarkOb
```

2. Install the requirements

```bash
pip install -r requirements.txt
```

3. Run the api

```bash
uvicorn server/server.old:app --bind 8888
```

#### Python (http.server Version)

1. Clone the repo

```bash
git clone https://github.com/Rooyca/MarkOb
```

2. Run the server

```bash
python server/server.py
```

---

## Usage

1. Highlight some text
2. Right click on the text
3. Select the option you want

You can also use the keyboard shortcuts:

- `ALT + J` to send the highlighted text to Obsidian.
- `ALT + K` to send the highlighted text + Tags.
- `ALT + L` to send the highlighted text + Note.
- `ALT + P` to send the highlighted text + Tags and a note.

---

## Contributing

All contributions are welcome! If you find a bug or have a suggestion please open an issue. If you want to contribute code please open a pull request.