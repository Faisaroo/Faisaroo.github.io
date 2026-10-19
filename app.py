from flask import Flask, request, render_template

app = Flask(__name__)

# بيانات الخبرات والشهادات والـ Sketchfab
my_sections = [
    {
        "id": "ibm-cert",
        "title": "شهادة IBM المعتمدة",
        "subtitle": "Python for Data Science, AI & Development",
        "category": "الذكاء الاصطناعي وتحليل البيانات",
        "desc": "إتمام البرنامج التدريبي واجتياز المشروع النهائي الموثق من IBM عبر Coursera باسم فيصل أحمد محمد الجهني.",
        "cert_id": "4OT6I02NBI3S",
        "date": "17 أغسطس 2026",
        "theme": "ibm",
        "bg_color": "#090d16",
        "accent_color": "#2563eb"
    },
    {
        "id": "blender-3d",
        "title": "نمذجة وتحريك Blender 3D",
        "category": "تطوير الألعاب والجرافيكس",
        "desc": "تصميم ونمذجة أصول ثلاثية الأبعاد، الـ UV Unwrapping، والرفع المباشر لمنصة Sketchfab لتجربة تفاعلية.",
        "sketchfab_embed": "https://sketchfab.com/models/embed", # نموذج افتراضي أو رابط نموذجك
        "theme": "blender",
        "bg_color": "#120b08",
        "accent_color": "#f97316"
    },
    {
        "id": "futurex",
        "title": "FutureX - المنصة الوطنية للتعليم",
        "category": "تطوير الويب والمنصات",
        "desc": "المشاركة البرمجية في تصميم وتطوير الأنظمة التعليمية الرقمية وفق معايير الحكومة الرقمية.",
        "theme": "futurex",
        "bg_color": "#051610",
        "accent_color": "#10b981"
    },
    {
        "id": "linux-sys",
        "title": "Linux Mint & Server Management",
        "category": "الشبكات وأنظمة التشغيل",
        "desc": "إدارة سيرفرات لينكس بسعة 24GB رام، إعداد جدار الحماية UFW، وتوجيه حركة البيانات عبر SSH Tunneling.",
        "theme": "linux",
        "bg_color": "#0c0a09",
        "accent_color": "#eab308"
    }
]

@app.route('/')
def home():
    return render_template('index.html', sections=my_sections)

@app.route('/projects/view')
def view_project():
    clicked_id = request.args.get('id')
    for s in my_sections:
        if s["id"] == clicked_id:
            return f"""
            <body style='background:{s["bg_color"]}; color:white; font-family:sans-serif; padding:50px; max-width:800px; margin:auto;' dir='rtl'>
                <h1 style='color:{s["accent_color"]};'>{s['title']}</h1>
                <h3 style='color:#94a3b8;'>التصنيف: {s['category']}</h3>
                <p style='font-size:18px; line-height:1.6;'>{s['desc']}</p>
                <br><br>
                <a href='/' style='background:{s["accent_color"]}; color:white; padding:10px 20px; text-decoration:none; border-radius:8px;'>← العودة للرئيسية</a>
            </body>
            """
    return "<h1>العنصر غير موجود (404)</h1>"

if __name__ == '__main__':
    app.run(debug=True)