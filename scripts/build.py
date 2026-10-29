#!/usr/bin/env python3
"""Builds brightpost.org v1 (static, no third-party scripts) into ./site."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "site"

LOGO = """<svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">
  <path d="M24 13 L2 6 L2 20 Z" fill="#E9A93B" opacity=".45"/>
  <path d="M24 13 L46 6 L46 20 Z" fill="#E9A93B" opacity=".45"/>
  <path d="M19 9 L24 4 L29 9 Z" fill="currentColor"/>
  <rect x="19.5" y="9.5" width="9" height="7" rx="1" fill="#E9A93B"/>
  <path d="M19 17 H29 L31.5 42 H16.5 Z" fill="currentColor"/>
  <path d="M18.3 25 H29.7 L30.2 30 H17.8 Z" fill="#E9A93B" opacity=".9"/>
  <rect x="12" y="42" width="24" height="3" rx="1.5" fill="currentColor"/>
</svg>"""

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="10" fill="#14213D"/>""" + \
    LOGO.split(">", 1)[1].replace("currentColor", "#F7F5EF").replace('aria-hidden="true" focusable="false"', "")

NAV = [("index.html", "Home"), ("covered.html", "What we cover"), ("diagnosis.html", "Getting a diagnosis"),
       ("resources.html", "Find support"), ("tools.html", "Tools"), ("about.html", "About")]

DISCLAIMER = """<p class="disclaimer"><strong>BrightPost is a guide, not a clinic.</strong> We aren't licensed psychologists, doctors or lawyers, and nothing on this site is a diagnosis, treatment or medical, psychological or legal advice. We point you to the people and organizations who can help. Always check details with them, since services and phone numbers change.</p>
<p class="crisis">In danger right now? Call 911. In a mental-health crisis, call or text 988, or chat at <a href="https://chat.988lifeline.org/">chat.988lifeline.org</a>.</p>"""


def page(fname, title, desc, body, hero=None):
    nav = "\n".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a></li>' for h, t in NAV)
    hero_html = hero or ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preload" href="fonts/atkinson-hyperlegible-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="soon"><div class="wrap"><strong>Opening soon.</strong> BrightPost is being built with the neurodivergent community. The guides below are ready to use; the help desk comes next.</div></div>
<header class="site"><div class="wrap">
<a class="brand" href="index.html">{LOGO}<span>BrightPost</span></a>
<nav class="main" aria-label="Main"><ul>
{nav}
</ul></nav>
</div></header>
{hero_html}
<main id="main"><div class="wrap">
{body}
</div></main>
<footer class="site"><div class="wrap">
{DISCLAIMER}
<p class="small">BrightPost is planned as a program of GOVW Foundation, Inc. No cookies, no trackers, no third-party scripts. Text set in Atkinson Hyperlegible, made by the Braille Institute for easy reading.</p>
</div></footer>
</body>
</html>
"""


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------- Home ----------
home_hero = """<section class="hero"><div class="wrap">
<h1>A light for every <span class="beam">kind of mind.</span></h1>
<p class="lead">BrightPost is a guide for the neurodivergent community and the people who support it: how to get a diagnosis, where to find help, and tools that make the day easier.</p>
</div></section>"""

home = """
<div class="cards">
  <div class="card"><h3>Getting a diagnosis</h3><p>Who can diagnose, how to ask for a free evaluation through Early Intervention or your public school, and ways to get seen sooner.</p><a class="go" href="diagnosis.html">Start here</a></div>
  <div class="card"><h3>Find support</h3><p>Organizations for autism, ADHD, learning differences, Tourette and more, including groups run by autistic people, parent centers and legal help.</p><a class="go" href="resources.html">See the list</a></div>
  <div class="card"><h3>What we cover</h3><p>Autism, ADHD, learning differences and closely related conditions. If yours isn't one of them, we'll point you to who can help.</p><a class="go" href="covered.html">See what's included</a></div>
  <div class="card"><h3>Tools</h3><p>Maze Cat, a task list with a timer that floats over your taskbar, and more tools on the way.</p><a class="go" href="tools.html">Try Maze Cat</a></div>
