import base64, os, sys
from playwright.sync_api import sync_playwright

D = os.path.dirname(os.path.abspath(__file__))
F = D + "/fonts/fontsource-heebo-5.3.0/files/"
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
FONTS = "".join(
    f"@font-face{{font-family:H;font-weight:{w};src:url(data:font/woff2;base64,{b64(F+f'heebo-hebrew-{w}-normal.woff2')}) format('woff2');unicode-range:U+0590-05FF,U+FB1D-FB4F;}}"
    f"@font-face{{font-family:H;font-weight:{w};src:url(data:font/woff2;base64,{b64(F+f'heebo-latin-{w}-normal.woff2')}) format('woff2');}}"
    for w in (400, 500, 700, 800, 900))

ACC = "#CDA678"
RED = "#B3262B"
LOGO = "data:image/png;base64,"+b64(D+"/logo/logo_s.png")
ICONS = {
 "water": '<path d="M50 8C50 8 20 44 20 62a30 30 0 0 0 60 0C80 44 50 8 50 8z"/>',
 "light": '<rect x="18" y="38" width="44" height="24" rx="4"/><path d="M62 34l22-12v56L62 66z"/><line x1="30" y1="50" x2="46" y2="50"/>',
 "med": '<rect x="14" y="26" width="72" height="56" rx="8"/><path d="M38 26v-8h24v8"/><line x1="50" y1="40" x2="50" y2="68"/><line x1="36" y1="54" x2="64" y2="54"/>',
 "doc": '<path d="M26 10h34l18 18v62H26z"/><path d="M60 10v18h18"/><line x1="36" y1="50" x2="68" y2="50"/><line x1="36" y1="64" x2="68" y2="64"/>',
 "family": '<circle cx="34" cy="30" r="11"/><circle cx="68" cy="38" r="8"/><path d="M14 86c0-16 9-28 20-28s20 12 20 28"/><path d="M54 86c0-12 6-22 14-22s14 10 14 22"/>',
 "clock": '<circle cx="50" cy="50" r="38"/><path d="M50 26v24l16 10"/>',
 "pot": '<path d="M18 44h64v26a14 14 0 0 1-14 14H32a14 14 0 0 1-14-14z"/><line x1="10" y1="44" x2="90" y2="44"/><path d="M40 32c0-6 6-6 6-12M54 32c0-6 6-6 6-12"/>',
}
def icon(n, size=150):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" fill="none" stroke="{ACC}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">{ICONS[n]}</svg>'

CSS = FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html{{width:1080px;height:1350px;overflow:hidden}}
body{{width:1080px;height:1350px;font-family:H,'DejaVu Sans';direction:rtl;color:#F3EFE6;
 background:#0F110D;position:relative;overflow:hidden}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:60px 60px}}
.glow{{position:absolute;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(179,38,43,.16),transparent 65%);top:-320px;right:-320px}}
.top{{position:absolute;top:44px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center;font-size:26px;letter-spacing:.18em;font-weight:700;direction:ltr}}
.brand{{color:#F3EFE6}} .brand b{{color:{ACC}}}
.num{{color:#8C8a80;font-weight:500;letter-spacing:.1em}}
.bar{{position:absolute;bottom:0;right:0;height:14px;background:{RED}}}
.logo{{width:118px;height:auto;display:block}}
.foot{{position:absolute;bottom:64px;right:80px;left:80px;display:flex;justify-content:space-between;font-size:26px;color:#8C8a80;font-weight:500}}
.wrap{{position:absolute;top:190px;bottom:170px;right:80px;left:80px;display:flex;flex-direction:column;justify-content:center}}
.kick{{font-size:34px;font-weight:700;color:{ACC};letter-spacing:.02em;margin-bottom:28px}}
h1{{font-size:118px;line-height:1.02;font-weight:900;letter-spacing:-.01em}}
h2{{font-size:84px;line-height:1.08;font-weight:800;margin:36px 0 34px}}
p{{font-size:46px;line-height:1.45;font-weight:400;color:#D9D4C7}}
p b{{color:#fff;font-weight:700}}
.hl{{color:{ACC}}}
.chip{{display:inline-block;border:3px solid {ACC};color:{ACC};padding:10px 26px;border-radius:999px;font-size:30px;font-weight:700;margin-top:48px;align-self:flex-start}}
.line{{width:120px;height:8px;background:{ACC};margin:40px 0}}
"""

def page(n, total, body, swipe=True):
    FOOTTXT = FOOT_LABEL
    pct = n/total*100
    foot = '<span>החליקו ←</span>' if swipe else '<span>שמרו את הפוסט</span>'
    return f"""<html dir="rtl"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="grid"></div><div class="glow"></div>
<div class="top"><img class="logo" src="{LOGO}"><span class="num">{n:02d} / {total:02d}</span></div>
<div class="wrap">{body}</div>
<div class="foot"><span>{FOOTTXT}</span>{foot}</div>
<div class="bar" style="width:{pct}%"></div></body></html>"""

def item(ic, kick, title, text):
    return f'{icon(ic)}<h2>{title}</h2><p>{text}</p>'

exec(open(D+"/content.py").read())
out = D + "/out"; os.makedirs(out, exist_ok=True)
with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width":1080,"height":1350})
    T = len(SLIDES)
    for i, s in enumerate(SLIDES, 1):
        pg.set_content(page(i, T, s, swipe=i < T)); pg.wait_for_timeout(300)
        pg.screenshot(path=f"{out}/ig_{i:02d}.png")
    pg.set_content(FB); pg.wait_for_timeout(300)
    pg.screenshot(path=f"{out}/fb_checklist.png")
    br.close()
print("done")
