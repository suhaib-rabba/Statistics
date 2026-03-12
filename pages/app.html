import { useState, useMemo } from "react";

const names = [
  { ar: "بصيرة البيانات", en: "Baseera Data", cat: "أثر وتأثير", lang: "ar", feel: "ملهم" },
  { ar: "أثير", en: "Atheer", cat: "أثر وتأثير", lang: "ar", feel: "قوي" },
  { ar: "وَقْع", en: "Waq", cat: "أثر وتأثير", lang: "ar", feel: "قوي" },
  { ar: "أثر البيانات", en: "Data Impact", cat: "أثر وتأثير", lang: "ar", feel: "مباشر" },
  { ar: "صدى البيانات", en: "Data Echo", cat: "أثر وتأثير", lang: "ar", feel: "ملهم" },
  { ar: "بَصْمة", en: "Basma", cat: "أثر وتأثير", lang: "ar", feel: "قوي" },
  { ar: "نقش", en: "Naqsh", cat: "أثر وتأثير", lang: "ar", feel: "فريد" },
  { ar: "تحوّل", en: "Tahawwul", cat: "أثر وتأثير", lang: "ar", feel: "ملهم" },
  { ar: "فارق", en: "Fareq", cat: "أثر وتأثير", lang: "ar", feel: "قوي" },
  { ar: "مسار", en: "Masaar", cat: "أثر وتأثير", lang: "ar", feel: "واضح" },
  { ar: "تأثير", en: "Taatheer", cat: "أثر وتأثير", lang: "ar", feel: "مباشر" },
  { ar: "رسوخ", en: "Rusoukh", cat: "أثر وتأثير", lang: "ar", feel: "موثوق" },
  { ar: "بصيرة", en: "Baseera", cat: "رؤية وبصيرة", lang: "ar", feel: "راقي" },
  { ar: "رؤيا", en: "Ruya", cat: "رؤية وبصيرة", lang: "ar", feel: "ملهم" },
  { ar: "أفق البيانات", en: "Data Horizon", cat: "رؤية وبصيرة", lang: "ar", feel: "طموح" },
  { ar: "منظور", en: "Manzour", cat: "رؤية وبصيرة", lang: "ar", feel: "احترافي" },
  { ar: "مَرصَد", en: "Marsad", cat: "رؤية وبصيرة", lang: "ar", feel: "علمي" },
  { ar: "عمق", en: "Umq", cat: "رؤية وبصيرة", lang: "ar", feel: "قوي" },
  { ar: "كاشف", en: "Kashif", cat: "رؤية وبصيرة", lang: "ar", feel: "مباشر" },
  { ar: "مُبصِر", en: "Mubsir", cat: "رؤية وبصيرة", lang: "ar", feel: "واضح" },
  { ar: "منارة البيانات", en: "Data Lighthouse", cat: "نور وإضاءة", lang: "ar", feel: "ملهم" },
  { ar: "بيانار", en: "Bayānar", cat: "نور وإضاءة", lang: "ar", feel: "فريد" },
  { ar: "نور البيانات", en: "Data Light", cat: "نور وإضاءة", lang: "ar", feel: "دافئ" },
  { ar: "ضياء", en: "Diyaa", cat: "نور وإضاءة", lang: "ar", feel: "راقي" },
  { ar: "إنارة", en: "Inara", cat: "نور وإضاءة", lang: "ar", feel: "دافئ" },
  { ar: "شعاع", en: "Shuaa", cat: "نور وإضاءة", lang: "ar", feel: "ملهم" },
  { ar: "فجر البيانات", en: "Data Dawn", cat: "نور وإضاءة", lang: "ar", feel: "طموح" },
  { ar: "إشراق", en: "Ishraq", cat: "نور وإضاءة", lang: "ar", feel: "راقي" },
  { ar: "توهّج", en: "Tawahuj", cat: "نور وإضاءة", lang: "ar", feel: "ديناميكي" },
  { ar: "دلالة", en: "Dalalah", cat: "معرفة وعلم", lang: "ar", feel: "عميق" },
  { ar: "حِكمة البيانات", en: "Data Wisdom", cat: "معرفة وعلم", lang: "ar", feel: "راقي" },
  { ar: "مدرك", en: "Mudrik", cat: "معرفة وعلم", lang: "ar", feel: "ذكي" },
  { ar: "واعٍ", en: "Waai", cat: "معرفة وعلم", lang: "ar", feel: "توعوي" },
  { ar: "إدراك", en: "Idrak", cat: "معرفة وعلم", lang: "ar", feel: "عميق" },
  { ar: "خبرة البيانات", en: "Data Expertise", cat: "معرفة وعلم", lang: "ar", feel: "احترافي" },
  { ar: "نبض البيانات", en: "Data Pulse", cat: "حياة ونبض", lang: "ar", feel: "ديناميكي" },
  { ar: "رواء البيانات", en: "Data Rawaa", cat: "حياة ونبض", lang: "ar", feel: "جميل" },
  { ar: "دفق", en: "Dafaq", cat: "حياة ونبض", lang: "ar", feel: "ديناميكي" },
  { ar: "إيقاع البيانات", en: "Data Rhythm", cat: "حياة ونبض", lang: "ar", feel: "إبداعي" },
  { ar: "ينبوع البيانات", en: "Data Spring", cat: "حياة ونبض", lang: "ar", feel: "دافئ" },
  { ar: "سداد", en: "Sadaad", cat: "قرار ونجاح", lang: "ar", feel: "موثوق" },
  { ar: "إنجاز", en: "Injaz", cat: "قرار ونجاح", lang: "ar", feel: "ملهم" },
  { ar: "ارتقاء", en: "Irtiqaa", cat: "قرار ونجاح", lang: "ar", feel: "طموح" },
  { ar: "تفوّق", en: "Tafawwuq", cat: "قرار ونجاح", lang: "ar", feel: "طموح" },
  { ar: "داتا إمباكت", en: "DataImpact", cat: "Impact & Power", lang: "en", feel: "مباشر" },
  { ar: "داتا فورس", en: "DataForce", cat: "Impact & Power", lang: "en", feel: "قوي" },
  { ar: "داتا إيدج", en: "DataEdge", cat: "Impact & Power", lang: "en", feel: "تنافسي" },
  { ar: "داتا رايز", en: "DataRise", cat: "Impact & Power", lang: "en", feel: "طموح" },
  { ar: "داتا ويف", en: "DataWave", cat: "Impact & Power", lang: "en", feel: "ديناميكي" },
  { ar: "داتا شيفت", en: "DataShift", cat: "Impact & Power", lang: "en", feel: "تحويلي" },
  { ar: "داتا سبارك", en: "DataSpark", cat: "Impact & Power", lang: "en", feel: "ملهم" },
  { ar: "داتا فلير", en: "DataFlare", cat: "Impact & Power", lang: "en", feel: "ديناميكي" },
  { ar: "داتا بولس", en: "DataPulse", cat: "Impact & Power", lang: "en", feel: "حيوي" },
  { ar: "داتا درايف", en: "DataDrive", cat: "Impact & Power", lang: "en", feel: "محفز" },
  { ar: "داتا بيك", en: "DataPeak", cat: "Impact & Power", lang: "en", feel: "طموح" },
  { ar: "داتا ستورم", en: "DataStorm", cat: "Impact & Power", lang: "en", feel: "قوي" },
  { ar: "داتا فيوز", en: "DataFuse", cat: "Impact & Power", lang: "en", feel: "ذكي" },
  { ar: "بيانار", en: "Datanar", cat: "Impact & Power", lang: "en", feel: "فريد" },
  { ar: "إنسايتورا", en: "Insightora", cat: "Vision & Intelligence", lang: "en", feel: "احترافي" },
  { ar: "داتا غلو", en: "DataGlow", cat: "Vision & Intelligence", lang: "en", feel: "مضيء" },
  { ar: "داتا لنز", en: "DataLens", cat: "Vision & Intelligence", lang: "en", feel: "دقيق" },
  { ar: "داتا فيجن", en: "DataVision", cat: "Vision & Intelligence", lang: "en", feel: "رؤية" },
  { ar: "داتا كلاريتي", en: "DataClarity", cat: "Vision & Intelligence", lang: "en", feel: "وضوح" },
  { ar: "داتا مايند", en: "DataMind", cat: "Vision & Intelligence", lang: "en", feel: "ذكي" },
  { ar: "داتا بيكون", en: "DataBeacon", cat: "Vision & Intelligence", lang: "en", feel: "إرشادي" },
  { ar: "لوسيدا داتا", en: "Lucida Data", cat: "Vision & Intelligence", lang: "en", feel: "راقي" },
  { ar: "داتا فلو", en: "DataFlow", cat: "Vision & Intelligence", lang: "en", feel: "سلس" },
  { ar: "داتا اكاديمي", en: "DataAcademy", cat: "Growth & Training", lang: "en", feel: "تعليمي" },
  { ar: "داتا لاب", en: "DataLab", cat: "Growth & Training", lang: "en", feel: "تطبيقي" },
  { ar: "داتا نيكست", en: "DataNext", cat: "Growth & Training", lang: "en", feel: "مستقبلي" },
  { ar: "داتا ليب", en: "DataLeap", cat: "Growth & Training", lang: "en", feel: "طفرة" },
  { ar: "داتا بوست", en: "DataBoost", cat: "Growth & Training", lang: "en", feel: "تسريع" },
  { ar: "داتافورد", en: "DataForward", cat: "Growth & Training", lang: "en", feel: "تقدم" },
  { ar: "داتا إيفولف", en: "DataEvolve", cat: "Growth & Training", lang: "en", feel: "تطور" },
  { ar: "بصيرة BI", en: "Baseera BI", cat: "مزيج", lang: "mix", feel: "احترافي" },
  { ar: "داتاوي", en: "Datawi", cat: "مزيج", lang: "mix", feel: "فريد" },
  { ar: "داتا رواء", en: "Data Rawaa", cat: "مزيج", lang: "mix", feel: "راقي" },
  { ar: "داتا نارة", en: "Datanara", cat: "مزيج", lang: "mix", feel: "مضيء" },
  { ar: "داتا أثير", en: "Data Atheer", cat: "مزيج", lang: "mix", feel: "عميق" },
  { ar: "داتا فجر", en: "Data Fajr", cat: "مزيج", lang: "mix", feel: "بداية" },
  { ar: "أثر داتا", en: "Athar Data", cat: "مزيج", lang: "mix", feel: "قوي" },
  { ar: "نبض داتا", en: "Nabdh Data", cat: "مزيج", lang: "mix", feel: "حيوي" },
  { ar: "أفق داتا", en: "Ufuq Data", cat: "مزيج", lang: "mix", feel: "طموح" },
  { ar: "داتا نور", en: "Data Noor", cat: "مزيج", lang: "mix", feel: "محلي" },
];