</div>

<div class="prose">
<h2>Different wiring, real strengths</h2>
<p>We see neurodivergence as a difference, not a defect. Many people find strengths in the way their mind works, and we build for those strengths instead of trying to change people.</p>

<h2>How we work</h2>
<ul>
  <li><strong>Nothing about us without us.</strong> Neurodivergent people help design and test everything here.</li>
  <li><strong>Self-identification counts.</strong> You don't need a diagnosis to use our guides or tools.</li>
  <li><strong>Calm by default.</strong> Quiet colors, no pop-ups, no flashing, no surprise sounds.</li>
  <li><strong>At no cost.</strong> The guides and tools are open to anyone who needs them.</li>
  <li><strong>Your data stays yours.</strong> This site doesn't track you.</li>
</ul>
</div>
"""

# ---------- Covered ----------
covered = """
<div class="prose page-title">
<p class="kicker">What we cover</p>
<h1>Autism, ADHD and closely related conditions</h1>
<p>BrightPost focuses on neurodevelopmental differences: the ones that start in childhood and shape how a person learns, moves, communicates or pays attention. These often show up together, so we cover them as a group.</p>
</div>

<div class="table-scroll"><table class="stack">
<thead><tr><th>Condition</th><th>In a few words</th><th>Where to start</th></tr></thead>
<tbody>
<tr><td data-label="Condition"><strong>Autism (ASD)</strong>, including what used to be called Asperger's</td><td data-label="In a few words">Differences in social communication, plus focused interests, routines or sensory differences.</td><td data-label="Where to start"><a href="diagnosis.html#children">Getting a diagnosis</a> · <a href="resources.html#autism">Autism groups</a></td></tr>
<tr><td data-label="Condition"><strong>ADHD</strong></td><td data-label="In a few words">Ongoing patterns of inattention, hyperactivity or impulsivity that started in childhood.</td><td data-label="Where to start"><a href="diagnosis.html#adults">Adults</a> · <a href="resources.html#adhd">ADHD groups</a></td></tr>
<tr><td data-label="Condition"><strong>Learning differences</strong>: dyslexia, dyscalculia, dysgraphia</td><td data-label="In a few words">Persistent difficulty with reading, math or writing that isn't explained by teaching or effort.</td><td data-label="Where to start"><a href="diagnosis.html#school">School evaluations</a> · <a href="resources.html#learning">Learning groups</a></td></tr>
<tr><td data-label="Condition"><strong>Dyspraxia</strong> (developmental coordination disorder)</td><td data-label="In a few words">Difficulty planning and coordinating movement, from handwriting to sports.</td><td data-label="Where to start"><a href="diagnosis.html#who">Who can diagnose</a></td></tr>
<tr><td data-label="Condition"><strong>Tourette syndrome and tic disorders</strong></td><td data-label="In a few words">Repeated movements or sounds (tics) that are hard to hold back.</td><td data-label="Where to start"><a href="resources.html#tics">Tourette groups</a></td></tr>
<tr><td data-label="Condition"><strong>Sensory processing differences</strong></td><td data-label="In a few words">Being over- or under-sensitive to sound, touch, light and more. Not a separate diagnosis in the main manuals, but common with autism and ADHD.</td><td data-label="Where to start"><a href="resources.html#sensory">Sensory resources</a></td></tr>
<tr><td data-label="Condition"><strong>Developmental language disorder (DLD)</strong></td><td data-label="In a few words">Lasting difficulty learning, understanding and using language, not explained by hearing loss or autism.</td><td data-label="Where to start">A speech-language pathologist evaluation · <a href="resources.html#language">Language resources</a></td></tr>
<tr><td data-label="Condition"><strong>Intellectual disability</strong></td><td data-label="In a few words">Differences in learning and everyday skills that start in childhood.</td><td data-label="Where to start"><a href="resources.html#idd">The Arc and other groups</a></td></tr>
<tr><td data-label="Condition"><strong>Twice-exceptional (2e)</strong></td><td data-label="In a few words">Gifted children and adults who also have ADHD, autism or a learning difference.</td><td data-label="Where to start"><a href="resources.html#twice">2e resources</a></td></tr>
<tr><td data-label="Condition"><strong>OCD</strong></td><td data-label="In a few words">Unwanted, repeated thoughts and the urge to do things to ease them. Often seen alongside autism, ADHD and tics.</td><td data-label="Where to start"><a href="resources.html#ocd">OCD resources</a></td></tr>
</tbody></table></div>

