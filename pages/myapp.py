import streamlit as st

st.set_page_config(page_title="مستكشف الأسماء التجارية", layout="wide", page_icon="🔍")

st.markdown("""
<style>
    body { direction: rtl; }
    .stApp { background: linear-gradient(135deg, #050d1a, #0a1628); color: #e2e8f0; }
    .name-card {
        background: linear-gradient(135deg, #0d2137, #060e1c);
        border: 1px solid #1e3d5c;
        border-radius: 13px;
        padding: 16px;
        margin-bottom: 10px;
        text-align: right;
    }
    .ar-name { font-size: 22px; font-weight: 900; color: #f0f7ff; }
    .en-name { font-size: 14px; color: #4fc3f7; font-weight: 600; }
    .badge { display: inline-block; padding: 2px 8px; border-radius: 5px; font-size: 11px; margin-left: 4px; }
</style>
""", unsafe_allow_html=True)

names = [
    {"ar": "بصيرة البيانات", "en": "Baseera Data", "cat": "أثر وتأثير", "lang": "عربي", "feel": "ملهم"},
    {"ar": "أثير", "en": "Atheer", "cat": "أثر وتأثير", "lang": "عربي", "feel": "قوي"},
    {"ar": "وقع", "en": "Waq", "cat": "أثر وتأثير", "lang": "عربي", "feel": "قوي"},
    {"ar": "أثر البيانات", "en": "Data Impact", "cat": "أثر وتأثير", "lang": "عربي", "feel": "مباشر"},
    {"ar": "صدى البيانات", "en": "Data Echo", "cat": "أثر وتأثير", "lang": "عربي", "feel": "ملهم"},
    {"ar": "بصمة", "en": "Basma", "cat": "أثر وتأثير", "lang": "عربي", "feel": "قوي"},
    {"ar": "تحول", "en": "Tahawwul", "cat": "أثر وتأثير", "lang": "عربي", "feel": "ملهم"},
    {"ar": "فارق", "en": "Fareq", "cat": "أثر وتأثير", "lang": "عربي", "feel": "قوي"},
    {"ar": "مسار", "en": "Masaar", "cat": "أثر وتأثير", "lang": "عربي", "feel": "واضح"},
    {"ar": "رسوخ", "en": "Rusoukh", "cat": "أثر وتأثير", "lang": "عربي", "feel": "موثوق"},
    {"ar": "بصيرة", "en": "Baseera", "cat": "رؤية وبصيرة", "lang": "عربي", "feel": "راقي"},
    {"ar": "رؤيا", "en": "Ruya", "cat": "رؤية وبصيرة", "lang": "عربي", "feel": "ملهم"},
    {"ar": "أفق البيانات", "en": "Data Horizon", "cat": "رؤية وبصيرة", "lang": "عربي", "feel": "طموح"},
    {"ar": "منظور", "en": "Manzour", "cat": "رؤية وبصيرة", "lang": "عربي", "feel": "احترافي"},
    {"ar": "مرصد", "en": "Marsad", "cat": "رؤية وبصيرة", "lang": "عربي", "feel": "علمي"},
    {"ar": "عمق", "en": "Umq", "cat": "رؤية وبصيرة", "lang": "عربي", "feel": "قوي"},
    {"ar": "كاشف", "en": "Kashif", "cat": "رؤية وبصيرة", "lang": "عربي", "feel": "مباشر"},
    {"ar": "منارة البيانات", "en": "Data Lighthouse", "cat": "نور وإضاءة", "lang": "عربي", "feel": "ملهم"},
    {"ar": "بيانار", "en": "Bayānar", "cat": "نور وإضاءة", "lang": "عربي", "feel": "فريد"},
    {"ar": "نور البيانات", "en": "Data Light", "cat": "نور وإضاءة", "lang": "عربي", "feel": "دافئ"},
    {"ar": "ضياء", "en": "Diyaa", "cat": "نور وإضاءة", "lang": "عربي", "feel": "راقي"},
    {"ar": "شعاع", "en": "Shuaa", "cat": "نور وإضاءة", "lang": "عربي", "feel": "ملهم"},
    {"ar": "فجر البيانات", "en": "Data Dawn", "cat": "نور وإضاءة", "lang": "عربي", "feel": "طموح"},
    {"ar": "إشراق", "en": "Ishraq", "cat": "نور وإضاءة", "lang": "عربي", "feel": "راقي"},
    {"ar": "دلالة", "en": "Dalalah", "cat": "معرفة وعلم", "lang": "عربي", "feel": "عميق"},
    {"ar": "حكمة البيانات", "en": "Data Wisdom", "cat": "معرفة وعلم", "lang": "عربي", "feel": "راقي"},
    {"ar": "مدرك", "en": "Mudrik", "cat": "معرفة وعلم", "lang": "عربي", "feel": "ذكي"},
    {"ar": "إدراك", "en": "Idrak", "cat": "معرفة وعلم", "lang": "عربي", "feel": "عميق"},
    {"ar": "نبض البيانات", "en": "Data Pulse", "cat": "حياة ونبض", "lang": "عربي", "feel": "ديناميكي"},
    {"ar": "رواء البيانات", "en": "Data Rawaa", "cat": "حياة ونبض", "lang": "عربي", "feel": "جميل"},
    {"ar": "إيقاع البيانات", "en": "Data Rhythm", "cat": "حياة ونبض", "lang": "عربي", "feel": "إبداعي"},
    {"ar": "سداد", "en": "Sadaad", "cat": "قرار ونجاح", "lang": "عربي", "feel": "موثوق"},
    {"ar": "إنجاز", "en": "Injaz", "cat": "قرار ونجاح", "lang": "عربي", "feel": "ملهم"},
    {"ar": "ارتقاء", "en": "Irtiqaa", "cat": "قرار ونجاح", "lang": "عربي", "feel": "طموح"},
    {"ar": "DataImpact", "en": "DataImpact", "cat": "Impact & Power", "lang": "إنجليزي", "feel": "مباشر"},
    {"ar": "DataForce", "en": "DataForce", "cat": "Impact & Power", "lang": "إنجليزي", "feel": "قوي"},
    {"ar": "DataEdge", "en": "DataEdge", "cat": "Impact & Power", "lang": "إنجليزي", "feel": "تنافسي"},
    {"ar": "DataRise", "en": "DataRise", "cat": "Impact & Power", "lang": "إنجليزي", "feel": "طموح"},
    {"ar": "DataSpark", "en": "DataSpark", "cat": "Impact & Power", "lang": "إنجليزي", "feel": "ملهم"},
    {"ar": "DataWave", "en": "DataWave", "cat": "Impact & Power", "lang": "إنجليزي", "feel": "ديناميكي"},
    {"ar": "DataShift", "en": "DataShift", "cat": "Impact & Power", "lang": "إنجليزي", "feel": "تحويلي"},
    {"ar": "DataPeak", "en": "DataPeak", "cat": "Impact & Power", "lang": "إنجليزي", "feel": "طموح"},
    {"ar": "DataPulse", "en": "DataPulse", "cat": "Impact & Power", "lang": "إنجليزي", "feel": "حيوي"},
    {"ar": "DataDrive", "en": "DataDrive", "cat": "Impact & Power", "lang": "إنجليزي", "feel": "محفز"},
    {"ar": "Datanar", "en": "Datanar", "cat": "Impact & Power", "lang": "إنجليزي", "feel": "فريد"},
    {"ar": "Insightora", "en": "Insightora", "cat": "Vision & Intelligence", "lang": "إنجليزي", "feel": "احترافي"},
    {"ar": "DataGlow", "en": "DataGlow", "cat": "Vision & Intelligence", "lang": "إنجليزي", "feel": "مضيء"},
    {"ar": "DataLens", "en": "DataLens", "cat": "Vision & Intelligence", "lang": "إنجليزي", "feel": "دقيق"},
    {"ar": "DataClarity", "en": "DataClarity", "cat": "Vision & Intelligence", "lang": "إنجليزي", "feel": "وضوح"},
    {"ar": "DataMind", "en": "DataMind", "cat": "Vision & Intelligence", "lang": "إنجليزي", "feel": "ذكي"},
    {"ar": "DataBeacon", "en": "DataBeacon", "cat": "Vision & Intelligence", "lang": "إنجليزي", "feel": "إرشادي"},
    {"ar": "DataFlow", "en": "DataFlow", "cat": "Vision & Intelligence", "lang": "إنجليزي", "feel": "سلس"},
    {"ar": "DataAcademy", "en": "DataAcademy", "cat": "Growth & Training", "lang": "إنجليزي", "feel": "تعليمي"},
    {"ar": "DataLab", "en": "DataLab", "cat": "Growth & Training", "lang": "إنجليزي", "feel": "تطبيقي"},
    {"ar": "DataLeap", "en": "DataLeap", "cat": "Growth & Training", "lang": "إنجليزي", "feel": "طفرة"},
    {"ar": "DataBoost", "en": "DataBoost", "cat": "Growth & Training", "lang": "إنجليزي", "feel": "تسريع"},
    {"ar": "DataEvolve", "en": "DataEvolve", "cat": "Growth & Training", "lang": "إنجليزي", "feel": "تطور"},
    {"ar": "DataForward", "en": "DataForward", "cat": "Growth & Training", "lang": "إنجليزي", "feel": "تقدم"},
    {"ar": "بصيرة BI", "en": "Baseera BI", "cat": "مزيج", "lang": "مزيج", "feel": "احترافي"},
    {"ar": "داتاوي", "en": "Datawi", "cat": "مزيج", "lang": "مزيج", "feel": "فريد"},
    {"ar": "داتا رواء", "en": "Data Rawaa", "cat": "مزيج", "lang": "مزيج", "feel": "راقي"},
    {"ar": "داتا نارة", "en": "Datanara", "cat": "مزيج", "lang": "مزيج", "feel": "مضيء"},
    {"ar": "أثر داتا", "en": "Athar Data", "cat": "مزيج", "lang": "مزيج", "feel": "قوي"},
    {"ar": "نبض داتا", "en": "Nabdh Data", "cat": "مزيج", "lang": "مزيج", "feel": "حيوي"},
    {"ar": "أفق داتا", "en": "Ufuq Data", "cat": "مزيج", "lang": "مزيج", "feel": "طموح"},
    {"ar": "داتا فجر", "en": "Data Fajr", "cat": "مزيج", "lang": "مزيج", "feel": "بداية"},
    {"ar": "داتا نور", "en": "Data Noor", "cat": "مزيج", "lang": "مزيج", "feel": "محلي"},
]