const langColors = {
  ar: { bg: "#0d2137", accent: "#4fc3f7" },
  en: { bg: "#0d2118", accent: "#69f0ae" },
  mix: { bg: "#1e0d26", accent: "#ce93d8" },
};

const langLabels = { all: "الكل", ar: "🇯🇴 عربي", en: "🌐 إنجليزي", mix: "✨ مزيج" };

export default function App() {
  const [search, setSearch] = useState("");
  const [lang, setLang] = useState("all");
  const [cat, setCat] = useState("الكل");
  const [feel, setFeel] = useState("الكل");
  const [favorites, setFavorites] = useState([]);
  const [showFavs, setShowFavs] = useState(false);
  const [copied, setCopied] = useState(null);

  const categories = useMemo(() => ["الكل", ...new Set(names.map(n => n.cat))], []);
  const feels = useMemo(() => ["الكل", ...new Set(names.map(n => n.feel))], []);

  const filtered = useMemo(() => names.filter(n =>
    (n.ar.includes(search) || n.en.toLowerCase().includes(search.toLowerCase())) &&
    (lang === "all" || n.lang === lang) &&
    (cat === "الكل" || n.cat === cat) &&
    (feel === "الكل" || n.feel === feel)
  ), [search, lang, cat, feel]);

  const display = showFavs ? names.filter(n => favorites.includes(n.en)) : filtered;
  const toggleFav = en => setFavorites(p => p.includes(en) ? p.filter(f => f !== en) : [...p, en]);
  const copy = (text, key) => { navigator.clipboard?.writeText(text); setCopied(key); setTimeout(() => setCopied(null), 1500); };

  const btnBase = (active, color) => ({
    padding: "5px 11px", borderRadius: 20, border: `1px solid ${active ? color : "#2d5a8e"}`,
    background: active ? color + "25" : "transparent", color: active ? color : "#7ea8cc",
    cursor: "pointer", fontSize: 11, fontWeight: active ? 700 : 400
  });

  return (
    <div style={{ minHeight: "100vh", background: "linear-gradient(135deg,#050d1a,#0a1628)", fontFamily: "Tahoma,sans-serif", color: "#e2e8f0", direction: "rtl" }}>

      {/* Header */}
      <div style={{ background: "linear-gradient(90deg,#0f2744,#1a3a5c,#0f2744)", borderBottom: "2px solid #1e4976", padding: "20px 20px 14px", position: "sticky", top: 0, zIndex: 100, boxShadow: "0 4px 24px rgba(0,0,0,0.6)" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 12 }}>
          <div>
            <div style={{ fontSize: 20, fontWeight: 900, background: "linear-gradient(90deg,#4fc3f7,#ce93d8,#69f0ae)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>
              🔍 مستكشف الأسماء التجارية
            </div>
            <div style={{ fontSize: 11, color: "#7ea8cc", marginTop: 2 }}>{display.length} اسم معروض من أصل {names.length}</div>
          </div>
          <button onClick={() => setShowFavs(!showFavs)} style={{ background: showFavs ? "linear-gradient(135deg,#c2185b,#e91e63)" : "linear-gradient(135deg,#1e4976,#2d6a9f)", border: "none", color: "#fff", padding: "8px 16px", borderRadius: 10, cursor: "pointer", fontWeight: 700, fontSize: 12 }}>
            ❤️ مفضلتي ({favorites.length})
          </button>
        </div>

        <input value={search} onChange={e => setSearch(e.target.value)} placeholder="🔍 ابحث بالعربي أو English..."
          style={{ width: "100%", padding: "9px 12px", background: "rgba(255,255,255,0.06)", border: "1px solid #2d5a8e", borderRadius: 9, color: "#e2e8f0", fontSize: 13, outline: "none", boxSizing: "border-box", marginBottom: 10 }} />

        <div style={{ display: "flex", gap: 5, flexWrap: "wrap", marginBottom: 6 }}>
          {Object.entries(langLabels).map(([k, v]) => <button key={k} onClick={() => setLang(k)} style={btnBase(lang === k, "#4fc3f7")}>{v}</button>)}
          <span style={{ color: "#2d5a8e", padding: "0 2px", alignSelf: "center" }}>|</span>
          {feels.map(f => <button key={f} onClick={() => setFeel(f)} style={btnBase(feel === f, "#ce93d8")}>{f}</button>)}
        </div>

        <div style={{ display: "flex", gap: 5, flexWrap: "wrap" }}>
          {categories.map(c => <button key={c} onClick={() => setCat(c)} style={btnBase(cat === c, "#69f0ae")}>{c}</button>)}
        </div>
      </div>

      {/* Cards Grid */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill,minmax(220px,1fr))", gap: 10, padding: "14px 16px 40px" }}>
        {display.map((n, i) => {
          const C = langColors[n.lang];
          const isFav = favorites.includes(n.en);
          return (
            <div key={n.en + i} style={{ background: `linear-gradient(135deg,${C.bg},#060e1c)`, border: `1px solid #1e3d5c`, borderRadius: 13, padding: "14px 13px", position: "relative", overflow: "hidden", transition: "all 0.2s" }}
              onMouseEnter={e => { e.currentTarget.style.border = `1px solid ${C.accent}55`; e.currentTarget.style.transform = "translateY(-2px)"; e.currentTarget.style.boxShadow = `0 6px 20px ${C.accent}15`; }}
              onMouseLeave={e => { e.currentTarget.style.border = "1px solid #1e3d5c"; e.currentTarget.style.transform = "none"; e.currentTarget.style.boxShadow = "none"; }}>

              <div style={{ position: "absolute", top: 0, right: 0, width: 3, height: "100%", background: `linear-gradient(180deg,${C.accent},transparent)`, borderRadius: "0 13px 13px 0" }} />

              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 9 }}>
                <div style={{ display: "flex", gap: 4 }}>
                  <span style={{ padding: "2px 6px", borderRadius: 5, fontSize: 9, fontWeight: 700, background: C.accent + "20", color: C.accent }}>
                    {n.lang === "ar" ? "🇯🇴 عربي" : n.lang === "en" ? "🌐 EN" : "✨ Mix"}
                  </span>
                  <span style={{ padding: "2px 6px", borderRadius: 5, fontSize: 9, background: "rgba(255,255,255,0.05)", color: "#7ea8cc" }}>{n.feel}</span>
                </div>
                <button onClick={() => toggleFav(n.en)} style={{ background: "none", border: "none", cursor: "pointer", fontSize: 15, filter: isFav ? "none" : "grayscale(1) opacity(0.3)", padding: 0 }}>❤️</button>
              </div>

              <div style={{ fontSize: 18, fontWeight: 900, color: "#f0f7ff", marginBottom: 2, lineHeight: 1.3 }}>{n.ar}</div>
              <div style={{ fontSize: 12, color: C.accent, fontWeight: 600, letterSpacing: 0.6, marginBottom: 6 }}>{n.en}</div>
              <div style={{ fontSize: 9, color: "#3d6a8a", marginBottom: 10 }}>📁 {n.cat}</div>

              <div style={{ display: "flex", gap: 5 }}>
                <button onClick={() => copy(n.ar, i)} style={{ flex: 1, padding: "5px", borderRadius: 6, border: `1px solid ${C.accent}30`, background: copied === i ? C.accent + "18" : "transparent", color: C.accent, cursor: "pointer", fontSize: 10, fontWeight: 600 }}>
                  {copied === i ? "✅ نُسخ" : "📋 نسخ"}
                </button>
                <button onClick={() => copy(n.en, i + 500)} style={{ flex: 1, padding: "5px", borderRadius: 6, border: "1px solid #2d5a8e", background: "transparent", color: "#6a9fcc", cursor: "pointer", fontSize: 10 }}>
                  {copied === i + 500 ? "✅ Done" : "📋 Copy"}
                </button>
              </div>
            </div>
          );
        })}
      </div>

      {display.length === 0 && (
        <div style={{ textAlign: "center", padding: 60, color: "#4a7a9b" }}>
          <div style={{ fontSize: 36, marginBottom: 10 }}>🔍</div>
          <div>لا توجد نتائج — جرّب فلتراً آخر</div>
        </div>
      )}
    </div>
  );
}