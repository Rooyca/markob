# **MarkOb**


Highlight your text and send it to your Obsidian vault. It automatically creates you a file with the name of the page.

## Installation

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

## Running the api

#### Docker (recomended)

If you dont have docker installed go [**here**](https://docs.docker.com/engine/install/) and follow the instructions.

1. Run 

```bash
docker run -d -v /home/USER/Documents/Obsidian/Highlights/:/code/obsi -p 8888:8888 rooyca/markob
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
docker run -d -v /home/rooyca/Documents/Obsidian/Highlights/:/code/obsi -p 8888:8888 markob
```

#### Python

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
uvicorn server:app --bind 8888
```

4. Go to your page and start highlighting 😊.

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