# ===== Sidebar Filters =====
st.sidebar.markdown("## 🎛️ الفلاتر")

search = st.sidebar.text_input("🔍 بحث", placeholder="ابحث بالعربي أو English")

all_langs = ["الكل"] + sorted(set(n["lang"] for n in names))
lang_filter = st.sidebar.selectbox("🌐 اللغة", all_langs)

all_cats = ["الكل"] + sorted(set(n["cat"] for n in names))
cat_filter = st.sidebar.selectbox("📁 الفئة", all_cats)

all_feels = ["الكل"] + sorted(set(n["feel"] for n in names))
feel_filter = st.sidebar.selectbox("💡 الشعور", all_feels)

# ===== Filter Logic =====
filtered = [
    n for n in names
    if (search.lower() in n["ar"].lower() or search.lower() in n["en"].lower())
    and (lang_filter == "الكل" or n["lang"] == lang_filter)
    and (cat_filter == "الكل" or n["cat"] == cat_filter)
    and (feel_filter == "الكل" or n["feel"] == feel_filter)
]

# ===== Header =====
st.markdown(f"""
<div style='text-align:right; direction:rtl; padding: 20px 0 10px'>
    <h1 style='background: linear-gradient(90deg,#4fc3f7,#ce93d8); -webkit-background-clip: text; color: #4fc3f7; font-size:28px'>
        🔍 مستكشف الأسماء التجارية
    </h1>
    <p style='color:#7ea8cc'>يعرض <b style="color:#4fc3f7">{len(filtered)}</b> اسم من أصل <b>{len(names)}</b></p>
</div>
""", unsafe_allow_html=True)

