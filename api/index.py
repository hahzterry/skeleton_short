
from flask import Flask, Response, jsonify

app = Flask(__name__)

HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#080a0b">

<title>BUILD MOTION | CRE MARKET</title>

<meta name="description"
content="Turn commercial real estate concepts into cinematic construction reveal videos. Flat $499 pricing and 24-hour delivery target.">

<style>
:root {
  --bg: #080a0b;
  --panel: #111719;
  --line: #273135;
  --white: #f4f7f7;
  --muted: #a5b2b5;
  --green: #b5ff4b;
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--white);
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.6;
}

a {
  color: inherit;
  text-decoration: none;
}

.wrap {
  max-width: 1180px;
  margin: auto;
  padding: 0 24px;
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  padding: 25px 0;
  border-bottom: 1px solid var(--line);
}

.logo {
  font-size: 22px;
  font-weight: 900;
  letter-spacing: -1px;
}

.logo span { color: var(--green); }

.links {
  display: flex;
  gap: 22px;
  align-items: center;
  font-size: 13px;
  font-weight: bold;
}

.btn {
  display: inline-block;
  background: var(--green);
  color: #071006;
  padding: 15px 24px;
  border-radius: 7px;
  font-weight: 900;
  text-align: center;
}

.btn:hover { filter: brightness(.9); }

.btn-outline {
  background: transparent;
  color: white;
  border: 1px solid #596367;
}

.eyebrow {
  color: var(--green);
  text-transform: uppercase;
  font-size: 12px;
  letter-spacing: 3px;
  font-weight: bold;
}

.hero {
  display: grid;
  grid-template-columns: 1.1fr .9fr;
  gap: 40px;
  align-items: center;
  padding: 95px 0;
}

h1 {
  font-size: clamp(46px, 6vw, 84px);
  line-height: 1.05;
  letter-spacing: -4px;
  margin: 20px 0;
}

h1 span { color: var(--green); }

h2 {
  font-size: clamp(32px, 4vw, 52px);
  line-height: 1.15;
  letter-spacing: -2px;
  margin: 15px 0;
}

p { color: var(--muted); }

.lead {
  font-size: 19px;
  max-width: 570px;
}

.actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin: 30px 0;
}

.small {
  font-size: 13px;
  color: var(--muted);
}

