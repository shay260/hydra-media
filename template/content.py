FOOT_LABEL = "בטיחות במטווח"
ICONS.update({
 "finger": '<path d="M24 58h40a8 8 0 0 0 0-16H44"/><path d="M24 58V40a10 10 0 0 1 10-10h30"/><path d="M24 58c0 14 10 24 24 24h12"/><line x1="64" y1="30" x2="88" y2="30"/>',
 "guard": '<path d="M30 30h44v14c0 16-10 26-24 26S30 60 30 52z"/><path d="M50 30v18"/><path d="M22 30h60"/>',
 "warn": '<path d="M50 12L90 84H10z"/><line x1="50" y1="40" x2="50" y2="60"/><circle cx="50" cy="71" r="2"/>',
 "range": '<circle cx="50" cy="50" r="36"/><circle cx="50" cy="50" r="20"/><circle cx="50" cy="50" r="5"/>',
 "repeat": '<path d="M78 40a30 30 0 0 0-54-10"/><path d="M22 14v16h16"/><path d="M22 60a30 30 0 0 0 54 10"/><path d="M78 86V70H62"/>',
 "tag": '<circle cx="36" cy="34" r="12"/><path d="M14 80c0-14 10-24 22-24s22 10 22 24"/><circle cx="70" cy="40" r="9"/><path d="M58 80c0-10 6-18 14-18s14 8 14 18"/>',
})

SLIDES = [
 '<div class="kick">בטיחות במטווח</div><h1>דבר אחד<br>שהייתי מתקן<br><span class="hl">אצל כל יורה</span></h1><div class="line"></div><p><b>איפה האצבע נמצאת.</b></p>',
 f'{icon("finger",140)}<h2>כבר בשליפה</h2><p>הרבה יורים מכניסים את האצבע לשמורת ההדק כבר בשליפה, <b>עוד לפני שהקנה מופנה למטרה.</b></p>',
 f'{icon("guard",140)}<h2>למה זה קורה</h2><p>היד רוצה להיות מוכנה לירות. <b>בלי הרגל נכון, האצבע נכנסת לשם מעצמה.</b></p>',
 f'{icon("range",140)}<h2>אצבע ישרה<br><span class="hl">על הצינה</span></h2><p>האצבע היורה נשארת מחוץ לשמורת ההדק, <b>עד שתמונת הכוונות על המטרה והחלטתם לירות.</b></p>',
 f'{icon("warn",140)}<h2>בלחץ, במעידה<br><span class="hl">או בבהלה</span></h2><p>כף היד נסגרת מעצמה. אם האצבע כבר בתוך שמורת ההדק, התנועה הזו מספיקה כדי לסחוט את ההדק, <b>וזו פליטת כדור.</b></p>',
 f'{icon("repeat",140)}<h2>בהתחלה זה<br><span class="hl">מרגיש לא טבעי</span></h2><p>אחרי כמה אימונים במטווח <b>האצבע תחזור לצינה בלי שתחשבו על זה.</b></p>',
 f'{icon("tag",140)}<h1 style="font-size:88px;margin-top:30px">תייגו את מי<br><span class="hl">שמגיע איתכם<br>למטווח</span></h1><div class="line"></div><p>כדי שגם הוא יזכור: <b>אצבע על הצינה עד שהחלטתם לירות.</b></p>',
]

FB = f"""<html dir="rtl"><head><meta charset="utf-8"><style>{CSS}
.list{{margin-top:56px;display:flex;flex-direction:column;gap:40px}}
.row{{display:flex;align-items:flex-start;gap:30px;font-size:42px;line-height:1.3;color:#E9E4D8}}
.n{{flex:none;width:68px;height:68px;border:4px solid {ACC};border-radius:50%;display:flex;align-items:center;justify-content:center;color:{ACC};font-weight:800;font-size:36px}}
.row b{{color:#fff;display:block;font-size:50px}}
</style></head><body><div class="grid"></div><div class="glow"></div>
<div class="top"><img class="logo" src="{LOGO}"><span class="num">בטיחות במטווח</span></div>
<div class="wrap" style="justify-content:flex-start;top:220px">
<h1 style="font-size:96px">איפה האצבע<br><span class="hl">שלכם נמצאת?</span></h1>
<div class="list">
<div class="row"><span class="n">1</span><span><b>בשליפה</b>מחוץ לשמורת ההדק</span></div>
<div class="row"><span class="n">2</span><span><b>עד שהחלטתם לירות</b>ישרה על הצינה</span></div>
<div class="row"><span class="n">3</span><span><b>בלחץ כף היד נסגרת</b>והאצבע סוחטת את ההדק</span></div>
<div class="row"><span class="n">4</span><span><b>בונים הרגל</b>בכל מקצה במטווח</span></div>
</div></div>
<div class="foot"><span>אצבע על הצינה עד שהחלטתם לירות</span></div>
<div class="bar" style="width:100%"></div></body></html>"""