# ===== Display Cards =====
if not filtered:
    st.warning("لا توجد نتائج — جرّب فلتراً آخر 🔍")
else:
    lang_emoji = {"عربي": "🇯🇴", "إنجليزي": "🌐", "مزيج": "✨"}
    lang_color = {"عربي": "#4fc3f7", "إنجليزي": "#69f0ae", "مزيج": "#ce93d8"}

    cols = st.columns(3)
    for i, n in enumerate(filtered):
        col = cols[i % 3]
        color = lang_color.get(n["lang"], "#4fc3f7")
        emoji = lang_emoji.get(n["lang"], "🌐")
        with col:
            st.markdown(f"""
            <div style='
                background: linear-gradient(135deg, #0d2137, #060e1c);
                border: 1px solid #1e3d5c;
                border-right: 3px solid {color};
                border-radius: 12px;
                padding: 14px;
                margin-bottom: 10px;
                direction: rtl;
                text-align: right;
            '>
                <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:8px'>
                    <span style='font-size:10px; background:{color}20; color:{color}; padding:2px 7px; border-radius:5px; font-weight:700'>{emoji} {n["lang"]}</span>
                    <span style='font-size:10px; background:rgba(255,255,255,0.05); color:#7ea8cc; padding:2px 7px; border-radius:5px'>{n["feel"]}</span>
                </div>
                <div style='font-size:20px; font-weight:900; color:#f0f7ff; margin-bottom:3px'>{n["ar"]}</div>
                <div style='font-size:13px; color:{color}; font-weight:600; letter-spacing:0.6px; margin-bottom:6px'>{n["en"]}</div>
                <div style='font-size:10px; color:#3d6a8a'>📁 {n["cat"]}</div>
            </div>
            """, unsafe_allow_html=True)