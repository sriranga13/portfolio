#!/usr/bin/env python3
"""Build blogs/index.html, posts/template.html, and two draft posts for Sri's portfolio.
Reuses the exact <style> block from index.html so the theme matches perfectly.
"""
import re, pathlib

BASE = pathlib.Path.home() / "workspace" / "your_files" / "portfolio"
src = (BASE / "index.html").read_text(encoding="utf-8")
style_block = re.search(r"<style.*?</style>", src, re.S).group(0)

HEAD_TOP = """<meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <meta name="color-scheme" content="dark" />
  <meta name="theme-color" content="#07100e" />
  <link rel="icon" href="data:," />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">"""

BLOG_CSS = """
  <style>
    /* Blog-only additions, same theme tokens */
    .post-list{display:grid;gap:26px}
    .post-card{display:block;text-decoration:none;color:inherit;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:34px 36px;transition:border-color .25s, transform .25s}
    .post-card:hover{border-color:var(--lime);transform:translateY(-3px)}
    .post-card .meta{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-bottom:14px}
    .post-card .date{font:500 11px/1.4 "IBM Plex Mono",monospace;color:var(--muted);letter-spacing:.08em}
    .post-card h3{font-size:clamp(24px,3vw,36px);margin:0 0 12px}
    .post-card p.excerpt{color:var(--muted);margin:0 0 18px;max-width:720px}
    .tagrow{display:flex;flex-wrap:wrap;gap:8px}
    .tag{font:500 10px/1.4 "IBM Plex Mono",monospace;color:var(--cyan);border:1px solid var(--line);border-radius:999px;padding:5px 12px;letter-spacing:.06em}
    .empty{border:1px dashed var(--line);border-radius:14px;padding:44px;color:var(--muted);text-align:center}
    .prose{max-width:760px}
    .prose p{margin:0 0 1.4em;color:#dfe8e2;font-size:17px;line-height:1.75}
    .prose h2{font-size:clamp(24px,3vw,34px);margin:2.2em 0 .7em;letter-spacing:-.03em}
    .prose ul{color:#dfe8e2;line-height:1.75;margin:0 0 1.4em;padding-left:1.3em}
    .prose li{margin-bottom:.5em}
    .prose strong{color:var(--paper)}
    .prose code{font-family:"IBM Plex Mono",monospace;background:#0b1714;border:1px solid var(--line);border-radius:6px;padding:1px 7px;font-size:.88em;color:var(--lime)}
    .back{display:inline-block;margin-bottom:34px;font:500 12px/1.4 "IBM Plex Mono",monospace;color:var(--lime);text-decoration:none;letter-spacing:.06em}
    .back:hover{text-decoration:underline}
    .draft-banner{background:#2a1e0c;border:1px solid #6b4d1f;color:#f2c979;border-radius:10px;padding:14px 20px;font-size:14px;margin-bottom:36px}
    .post-hero-meta{display:flex;flex-wrap:wrap;gap:16px;align-items:center;margin:18px 0 44px}
  </style>"""

NAV_BLOG = """<nav class="nav" aria-label="Page sections">
    <a href="../index.html">Home</a><a href="../index.html#about">About</a><a href="../index.html#expertise">Expertise</a><a href="../index.html#work">Work</a><a href="../index.html#career">Career</a><a href="./" class="active" aria-current="page">Writing</a><a class="mail" href="../index.html#contact">Contact</a>
  </nav>"""

def page(title, nav, body_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_TOP}
  <title>{title}</title>
{style_block}
{BLOG_CSS}
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
{nav}
  <main id="main">
{body_html}
  </main>
