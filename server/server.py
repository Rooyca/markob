from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing import Any
import os, datetime, uvicorn

app = FastAPI()
obsidian_path = os.getenv('OBSIDIAN_PATH', '/code/obsi/')


class Content(BaseModel):
    href: Union[str, None] = Field(default=None, title="Link of the highlighted text")
    title: Union[str, None] = Field(default=None, title="Title of the tab")
    time: Union[str, None] = Field(default=None, title="Time when text was highlighted")
    text: Union[str, None] = Field(default=None, title="The content of the highlighted text")
    html: Union[str, None] = Field(default=None, title="The content of the highlighted text with HTML components")
    note: Union[str, None] = Field(default=None, title="Notes from user")
    tags: Any

@app.post("/")
async def get_contem(content: Content = Body()):
	ts = int(content.time)
	template_es = f"""---
tipo: Highlights
titulo: {content.title}
referencia: {content.href}
creado: {datetime.datetime.now().strftime("%Y" + "-" + "%m" + "-" + "%d")}
---

# Highlights

- [{content.note}]
- [[{content.tags}]]
> {content.text}<div class="signature"> Highlighted: {datetime.datetime.utcfromtimestamp(ts / 1e3)} </div>
"""
	path = obsidian_path+content.href.split('/')[2]+" - "+content.title.replace('|','').replace(':','')+".md"
	isFile = os.path.isfile(path)
	if not isFile:
		with open(path, 'w') as wt:
			wt.write(template_es)
		return content

	append_higlight_es = f"""

- [{content.note}]
- [[{content.tags}]]
> {content.text}<div class="signature"> Highlighted: {datetime.datetime.utcfromtimestamp(ts / 1e3)} </div>
"""

	with open(path, 'a') as wat:
		wat.write(append_higlight_es)

	return content

if __name__ == "__main__":
	uvicorn.run(app, host="localhost", port=8888)
	