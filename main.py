import streamlit as st
import pyodbc

# ── Database connection ──────────────────────────────────────────
def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=stats-server-suhaib.database.windows.net;'
        'DATABASE=stats-db;'
        'UID=sqladmin;'
        'PWD=Stats@2026!;'
        'Encrypt=yes;'
        'TrustServerCertificate=no;'
        'Connection Timeout=30;'
    )
    return conn

# ── Page config ──────────────────────────────────────────────────
st.set_page_config(page_title="Students Database", page_icon="🎓")
st.title("🎓 Students Information")
st.markdown("---")

# ── Input Form ───────────────────────────────────────────────────
st.subheader("➕ Add New Student")

name        = st.text_input("Full Name",     placeholder="e.g. Ahmad Al-Rashid")
email       = st.text_input("Email",         placeholder="e.g. ahmad@example.com")
phone       = st.text_input("Phone Number",  placeholder="e.g. 0791234567")

st.markdown("---")

# ── Submit Button ────────────────────────────────────────────────
if st.button("💾 Save to Database", use_container_width=True):
    if not name:
        st.error("❌ Name is required!")
    else:
        try:
            conn   = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO [Students Information] (Name, Email, PhoneNumber) VALUES (?, ?, ?)",
                (name, email, phone)
            )
            conn.commit()
            conn.close()
            st.success(f"✅ Student '{name}' added successfully!")
            st.balloons()
        except Exception as e:
            st.error(f"❌ Error: {e}")

st.markdown("---")

# ── View All Students ────────────────────────────────────────────
st.subheader("📋 All Students")

if st.button("🔄 Load Students", use_container_width=True):
    try:
        conn   = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [Students Information]")
        rows    = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()

        if rows:
            import pandas as pd
            df = pd.DataFrame.from_records(rows, columns=columns)
            st.dataframe(df, use_container_width=True)
            st.info(f"Total students: {len(df)}")
        else:
            st.warning("No students found in the database yet.")
    except Exception as e:
        st.error(f"❌ Connection Error: {e}")