</body>
</html>
"""

# ---------------------------------------------------------------- blogs/index.html
blog_body = """    <section>
      <div class="wrap">
        <div class="section-head">
          <div class="eyebrow">WRITING</div>
          <h2>Notes from the <em>lab × data</em> frontier.</h2>
        </div>
        <div class="post-list" id="post-list">
          <div class="empty">
            <p class="eyebrow" style="margin-bottom:12px">COMING SOON</p>
            <p style="margin:0">First posts are in review and will appear here shortly.<br>Topics: enterprise GenAI for regulated R&amp;D, computer vision in bioprocess, LIMS data engineering.</p>
          </div>
        </div>
        <!--
          PUBLISHED POST CARD PATTERN (uncomment + fill when a draft is approved):

          <a class="post-card" href="../posts/POST-SLUG.html">
            <div class="meta"><span class="date">MONTH YYYY</span></div>
            <h3>Post title</h3>
            <p class="excerpt">One-line excerpt.</p>
            <div class="tagrow"><span class="tag">TAG</span></div>
          </a>
        -->
      </div>
    </section>"""

(BASE / "blogs").mkdir(exist_ok=True)
(BASE / "blogs" / "index.html").write_text(
    page("Writing — Sri Gorantla", NAV_BLOG, blog_body), encoding="utf-8")
print("wrote blogs/index.html")

# ---------------------------------------------------------------- template
template_body = """    <section>
      <div class="wrap">
        <a class="back" href="../blogs/">&larr; ALL POSTS</a>
        <!-- EDIT: eyebrow = post category -->
        <div class="eyebrow">CATEGORY</div>
        <!-- EDIT: post title -->
        <h1 style="font-size:clamp(40px,6vw,76px);line-height:.95;letter-spacing:-.06em;margin:14px 0 0;max-width:900px;font-weight:800">[Post title]</h1>
        <div class="post-hero-meta">
          <!-- EDIT: publish date -->
          <span class="date" style="font:500 11px/1.4 'IBM Plex Mono',monospace;color:var(--muted);letter-spacing:.08em">[MONTH YYYY]</span>
          <!-- EDIT: tags -->
          <div class="tagrow"><span class="tag">[TAG 1]</span><span class="tag">[TAG 2]</span></div>
        </div>
        <div class="prose">
          <!-- EDIT: post body. Use <p>, <h2>, <ul><li>, <strong>, <code> as needed. -->
          <p>[Opening paragraph — hook the reader with the problem.]</p>
          <h2>[Section heading]</h2>
          <p>[Body paragraph.]</p>
        </div>
      </div>
    </section>"""

posts_dir = BASE / "posts"
posts_dir.mkdir(exist_ok=True)
(posts_dir / "template.html").write_text(
    page("[Post title] — Sri Gorantla", NAV_BLOG, template_body), encoding="utf-8")
print("wrote posts/template.html")

# ---------------------------------------------------------------- drafts
drafts_dir = posts_dir / "drafts"
drafts_dir.mkdir(exist_ok=True)

DRAFT1 = """<p>Scientists at a biotech company sit on top of a goldmine: years of experimental data, regulatory filings, QC records, and process knowledge spread across databases that only a handful of specialists know how to query. Everyone else files a ticket, waits, and eventually makes a decision with half the picture. I kept running into this wall, so we built something to tear it down: <strong>Genie</strong>, an enterprise GenAI platform that lets regulatory, QC, and R&amp;D teams ask questions in plain English and get answers grounded in the company's own scientific databases.</p>
<p>This post is about what it actually took to build that — and why the hard parts had almost nothing to do with the language model.</p>
<h2>The problem with "just ask the chatbot"</h2>
<p>In a regulated environment, a fluent wrong answer is worse than no answer. A scientist asking about a formulation's stability history or a regulatory colleague pulling submission-relevant data cannot afford a hallucination dressed up as confidence. So the central design decision for Genie was this: <strong>the LLM is the interface, not the source of truth</strong>. Every answer has to be traceable back to a query against a real database, and the user needs to see that provenance.</p>
<p>That framing shaped everything downstream. We weren't building a chatbot with a database plugged in; we were building a natural-language query layer over scientific data, where the model translates intent into structured retrieval and then synthesizes — never invents.</p>
<h2>Grounding answers in scientific databases</h2>
<p>The backbone is retrieval over the company's scientific databases: experimental results, batch and formulation records, QC data, and regulatory documentation. Natural-language querying sounds magical until you watch a model try to join three domain tables it has never seen. Getting this right meant careful work on schema description, giving the model an accurate map of what lives where, and constraining it to generate queries against that map rather than freelancing.</p>
<p>Prompt engineering turned out to be genuine engineering here, not vibes. We iterated on system prompts the way you'd iterate on code: versioned, tested against a set of representative questions, and reviewed when answers drifted. The prompts encode domain rules — which sources to prefer, how to say "I don't know" instead of guessing, and how to present uncertainty. In a regulated setting, a well-engineered refusal is a feature.</p>
<h2>MCP servers: giving the model hands, not just eyes</h2>
<p>Retrieval covers "what does the data say," but R&amp;D workflows need actions: look up a manufacturing record, check a formulation's component history, pull discovery-stage assay context. That's where <strong>MCP servers</strong> came in. We built MCP servers for manufacturing, formulations, and discovery — each exposing a curated set of tools the model can call — and surfaced them through <strong>LibreChat</strong> as the conversational front end.</p>
<p>I like the MCP approach for a practical reason: it draws a clean boundary. The model reasons in language; the tools execute deterministic operations against systems of record. The tool definitions become a contract you can validate, version, and audit — which matters enormously when quality and regulatory teams ask "exactly what did the system touch to produce this answer?" LibreChat gave us an open, extensible chat interface without building a whole frontend framework from scratch, so the team could focus on the tools and the grounding instead of UI plumbing.</p>
<h2>What I'd tell anyone building this</h2>
<ul>
<li><strong>Start with the refusal.</strong> Design how the system says "I can't answer that from available data" before you design anything else. In regulated R&amp;D, trust is the product.</li>
<li><strong>Treat prompts like code.</strong> Version them, test them, review them. Prompt drift is real and silent.</li>
<li><strong>Keep humans in the loop where it counts.</strong> Genie accelerates research and QC investigation; it doesn't sign off on anything. That boundary should be explicit in the product, not just the documentation.</li>
<li><strong>Tools beat context.</strong> An MCP tool that runs the right query will outperform a giant context window stuffed with hopefully-relevant documents, every time.</li>
</ul>
<p>Genie changed how quickly teams at Greenlight could go from question to evidence. The lesson I keep coming back to: enterprise GenAI in a regulated industry isn't a model problem, it's a <em>trust architecture</em> problem — provenance, boundaries, and honest uncertainty, with the LLM as the friendly face on top of rigorous machinery.</p>"""

DRAFT2 = """<p>In bioprocess manufacturing, contamination is the nightmare scenario: a compromised batch means lost product, lost time, and a painful investigation. Traditionally, catching fungal contamination early meant trained eyes on plates and samples — slow, subjective, and hard to scale. We built a computer-vision pipeline that does it automatically, and it now detects fungal contamination at <strong>97% accuracy</strong>. Here's how, and what I learned taking it from idea to a deployed Azure ML system.</p>
<h2>Why SAM</h2>
<p>The classic approach would be training a segmentation model from scratch on labeled contamination images. The problem: high-quality labeled data in this domain is scarce and expensive — every label needs a trained microbiologist. Instead, we built on <strong>SAM, the Segment Anything Model</strong>, as the segmentation backbone.</p>
<p>SAM's strength is that it already understands "what is an object" from massive pretraining, so it can delineate colony boundaries and morphology without us teaching it vision from zero. Our job shifted from "learn to see" to "learn what fungal contamination looks like" — a much smaller, more tractable learning problem that needs far less labeled data. For niche scientific imaging, that leverage is the whole game: foundation models let small teams punch far above their dataset size.</p>
<h2>The pipeline</h2>
<p>The pipeline runs in stages. First, imaging: consistent capture conditions matter more than any model tweak — lighting, focus, and plate positioning inconsistencies will quietly cap your accuracy before training even starts. Then SAM-based segmentation isolates candidate regions: colonies, growth patterns, morphological features. A classification stage then decides contamination versus clean, trained on labeled examples of both.</p>
<p>Getting to 97% accuracy wasn't one breakthrough; it was a grind of small wins. The biggest jumps came from data work, not architecture work: cleaning label noise, making sure edge cases (early-stage growth, atypical colony morphology, imaging artifacts) were represented in training, and building an evaluation set that actually reflected production conditions rather than the easy cases.</p>
<h2>Deploying on Azure ML</h2>
<p>A model that only runs in a notebook helps nobody. We deployed the pipeline on <strong>Azure ML</strong>, which gave us versioned model endpoints, reproducible training runs, and a path to retrain as new labeled data comes in. That last part matters: contamination strains and imaging setups drift, and a deployed model without a retraining story is a model with an expiration date.</p>
<p>We also kept a human-in-the-loop for low-confidence predictions. The system is confident and correct the vast majority of the time, but the cost of a missed contamination event dwarfs the cost of a false alarm — so borderline cases get flagged for human review rather than auto-cleared. Designing that threshold explicitly, instead of defaulting to the model's argmax, was one of the most important product decisions in the project.</p>
<p>Monitoring closes the loop. We track prediction confidence distributions and flag drift — if the incoming image characteristics shift (a new camera, a different plate supplier), the team hears about it before accuracy silently degrades. A vision system in manufacturing is never "done"; it's a living system with a maintenance contract.</p>
<h2>Practical lessons</h2>
<ul>
<li><strong>Data beats architecture.</strong> Nearly every accuracy gain came from better labels and better evaluation, not a fancier model.</li>
<li><strong>Evaluate on production reality.</strong> A test set of clean, well-lit examples will lie to you. Include the ugly cases.</li>
<li><strong>Design for drift.</strong> Ship the retraining pipeline alongside the model, not after.</li>
<li><strong>Respect asymmetric costs.</strong> When a false negative is catastrophic, tune and threshold accordingly — accuracy alone doesn't tell the story.</li>
</ul>
<p>Computer vision in bioprocess isn't about chasing state-of-the-art on a benchmark; it's about building something reliable enough that a QC team trusts it with real batches. SAM got us there faster than training from scratch ever could, Azure ML keeps it running reproducibly, and the unglamorous data work is what made 97% real instead of theoretical.</p>"""

def wordcount(html):
    text = re.sub(r"<[^>]+>", " ", html)
    return len(text.split())

draft_meta = [
    ("genie-genai-platform.html",
     "Building Genie: an enterprise GenAI platform for regulated R&D",
     "ENTERPRISE GENAI",
     ["GENAI", "RAG", "MCP", "LIBRECHAT", "PROMPT ENGINEERING"],
     DRAFT1,
     "How we built Genie at Greenlight Biosciences: natural-language querying of scientific databases, MCP servers for manufacturing/formulations/discovery, and why trust architecture matters more than the model in regulated R&D."),
    ("sam-fungal-detection.html",
     "97% accuracy on fungal contamination detection with SAM",
     "COMPUTER VISION",
     ["SAM", "COMPUTER VISION", "AZURE ML", "BIOPROCESS"],
     DRAFT2,
     "A SAM-based vision pipeline for fungal contamination detection at 97% accuracy, deployed on Azure ML — and the unglamorous data work that made it real."),
]

for fname, title, eyebrow, tags, body, excerpt in draft_meta:
    tagrow = "".join(f'<span class="tag">{t}</span>' for t in tags)
    banner = ('<div class="draft-banner"><strong>DRAFT — pending Sri\'s approval.</strong> '
              'Not linked from the blog index. Do not publish as-is.</div>')
    body_html = f"""    <section>
      <div class="wrap">
        <a class="back" href="../../blogs/">&larr; ALL POSTS</a>
        {banner}
        <div class="eyebrow">{eyebrow}</div>
        <h1 style="font-size:clamp(40px,6vw,76px);line-height:.95;letter-spacing:-.06em;margin:14px 0 0;max-width:900px;font-weight:800">{title}</h1>
        <div class="post-hero-meta">
          <span class="date" style="font:500 11px/1.4 'IBM Plex Mono',monospace;color:var(--muted);letter-spacing:.08em">DRAFT — DATE ON PUBLISH</span>
          <div class="tagrow">{tagrow}</div>
        </div>
        <div class="prose">
{body}
        </div>
      </div>
    </section>"""
    (drafts_dir / fname).write_text(
        page(f"{title} — Sri Gorantla [DRAFT]", NAV_BLOG, body_html), encoding="utf-8")
    print(f"wrote posts/drafts/{fname} ({wordcount(body)} words)")

print("done")
