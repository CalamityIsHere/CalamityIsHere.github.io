"""Build the portfolio with the Python 3 standard library. Run from any directory."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json
import shutil

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_site"
OUT.mkdir(exist_ok=True)
# Replace generated pages and assets so removed projects disappear on a local rebuild.
for folder in ["projects", "assets", "uploads"]:
    if (OUT / folder).exists():
        shutil.rmtree(OUT / folder)
    if folder != "projects" and (ROOT / folder).is_dir():
        shutil.copytree(ROOT / folder, OUT / folder)
(OUT / "projects").mkdir()

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))

def paragraphs(value):
    return "".join(f"<p>{escape(part.strip())}</p>" for part in value.split("\n\n") if part.strip())

profile = read(ROOT / "content/profile.json")
brand = escape(profile["name"])
navigation = {"index.html": "Welcome", "about.html": "About me", "projects.html": "Projects", "contact.html": "Contact"}

def page(filename, title, body, active):
    prefix = "../" if "/" in filename else ""
    links = []
    for path, label in navigation.items():
        current = ' aria-current="page"' if active == path else ''
        links.append(f'<a href="{prefix}{path}"{current}>{label}</a>')
    markup = f'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · {brand}</title><link rel="stylesheet" href="{prefix}assets/style.css"></head>
<body><a class="skip" href="#main">Skip to content</a>
<header><a class="brand" href="{prefix}index.html"><span aria-hidden="true">∿</span>{brand}</a>
<nav aria-label="Main navigation">{"".join(links)}</nav></header>
<main id="main">{body}</main>
<footer><span>{brand} · Electrical engineering portfolio</span><a href="{prefix}contact.html">Contact</a></footer></body></html>'''
    (OUT / filename).write_text(markup, encoding="utf-8")

def intro(label, heading, description):
    return f'<div class="intro"><p class="label">{escape(label)}</p><h1>{escape(heading)}</h1>{paragraphs(description)}</div>'

scope = '''<figure class="scope"><figcaption>Transient response</figcaption>
<img src="assets/trace.svg" alt="A damped oscillation settling toward the baseline">
<small>Illustrative trace · normalized amplitude</small></figure>'''
home = f'''<section class="hero"><div><p class="label">Electrical engineering portfolio</p>
<h1>{escape(profile["headline"])}</h1>{paragraphs(profile["welcome"])}
<a class="button" href="projects.html">Explore projects</a></div>{scope}</section>
<section class="panel"><h2>About me</h2>{paragraphs(profile["intro"])}
<a href="about.html">Read my introduction</a></section>'''
page("index.html", "Welcome", home, "index.html")
about = intro("Profile", "About me", profile["intro"])
about += f'<section class="panel"><h2>My background</h2>{paragraphs(profile["bio"])}{paragraphs(profile.get("background", ""))}</section>'
page("about.html", "About me", about, "about.html")
contact = intro("Correspondence", "Get in touch", profile["contactIntro"])
email = profile.get("email", "").strip()
address = f'<p><a href="mailto:{quote(email, safe="@.+-")}">{escape(email)}</a></p>' if email else '<p>Contact details will appear here.</p>'
page("contact.html", "Contact", contact + '<section class="panel"><h2>Email</h2>'+address+'</section>', "contact.html")

cards = []
for path in sorted((ROOT / "content/projects").glob("*.json")):
    project = read(path)
    if project.get("published") is not True:
        continue
    title = escape(project["title"])
    category = escape(project.get("category") or "Project")
    destination = f"projects/{quote(path.stem)}.html"
    source = (project.get("image") or "").lstrip("/")
    image = ""
    if source:
        asset = Path(source)
        if asset.parts[0] not in {"assets", "uploads"} or ".." in asset.parts or not (OUT / asset).is_file():
            raise ValueError(f"Missing local image for {path.name}: {source}")
        image = f'<img class="diagram" src="{quote(source)}" alt="{escape(project.get("alt") or "")}">'
    description = paragraphs(project["summary"])
    card = f'<div><p class="label">{category}</p><h2><a href="{destination}">{title}</a></h2>{description}</div>'
    cards.append(f'<article class="project">{image or "<div></div>"}{card}</article>')
    body = intro(project.get("category") or "Project", project["title"], project["summary"])
    body += image.replace('src="', 'src="../', 1)
    for field, heading in [("brief", "Design brief"), ("design", "Design decisions"), ("results", "Results and lessons")]:
        if project.get(field):
            body += f'<section><h2>{heading}</h2>{paragraphs(project[field])}</section>'
    body += '<a href="../projects.html">All projects</a>'
    page(f"projects/{path.stem}.html", project["title"], f'<article class="case">{body}</article>', "projects.html")
archive = "".join(cards) or '<p class="panel">Project write-ups are on their way.</p>'
page("projects.html", "Projects", intro("Work index", "Projects", profile["projectsIntro"]) + archive, "projects.html")
print(f"Built four pages and {len(cards)} project case studies in _site/")