.visual {
  min-height: 470px;
  border: 1px solid #394442;
  border-radius: 15px;
  background:
    radial-gradient(circle at 50% 35%,
      #244239, #101c1d 50%, #080a0b);
  display: flex;
  align-items: end;
  padding: 30px;
  position: relative;
  overflow: hidden;
}

.visual:before {
  content: "";
  position: absolute;
  inset: 14% 13% 25%;
  border: 2px solid #b5ff4b77;
  background:
    repeating-linear-gradient(
      90deg,
      transparent 0 30px,
      #b5ff4b33 31px 32px
    ),
    repeating-linear-gradient(
      0deg,
      transparent 0 32px,
      #b5ff4b33 33px 34px
    );
  transform: perspective(450px)
             rotateY(-13deg) skewY(-5deg);
  box-shadow: 0 0 90px #b5ff4b22;
}

.visual-content {
  position: relative;
  z-index: 2;
}

.visual h3 {
  font-size: 34px;
  line-height: 1.1;
  margin-bottom: 8px;
}

.metrics {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  padding: 28px 0;
  gap: 20px;
}

.metrics strong {
  display: block;
  color: var(--green);
  font-size: 30px;
}

.metrics span {
  color: var(--muted);
  font-size: 13px;
}

section.content {
  padding: 85px 0;
}

.steps {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  margin-top: 35px;
}

.card {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 28px;
}

.card .number {
  color: var(--green);
  font-weight: bold;
}

.card h3 {
  font-size: 23px;
  margin: 15px 0;
}

.compare-section {
  background: #0e1214;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}

.comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
  margin-top: 35px;
}

.comparison .new {
  border-color: var(--green);
  background: linear-gradient(
    145deg, #16221b, #0e1614
  );
}

.big-price {
  font-size: clamp(34px, 4vw, 50px);
  font-weight: 900;
  letter-spacing: -2px;
  margin: 20px 0;
}

.green { color: var(--green); }

ul { padding-left: 22px; }

li { margin: 10px 0; }

.note {
  font-size: 12px;
  color: var(--muted);
  margin-top: 20px;
}

.pricing {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: center;
}

.price-box {
  border: 1px solid var(--green);
  background: #111b15;
  padding: 35px;
  border-radius: 14px;
}

.amount {
  font-size: 76px;
  font-weight: 900;
  letter-spacing: -4px;
}

.amount small {
  font-size: 16px;
  color: var(--muted);
  letter-spacing: 0;
}

.faq {
  margin: 15px 0;
}

.faq h3 { margin-bottom: 6px; }

.faq p { margin-top: 0; }

.cta {
  text-align: center;
  padding: 85px 20px;
  border-top: 1px solid var(--line);
}

footer {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  padding: 30px 0;
  border-top: 1px solid var(--line);
  font-size: 13px;
  color: var(--muted);
}

@media(max-width: 800px) {
  .hero, .comparison, .pricing {
    grid-template-columns: 1fr;
  }

  .hero { padding: 55px 0; }

  .visual { min-height: 340px; }

  .steps { grid-template-columns: 1fr; }

  .links a:not(.btn) { display: none; }

  .metrics {
    grid-template-columns: 1fr 1fr;
  }

  section.content { padding: 60px 0; }

  footer { flex-direction: column; }

  h1 { letter-spacing: -2px; }

  .amount { font-size: 60px; }
}
</style>
</head>

<body>

<div class="wrap">

<nav>
  <a href="https://cremarket.io" class="logo">
    CRE<span>MARKET</span> / MOTION
  </a>

  <div class="links">
    <a href="#how">HOW IT WORKS</a>
    <a href="#compare">COMPARE</a>
    <a href="#pricing">PRICING</a>
    <a class="btn" href="#pricing">
      START A PROJECT
    </a>
  </div>
</nav>

<main>

<section class="hero">

  <div>
    <div class="eyebrow">
      Commercial Real Estate Visual Storytelling
    </div>

    <h1>
      YOUR BUILDING.<br>
      <span>BUILT ON SCREEN.</span><br>
      IN 24 HOURS.
    </h1>

    <p class="lead">
      Turn your commercial building into a
      cinematic 30-second construction reveal.

      From sketch to steel frame to finished
      property — ready for investor pitches,
      real estate listings, and social media.
    </p>

    <div class="actions">
      <a class="btn" href="#pricing">
        GET YOUR VIDEO — $499
      </a>

      <a class="btn btn-outline" href="#how">
        HOW IT WORKS
      </a>
    </div>

    <p class="small">
      Flat fee · 9:16 video · One revision ·
      24-hour delivery target
    </p>
  </div>

  <div class="visual">
    <div class="visual-content">
      <div class="eyebrow">
        SKETCH → STRUCTURE → REVEAL
      </div>

      <h3>
        FROM VISION<br>
        TO VISUAL.
      </h3>

      <p class="small">
        Architectural concept animation
      </p>
    </div>
  </div>

</section>

<div class="metrics">

  <div>
    <strong>24 HRS</strong>
    <span>Target turnaround</span>
  </div>

  <div>
    <strong>30 SEC</strong>
    <span>Cinematic video</span>
  </div>

  <div>
    <strong>$499</strong>
    <span>Flat enterprise project fee</span>
  </div>

</div>

<section id="how" class="content">

  <div class="eyebrow">Simple Process</div>

  <h2>THREE STEPS. ONE VIDEO.</h2>

  <p>
    No complicated production process.
    Submit your building and we handle
    the cinematic visualization.
  </p>

  <div class="steps">

    <div class="card">
      <div class="number">01 / SUBMIT</div>
      <h3>UPLOAD YOUR BUILDING</h3>
      <p>
        Send a property photograph, approved
        architectural rendering, or building
        concept with a short description.
      </p>
    </div>

    <div class="card">
      <div class="number">02 / CREATE</div>
      <h3>WE RECREATE IT</h3>
      <p>
        We produce a cinematic construction
        sequence showing your building
        taking shape from the ground up.
      </p>
    </div>

    <div class="card">
      <div class="number">03 / DELIVER</div>
      <h3>GET YOUR VIDEO</h3>
      <p>
        Receive a 30-second vertical video
        for presentations, investor outreach,
        listings, and social media.
      </p>
    </div>

  </div>

</section>

</main>
</div>

<section id="compare"
         class="content compare-section">

<div class="wrap">

  <div class="eyebrow">
    A New Way to Market Commercial Real Estate
  </div>

  <h2>
    WEEKS OF WAITING.<br>
    OR ONE DAY.
  </h2>

  <p>
    Compare traditional custom architectural
    animation production with our streamlined
    concept-video service.
  </p>

  <div class="comparison">

    <div class="card">
      <div class="eyebrow"
           style="color:#a5b2b5">
        TRADITIONAL CRE PRODUCTION
      </div>

      <h3>THE OLD WAY</h3>

      <div class="big-price">
        $2,500–$10,000+
      </div>

      <ul>
        <li>Illustrative custom production budget</li>
        <li>2–6 weeks planning allowance</li>
        <li>Detailed 3D modeling and rendering</li>
        <li>Multiple production review stages</li>
        <li>Higher-detail architectural deliverables</li>
      </ul>
    </div>

    <div class="card new">
      <div class="eyebrow">
        CRE MARKET VISION
      </div>

      <h3>THE NEW WAY</h3>

      <div class="big-price green">
        $499 FLAT
      </div>

      <ul>
        <li>One cinematic 30-second video</li>
        <li>24-hour delivery target</li>
        <li>AI-assisted construction animation</li>
        <li>Voiceover, music, and captions</li>
        <li>One revision included</li>
      </ul>
    </div>

  </div>

  <p class="note">
    Traditional fees and timelines are
    illustrative planning estimates, not
    verified industry averages. The services
    have different scopes and deliverables.
  </p>

</div>
</section>

<div class="wrap">

<section id="pricing" class="content pricing">

  <div>
    <div class="eyebrow">
      Enterprise Video Production
    </div>

    <h2>
      ONE PROPERTY.<br>
      ONE PRICE.
    </h2>

    <p>
      Designed for commercial real estate
      brokers, property owners, developers,
      investors, and asset managers.
    </p>

    <p>
      Professional property storytelling
      without a traditional custom
      animation production engagement.
    </p>
  </div>

  <div class="price-box">

    <div class="eyebrow">
      ENTERPRISE CONCEPT VIDEO
    </div>

    <div class="amount">
      $499 <small>/ video</small>
    </div>

    <ul>
      <li>One commercial property concept</li>
      <li>30-second vertical MP4</li>
      <li>1080 × 1920 resolution</li>
      <li>Construction reveal animation</li>
      <li>AI voiceover and captions</li>
      <li>Background music</li>
      <li>One reasonable revision</li>
      <li>24-hour delivery target</li>
    </ul>

    <a class="btn"
       style="display:block;margin-top:25px"
       href="mailto:projects@cremarket.io?subject=Build%20Motion%20Project%20Inquiry">
      REQUEST YOUR VIDEO
    </a>

    <p class="note">
      Opens an email inquiry, not a payment
      checkout. Replace with your payment
      link when ordering is configured.
    </p>

  </div>

</section>

<section class="content"
         style="padding-top:0">

  <div class="eyebrow">
    Frequently Asked Questions
  </div>

  <h2>GOOD TO KNOW.</h2>

  <div class="card faq">
    <h3>DO I NEED ARCHITECTURAL DRAWINGS?</h3>
    <p>
      No. A description or reference image
      can start a conceptual visualization.
      Approved drawings improve accuracy.
    </p>
  </div>

  <div class="card faq">
    <h3>CAN YOU RECREATE MY BUILDING?</h3>
    <p>
      We can use your existing building as
      a visual reference. AI-generated
      details may differ from the original.
    </p>
  </div>

  <div class="card faq">
    <h3>HOW FAST IS DELIVERY?</h3>
    <p>
      Our proposed turnaround target is
      24 hours after receiving complete,
      approved project materials.
    </p>
  </div>

  <div class="card faq">
    <h3>IS THIS AN ARCHITECTURAL RENDERING?</h3>
    <p>
      This is conceptual marketing content,
      not a dimensionally verified
      architectural or engineering model.
    </p>
  </div>

</section>

</div>

<section class="cta">

  <div class="wrap">

    <div class="eyebrow">
      CRE MARKET / BUILD MOTION
    </div>

    <h2>
      STOP EXPLAINING THE VISION.<br>
      SHOW IT.
    </h2>

    <p>
      One property. One cinematic reveal.
      One flat price.
    </p>

    <a class="btn"
       href="mailto:projects@cremarket.io?subject=Build%20Motion%20Project%20Inquiry">
      START YOUR PROJECT — $499
    </a>

  </div>

</section>

<div class="wrap">
<footer>
  <span>
    © CRE MARKET · VISION
  </span>

  <span>
    Concept visualization only ·
    <a href="https://cremarket.io">
      CREMARKET.io
    </a>
  </span>
</footer>
</div>

</body>
</html>
"""

@app.get("/")
def home():
    return Response(HOME_HTML, mimetype="text/html")

@app.get("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "CRE MARKET Build Motion"
    })


