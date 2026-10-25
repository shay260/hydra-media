FOOT_LABEL = "בחירת נרתיק"
ICONS.update({
 "guard": '<path d="M30 30h44v14c0 16-10 26-24 26S30 60 30 52z"/><path d="M50 30v18"/><path d="M22 30h60"/>',
 "fit": '<path d="M20 18h44l16 16v48H20z"/><path d="M34 52l10 10 20-22"/>',
 "lock": '<rect x="24" y="44" width="52" height="40" rx="6"/><path d="M34 44V32a16 16 0 0 1 32 0v12"/><line x1="50" y1="60" x2="50" y2="70"/>',
 "open": '<path d="M28 16v48a22 22 0 0 0 44 0V16"/><path d="M20 16h16M64 16h16"/>',
 "hand": '<path d="M30 52V30a6 6 0 0 1 12 0v18M42 46V24a6 6 0 0 1 12 0v22M54 46V28a6 6 0 0 1 12 0v26c0 18-10 30-26 30-10 0-16-6-22-16l-6-12a6 6 0 0 1 10-6l8 10"/>',
 "warn": '<path d="M50 12L90 84H10z"/><line x1="50" y1="40" x2="50" y2="60"/><circle cx="50" cy="71" r="2"/>',
 "range": '<circle cx="50" cy="50" r="36"/><circle cx="50" cy="50" r="20"/><circle cx="50" cy="50" r="5"/>',
})

def crit(n, ic, title, text):
    return (f'<div style="display:flex;align-items:center;justify-content:space-between">{icon(ic,140)}'
            f'<span style="font-size:30px;font-weight:700;color:{ACC};letter-spacing:.06em">קריטריון {n} מתוך 5</span></div>'
            f'<h2>{title}</h2><p>{text}</p>')

SLIDES = [
 '<div class="kick">לנושאי נשק</div><h1>שלושה נרתיקים<br>עד שמצאתם<br><span class="hl">את הנכון?</span></h1><div class="line"></div><p>מה שעולה זול, לרוב משלמים עליו ביוקר.<br><b>ככה בוחרים נכון כבר מהראשון.</b></p>',
 '<h1 style="font-size:96px">האקדח עליכם<br><span class="hl">כל היום.</span></h1><div class="line"></div><p>עם נרתיק טוב <b>כמעט לא מרגישים אותו.</b> והנרתיק הוא גם מה ששומר שההדק מכוסה והאקדח נשאר במקום.</p>',
 crit(1,"guard","שמורת ההדק מכוסה","חומר קשיח שמכסה את כל שמורת ההדק. <b>אם אפשר להגיע להדק דרך הנרתיק, הנרתיק לא מתאים.</b>"),
 crit(2,"fit","בנוי לאקדח שלכם","נרתיק שנבנה לדגם המדויק. רוב הנרתיקים האוניברסליים גדולים ומסיביים. <b>יש פנס או כוונת השלכה? הנרתיק צריך להיות בנוי גם להם.</b>"),
 crit(3,"lock","מחזיק גם בתנועה","האקדח לא זז כשרצים, מתכופפים או יוצאים מהרכב. <b>הוא יוצא רק כשאתם שולפים.</b>"),
 crit(4,"open","נשאר פתוח אחרי השליפה","פתח הנרתיק לא קורס. <b>ככה מחזירים את האקדח ביד אחת, ושום בד או רצועה לא נכנסים לשמורת ההדק.</b>"),
 crit(5,"hand","אחיזה מלאה כבר בפנים","שקע כף היד נצמד לשקע ידית האחיזה עוד כשהאקדח בנרתיק. <b>אם הנרתיק חוסם את היד, השליפה מתחילה באחיזה לא נכונה.</b>"),
 f'{icon("warn",150)}<h2 style="font-size:80px">ומה קורה כשהנרתיק<br><span class="hl">לא טוב?</span></h2>'
 '<p>ההדק חשוף.<br>האקדח זז, ולפעמים נופל.<br>השליפה איטית ומתחילה באחיזה לא נכונה.<br><b>ובסוף קונים עוד נרתיק.</b></p>',
 f'{icon("range",130)}<h1 style="font-size:88px;margin-top:30px">כמה נרתיקים<br><span class="hl">עברתם עד שמצאתם<br>את שלכם?</span></h1><div class="line"></div><p>ספרו בתגובות. ולפני שסומכים על נרתיק חדש, <b>בודקים אותו במטווח עם המדריך.</b></p>',
]

FB = f"""<html dir="rtl"><head><meta charset="utf-8"><style>{CSS}
.list{{margin-top:48px;display:flex;flex-direction:column;gap:32px}}
.row{{display:flex;align-items:flex-start;gap:30px;font-size:42px;line-height:1.3;color:#E9E4D8}}
.n{{flex:none;width:68px;height:68px;border:4px solid {ACC};border-radius:50%;display:flex;align-items:center;justify-content:center;color:{ACC};font-weight:800;font-size:36px}}
.row b{{color:#fff;display:block;font-size:50px}}
</style></head><body><div class="grid"></div><div class="glow"></div>
<div class="top"><img class="logo" src="{LOGO}"><span class="num">לנושאי נשק</span></div>
<div class="wrap" style="justify-content:flex-start;top:220px">
<h1 style="font-size:92px">5 קריטריונים<br><span class="hl">לבחירת נרתיק</span></h1>
<div class="list">
<div class="row"><span class="n">1</span><span><b>שמורת ההדק מכוסה</b>חומר קשיח, בלי גישה להדק</span></div>
<div class="row"><span class="n">2</span><span><b>בנוי לאקדח שלכם</b>ולכל מה שמותקן עליו</span></div>
<div class="row"><span class="n">3</span><span><b>מחזיק גם בתנועה</b>ומשחרר רק בשליפה</span></div>
<div class="row"><span class="n">4</span><span><b>נשאר פתוח</b>להחזרה ביד אחת</span></div>
<div class="row"><span class="n">5</span><span><b>אחיזה מלאה</b>כבר כשהאקדח בנרתיק</span></div>
</div></div>
<div class="foot"><span>לפני שסומכים על נרתיק חדש, בודקים אותו במטווח עם המדריך</span></div>
<div class="bar" style="width:100%"></div></body></html>"""