<div class="prose">
<h2>What we don't cover</h2>
<p>We aren't a general mental-health service. For the conditions below, these places can help you find care:</p>
<ul>
<li>Depression, anxiety on its own, bipolar disorder, psychosis, eating disorders, trauma and PTSD, and substance use: the <strong>SAMHSA National Helpline</strong>, 1-800-662-4357, free and open 24/7, gives treatment referrals and information (it isn't counseling). <a href="https://findtreatment.gov/">FindTreatment.gov</a> lists state-licensed treatment near you.</li>
<li>Dementia and brain injury: start with your doctor.</li>
<li>Any crisis: call or text <strong>988</strong>, or call <strong>911</strong> if someone is in danger.</li>
</ul>
<div class="note">Not sure where you fit? You don't have to know. Self-identification counts here, and the people in our <a href="resources.html">support list</a> can help you sort it out.</div>
</div>
"""

# ---------- Diagnosis ----------
diagnosis = """
<div class="prose page-title">
<p class="kicker">Getting a diagnosis</p>
<h1>How to get a diagnosis, and how to get it sooner</h1>
<p>A diagnosis can open doors to support at school, at work and in health care. It can also take a long time. Here's what the official sources say, in plain words. This guide is for the United States.</p>
<div class="alert"><strong>Good to know first</strong>Children don't need a diagnosis to get Early Intervention or school services, and you can ask for those evaluations yourself, for free. Start them at the same time as the medical route, not after.</div>
<div class="toc"><strong>On this page</strong><ul>
<li><a href="#children">Children: from first worries to an evaluation</a></li>
<li><a href="#school">School evaluations and Section 504</a></li>
<li><a href="#who">Who can diagnose</a></li>
<li><a href="#adults">Adults</a></li>
<li><a href="#faster">Ways to speed it up</a></li>
<li><a href="#costs">Costs and insurance</a></li>
</ul></div>

<h2 id="children">Children: from first worries to an evaluation</h2>
<ol class="steps">
<li><strong>Ask your child's doctor about screening.</strong> The American Academy of Pediatrics recommends autism screening at the 18- and 24-month checkups, and general developmental screening at 9, 18 and 30 months. You can ask for a screening at any time you're worried. A screening doesn't diagnose; it shows whether a full evaluation is needed. CDC's free milestone checklists help you bring notes.</li>
<li><strong>Ask for a referral to a specialist</strong> if there may be a delay.</li>
<li><strong>Under age 3: call your state's Early Intervention program yourself.</strong> You don't need a doctor's referral or a diagnosis. The evaluation is free, and the program has 45 days from your call to finish it and hold the first planning meeting. Find your state's number on <a href="https://www.cdc.gov/act-early/early-intervention/contact-information-by-state.html">CDC's Early Intervention contact list</a>.</li>
<li><strong>Age 3 and up: contact your local public elementary school</strong>, even if your child doesn't go there. Say you have concerns and want an evaluation for special education. If staff don't know the process, ask for the special-education director.</li>
</ol>

<h2 id="school">School evaluations and Section 504</h2>
<ul>
<li><strong>You can ask at any time.</strong> A school can't use tiered-support programs (often called MTSS or RTI) to delay or deny an evaluation when a disability is suspected.</li>
<li><strong>Put it in writing.</strong> A short, dated letter that names your child, describes your concerns with examples, lists what's been tried, and includes any outside reports. Keep a copy. The federal Center for Parent Information and Resources has a <a href="https://www.parentcenterhub.org/evaluation-2/">sample letter</a>.</li>
<li><strong>Know the clock.</strong> Under federal rules, the evaluation must be done within 60 days of the day you sign consent (not the day you ask), unless your state sets a different deadline.</li>
<li><strong>If the school says no,</strong> it must explain why in writing and tell you your rights. You can challenge the decision. Your state's <a href="https://www.parentcenterhub.org/find-your-center/">Parent Center</a> can help, at no cost.</li>
<li><strong>Section 504</strong> covers students whose condition substantially limits a major life activity. A medical diagnosis isn't required, and having one doesn't guarantee a plan on its own.</li>
<li><strong>Gifted and neurodivergent (2e)?</strong> The U.S. Department of Education has said that high ability alone can't rule a child out. A child who has a disability and needs special education still qualifies, and schools must use more than one test to decide.</li>
</ul>

<h2 id="who">Who can diagnose</h2>
<ul>
<li><strong>Autism:</strong> developmental pediatricians, child psychologists or psychiatrists, child neurologists, often with speech and occupational therapists. For adults: a psychologist, psychiatrist or neuropsychologist with autism experience.</li>
<li><strong>ADHD:</strong> a psychologist, a psychiatrist, or a primary care provider such as a pediatrician. There's no single test; the provider gathers input from family, teachers and others, and checks hearing and vision.</li>
<li><strong>Learning differences:</strong> usually a school team (school psychologist, special-education staff, speech-language pathologist, reading specialist).</li>
<li><strong>Developmental language disorder:</strong> a speech-language pathologist.</li>
<li><strong>Tics and Tourette:</strong> a provider familiar with tic disorders.</li>
<li><strong>Dyspraxia:</strong> a team that may include pediatricians, neurologists and physical or occupational therapists.</li>
</ul>

<h2 id="adults">Adults</h2>
<ul>
<li><strong>Start with your primary care provider</strong> and ask for a referral to someone experienced with adults.</li>
<li><strong>Bring your history.</strong> ADHD symptoms must have started before age 12, so school reports, old records and memories from people who knew you as a child all help.</li>
<li><strong>It's often harder for adults,</strong> because traits overlap with anxiety and other conditions, and many people, especially women and girls, were missed as children. More than half of U.S. adults with ADHD were diagnosed at 18 or older.</li>
<li><strong>At work,</strong> you may be able to ask for reasonable accommodations under the ADA. The <a href="https://askjan.org/">Job Accommodation Network</a> gives free, confidential advice: (800) 526-7234.</li>
<li><strong>Telehealth</strong> is common for adult ADHD care. Federal rules allowing some controlled medicines to be prescribed without an in-person visit are extended through December 31, 2026; check with your provider about what applies to you.</li>
</ul>

<h2 id="faster">Ways to speed it up</h2>
<ol class="steps">
<li><strong>Start every route at once.</strong> Ask for the medical referral, and contact Early Intervention or the school the same week.</li>
<li><strong>Don't wait for a diagnosis to get help.</strong> Therapy for a specific need, such as speech therapy for a language delay, can often start before the evaluation.</li>
<li><strong>Under 3, Early Intervention may be the fastest door</strong> to an evaluation.</li>
<li><strong>Join more than one waitlist,</strong> and leave the others once one comes through.</li>
<li><strong>Ask about university training clinics.</strong> Supervised graduate students do the testing, often on a sliding scale (many don't take insurance).</li>
<li><strong>Ask about community evaluators</strong> and your primary care office, which can sometimes see young children sooner than big centers.</li>
<li><strong>Check your insurance first:</strong> is the evaluation covered, and do you need a referral?</li>
<li><strong>Bring a folder:</strong> written examples of what you've noticed, milestone checklists, school reports and any earlier evaluations.</li>
</ol>

<h2 id="costs">Costs and insurance</h2>
<ul>
<li><strong>Free public evaluations:</strong> Early Intervention (under 3) and public-school evaluations are at no cost to families. Some later Early Intervention services may have sliding-scale fees, depending on the state.</li>
<li><strong>Medicaid</strong> covers screening, diagnosis and treatment for enrolled children and young people under 21.</li>
<li><strong>Private insurance:</strong> every state has some kind of autism coverage law, but most cover children only, and many employer plans that pay claims themselves ("self-funded" plans) are exempt. Ask your plan directly.</li>
</ul>

<div class="sources"><h3>Sources</h3>
<p><a href="https://www.cdc.gov/act-early/families/concerned.html">CDC: Concerned about your child's development?</a> · <a href="https://www.cdc.gov/autism/diagnosis/index.html">CDC: Screening for autism</a> · <a href="https://www.cdc.gov/autism/treatment/accessing-services.html">CDC: Accessing services for autism</a> · <a href="https://www.ecfr.gov/current/title-34/subtitle-B/chapter-III/part-303/subpart-D/subject-group-ECFR821570af41ca511/section-303.310">34 CFR 303.310 (45-day timeline)</a> · <a href="https://sites.ed.gov/idea/regs/b/d/300.301">34 CFR 300.301 (60-day timeline)</a> · <a href="https://sites.ed.gov/idea/files/rts-qa-child-find-part-b-08-24-2021.pdf">U.S. Dept. of Education: Child Find</a> · <a href="https://www.ed.gov/laws-and-policy/civil-rights-laws/disability-discrimination/frequently-asked-questions-section-504-free-appropriate-public-education-fape">U.S. Dept. of Education: Section 504 FAQ</a> · <a href="https://sites.ed.gov/idea/idea-files/policy-letter-december-20-2013-to-dr-jim-delisle/">OSEP Letter to Delisle (2e)</a> · <a href="https://www.cdc.gov/adhd/diagnosis/index.html">CDC: Diagnosing ADHD</a> · <a href="https://www.nimh.nih.gov/health/publications/autism-spectrum-disorder">NIMH: Autism</a> · <a href="https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know">NIMH: ADHD in adults</a> · <a href="https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm">CDC MMWR: ADHD in adults (2024)</a> · <a href="https://www.nichd.nih.gov/health/topics/learning/conditioninfo/diagnosed">NICHD: Learning disabilities</a> · <a href="https://www.nidcd.nih.gov/health/specific-language-impairment">NIDCD: Developmental language disorder</a> · <a href="https://www.cdc.gov/tourette-syndrome/diagnosis/index.html">CDC: Diagnosing tic disorders</a> · <a href="https://www.hhs.gov/press-room/dea-telemedicine-extension-2026.html">HHS: Telemedicine extension</a> · <a href="https://www.medicaid.gov/medicaid/benefits/early-and-periodic-screening-diagnostic-and-treatment">Medicaid.gov: EPSDT</a> · <a href="https://www.seattlechildrens.org/healthcare-professionals/provider-news/evaluation-autism-sooner/">Seattle Children's: Evaluation sooner</a> · <a href="https://autismnj.org/article/waitlists-for-an-autism-evaluation-what-you-can-do-while-you-wait/">Autism New Jersey: While you wait</a>. Checked October 29, 2026.</p></div>
</div>
"""

# ---------- Resources ----------
ORGS = [
    ("autism", "Autism", [
        ("Autistic Self Advocacy Network (ASAN)", "https://autisticadvocacy.org/about-asan/", "Run by and for autistic people. Policy work, self-advocacy toolkits and plain-language guides.", "Email info@autisticadvocacy.org", "Autistic-led"),
        ("Autism Society of America", "https://autismsociety.org/contact-us/", "National helpline and local affiliates for information, referrals and support. Not a crisis line.", "1-800-328-8476", ""),
        ("Organization for Autism Research (OAR)", "https://researchautism.org/", "Free guidebooks, scholarships for autistic students and job-seeker programs.", "(866) 366-9710", ""),
        ("Autistic Women & Nonbinary Network (AWN)", "https://awnnetwork.org/about/", "Community and resources for autistic women, girls, nonbinary, trans and Two Spirit people.", "", ""),
        ("Autism Speaks", "https://www.autismspeaks.org/", "Large advocacy and research-funding group with an Autism Response Team for family information and referrals. Some autistic advocates, including ASAN, criticize its leadership, spending and messaging; it has since dropped the goal of a cure from its mission.", "", ""),
    ]),
    ("adhd", "ADHD", [
        ("CHADD: National Resource Center on ADHD", "https://chadd.org/about/about-nrc/", "Evidence-based information, webinars and parent toolkits, funded mainly through the CDC. It doesn't give counseling or refer you to specific professionals.", "1-866-200-8098, Mon–Fri 1–5 pm ET, Spanish available", ""),
        ("Attention Deficit Disorder Association (ADDA)", "https://add.org/", "Focused on adults with ADHD: online peer support groups, webinars and workplace resources.", "Online contact form", ""),
    ]),
    ("learning", "Learning differences", [
        ("Learning Disabilities Association of America (LDA)", "https://ldaamerica.org/", "Information, state resources and advocacy for learning disabilities and ADHD.", "(412) 341-1515", ""),
        ("Understood", "https://www.understood.org/about/our-mission", "Nonprofit guides, tools and community for ADHD, dyslexia and other kinds of neurodivergence.", "", "Leadership includes ND people"),
        ("International Dyslexia Association (IDA)", "https://dyslexiaida.org/provider-directories/", "Directory of evaluators, tutors and advocates. IDA doesn't vet the providers listed.", "", ""),
        ("National Center for Learning Disabilities (NCLD)", "https://ncld.org/", "Policy, research and resources for parents, young adults and educators.", "", ""),
    ]),
    ("language", "Language", [
        ("NIDCD: Developmental language disorder", "https://www.nidcd.nih.gov/health/specific-language-impairment", "Plain-language facts from the National Institutes of Health, including who evaluates DLD (a speech-language pathologist).", "", ""),
    ]),
    ("tics", "Tourette syndrome and tics", [
        ("Tourette Association of America", "https://tourette.org/resources/get-help-now/", "Toolkits for families and schools, a provider directory, chapters and support groups.", "888-4-TOURET, or web chat", ""),
    ]),
    ("sensory", "Sensory processing", [
        ("STAR Institute", "https://sensoryhealth.org/basic/about-spd", "Research, education and a treatment directory for sensory processing differences.", "Intake by online form", ""),
    ]),
    ("idd", "Intellectual and developmental disabilities", [
        ("The Arc of the United States", "https://thearc.org/find-a-chapter/", "Rights and support for people with intellectual and developmental disabilities and their families, with hundreds of state and local chapters.", "", ""),
    ]),
    ("twice", "Twice-exceptional (2e)", [
        ("Davidson Institute: 2e resource guide", "https://www.davidsongifted.org/gifted-blog/2e-guidebook-resources-and-bibliography/", "A free parent guide to twice-exceptionality: identification, school options, IEP and 504 plans, and social-emotional support.", "", ""),
    ]),
    ("ocd", "OCD", [
        ("International OCD Foundation (IOCDF)", "https://iocdf.org/ocd-finding-help/", "Searchable directory of over 2,000 therapists, clinics and support groups.", "(617) 973-5801", ""),
    ]),
    ("families", "Families", [
        ("Family Voices: Family-to-Family Health Information Centers", "https://familyvoices.org/", "Free help with health coverage and care, run by parents who've been there. In every state.", "", "Family-led"),
        ("Parent to Parent USA", "https://www.p2pusa.org/parents/", "Get matched one-to-one with an experienced parent for support.", "", "Parent-led"),
    ]),
    ("rights", "School and legal rights", [
        ("Parent Training and Information Centers", "https://www.parentcenterhub.org/find-your-center/", "Nearly 100 federally funded centers that help families with special education, at no cost.", "", ""),
        ("Protection & Advocacy agencies (NDRN)", "https://www.ndrn.org/about/ndrn-member-agencies/", "Legal advocacy agencies in every state for disability rights, including special education.", "", ""),
        ("Council of Parent Attorneys and Advocates (COPAA)", "https://www.copaa.org/page/about", "Directory of special-education attorneys and advocates. COPAA itself doesn't represent families.", "", ""),
        ("Office for Civil Rights (U.S. Dept. of Education)", "https://www.ed.gov/laws-and-policy/civil-rights-laws/file-complaint/how-file-discrimination-complaint-ocr", "Where to file a disability discrimination or Section 504 complaint against a school, usually within 180 days.", "", ""),
    ]),
    ("work", "Work", [
        ("Job Accommodation Network (JAN)", "https://askjan.org/", "Free, confidential advice on workplace accommodations, funded by the U.S. Department of Labor.", "(800) 526-7234", ""),
    ]),
    ("gov", "Government guides", [
        ("CDC: Learn the Signs. Act Early.", "https://www.cdc.gov/act-early/families/concerned.html", "Milestone checklists, the Milestone Tracker app and Early Intervention contacts by state.", "", ""),
        ("NIMH: Autism and ADHD", "https://www.nimh.nih.gov/health/publications/autism-spectrum-disorder", "Plain-language health information from the National Institute of Mental Health.", "", ""),
    ]),
]

res_parts = ["""
<div class="prose page-title">
<p class="kicker">Find support</p>
<h1>Organizations that can help</h1>
<p>A starting list of U.S. organizations, grouped by need. We don't endorse any of them or get anything for listing them, and we list a few you may have mixed feelings about, with a note on why. Phone numbers are as shown on each organization's own site; please check before you call.</p>
<div class="toc"><strong>Jump to</strong><ul>"""]
res_parts.append("".join(f'<li><a href="#{k}">{t}</a></li>' for k, t, _ in ORGS))
res_parts.append("</ul></div>")
for key, title, orgs in ORGS:
    res_parts.append(f'<h2 id="{key}">{title}</h2>')
    for name, url, what, contact, tag in orgs:
        t = f'<span class="tag">{tag}</span>' if tag else ""
        c = f"<p>{esc(contact)}</p>" if contact else ""
        res_parts.append(f'<div class="org"><h3><a href="{url}">{esc(name)}</a>{t}</h3><p>{esc(what)}</p>{c}</div>')
res_parts.append("""
<h2 id="crisis">Crisis and other help</h2>
<div class="org"><h3><a href="https://988lifeline.org/get-help/">988 Suicide &amp; Crisis Lifeline</a></h3><p>Free, confidential and open 24/7. Call or text 988, or chat online. In Spanish, press 2 or text AYUDA to 988.</p></div>
<div class="org"><h3><a href="https://www.samhsa.gov/find-help/helplines/national-helpline">SAMHSA National Helpline</a></h3><p>Free, 24/7 treatment referrals and information for mental health and substance use, in English and Spanish. It isn't counseling.</p><p>1-800-662-4357</p></div>
<div class="org"><h3>911</h3><p>When someone is in danger right now. Call if you can; text only where your area supports it.</p></div>
<p class="sources">List checked October 29, 2026. Know a group that should be here, or a link that's wrong? The help desk is coming soon; until then, write to help@govw.org.</p>
</div>""")
resources = "\n".join(res_parts)

# ---------- Tools ----------
tools = """
<div class="prose page-title">
<p class="kicker">Tools</p>
<h1>Tools for the day-to-day</h1>
<p>Small, calm tools made with neurodivergent people. Free to use, and your data stays on your device.</p>
</div>
<div class="cards">
<div class="card"><h3>Maze Cat</h3><p>Your task list and a timer that floats over the taskbar. Pick a task, press Start, and it stays in front of you until it's done. When time's up, the cat wakes up and a soft chime plays.</p><p>Windows. Open source (MIT license). Your lists are plain files on your computer.</p><a class="go" href="https://github.com/thornebrian/mazecat">Get Maze Cat on GitHub</a></div>
<div class="card"><h3>More on the way</h3><p>Quiet modes that pause notifications when it's all too much, help turning a long email into steps, and a shared look across every tool so nobody has to relearn anything.</p></div>
</div>
"""

# ---------- About ----------
about = """
<div class="prose page-title">
<p class="kicker">About</p>
<h1>About BrightPost</h1>
<p>BrightPost started with one person's own tools. Its founder built Maze Cat to stay on track, and it made enough of a difference to share. BrightPost grows that into a home for the neurodivergent community and the people who support it: clear guides, trusted links and calm tools.</p>
<p>A lighthouse doesn't steer the ship. It shows where the rocks are and where the harbor is, so you can choose your own way. That's the job we want to do.</p>

<h2>Who runs it</h2>
<p>BrightPost is planned as a program of GOVW Foundation, Inc., a nonprofit. We're building a team that includes neurodivergent people, families and educators, and we'll introduce them here as they join.</p>

<h2>What we are, and what we aren't</h2>
<ul>
<li>We <strong>are</strong> a guide: we explain the process in plain words and point you to the right people.</li>
<li>We <strong>aren't</strong> licensed psychologists, doctors or lawyers. We don't diagnose, treat or give medical, psychological or legal advice.</li>
<li>We don't accept payment for listing organizations.</li>
</ul>

<h2>Your privacy</h2>
<p>This site has no cookies, no trackers and no third-party scripts. A full privacy policy comes with the help desk.</p>

<h2>Contact</h2>
<p>A help desk is coming soon. Until then, write to help@govw.org.</p>
</div>
"""

PAGES = [
    ("index.html", "BrightPost", "A guide for the neurodivergent community: getting a diagnosis, finding support and calm tools.", home, home_hero),
    ("covered.html", "What we cover · BrightPost", "Autism, ADHD, learning differences and closely related conditions, and where to go for everything else.", covered, None),
    ("diagnosis.html", "Getting a diagnosis · BrightPost", "How to get an autism, ADHD or learning evaluation in the U.S., free options, and ways to get seen sooner.", diagnosis, None),
    ("resources.html", "Find support · BrightPost", "U.S. organizations for autism, ADHD, learning differences, Tourette, OCD, families and legal rights.", resources, None),
    ("tools.html", "Tools · BrightPost", "Maze Cat and other calm tools made with neurodivergent people.", tools, None),
    ("about.html", "About · BrightPost", "What BrightPost is, who runs it, and what it isn't.", about, None),
]

for fname, title, desc, body, hero in PAGES:
    (OUT / fname).write_text(page(fname, title, desc, body, hero), encoding="utf-8")

(OUT / "404.html").write_text(page("404.html", "Not found · BrightPost", "Page not found.",
    '<div class="prose page-title"><h1>This page isn\'t here</h1><p>The light still works, though. Try the <a href="index.html">home page</a>.</p></div>'), encoding="utf-8")
(OUT / "favicon.svg").write_text(FAVICON, encoding="utf-8")
(OUT / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
print("built", sorted(p.name for p in OUT.iterdir()))
