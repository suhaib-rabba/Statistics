# ============================================================
#  STUDENTS INFORMATION APP
#  Built with: Streamlit + pymssql + Azure SQL Database
#  Author: Suhaib
#  Date: 2026
# ============================================================

# ── IMPORTS ─────────────────────────────────────────────────
# streamlit  → the framework that turns Python into a web app
# pymssql    → the library that connects Python to SQL Server
# pandas     → the library that handles tables/dataframes



import streamlit as st
import pyodbc
import pandas as pd
# ============================================================
#  DATABASE CONNECTION FUNCTION
# ============================================================
# This function creates a connection to our Azure SQL database.
# We use st.secrets to hide sensitive info (server, password)
# so they are NOT visible in the code or on GitHub.
#
# st.secrets reads from:
#   - Locally:          .streamlit/secrets.toml file
#   - Streamlit Cloud:  Settings → Secrets section
#
# The secrets.toml file should look like this:
# -----------------------------------------------
# DB_SERVER   = "stats-server-suhaib.database.windows.net"
# DB_NAME     = "stats-db"
# DB_USER     = "sqladmin"
# DB_PASSWORD = "Stats@2026!"
# -----------------------------------------------
# NEVER put your real password directly in the code!
# ============================================================

def get_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 18 for SQL Server};'
            'SERVER=stats-server-suhaib.database.windows.net;'
            'DATABASE=stats-db;'
            'UID=sqladmin;'
            'PWD=Stats@2026!;'
            'Encrypt=yes;'
            'TrustServerCertificate=yes;'
        )
        return conn
    except Exception as e:
        st.error(f"❌ Database Connection Failed: {e}")
        return None
# ====================================
#  PAGE CONFIGURATION
# ============================================================
# set_page_config must be the FIRST streamlit command in the file.
# page_title → appears on the browser tab
# page_icon  → the emoji/icon on the browser tab
# layout     → "wide" uses the full screen width
# ============================================================

st.set_page_config(
    page_title="Students Database",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
#  PAGE HEADER
# ============================================================
# st.title    → big title at the top of the page
# st.markdown → renders markdown text. "---" creates a divider line
# ============================================================

st.title("🎓 Students Information System")
st.markdown("This app connects to an **Azure SQL Database** to store and display student information.")
st.markdown("---")


# ============================================================
#  SECTION 1: ADD NEW STUDENT FORM
# ============================================================
# st.subheader  → medium-sized section title
# st.text_input → creates a text box for user to type in
#   - First argument  = label shown above the box
#   - placeholder     = grey hint text inside the box
# ============================================================

st.subheader("➕ Add New Student")

# Create 3 columns to put inputs side by side
# This makes the layout cleaner on wide screens
col1, col2, col3 = st.columns(3)

with col1:
    # Name field — required, supports Arabic (nvarchar in DB)
    name = st.text_input(
        "Full Name *",
        placeholder="e.g. Ahmad Al-Rashid"
    )

with col2:
    # Email field — optional, max 255 chars (standard email length)
    email = st.text_input(
        "Email",
        placeholder="e.g. ahmad@example.com"
    )

with col3:
    # Phone field — optional, varchar(20) to support +962 format
    phone = st.text_input(
        "Phone Number",
        placeholder="e.g. 0791234567"
    )


# ============================================================
#  SAVE BUTTON
# ============================================================
# st.button → creates a clickable button
# When clicked, the code inside the if block runs
#
# use_container_width=True → button stretches to full width
#
# We use parameterized queries (%s) instead of string formatting
# This PREVENTS SQL injection attacks — a security best practice!
# NEVER use f-strings to build SQL queries with user input!
# ============================================================

if st.button("💾 Save to Database", use_container_width=True):

    # Validate that name is not empty before saving
    if not name:
        # st.error → shows a red error message box
        st.error("❌ Name is required! Please enter the student's full name.")
    else:
        try:
            # Step 1: Create connection to Azure SQL
            conn = get_connection()

            # Step 2: Create a cursor (used to execute SQL commands)
            cursor = conn.cursor()

            # Step 3: Execute INSERT query
            # %s are placeholders — pymssql replaces them safely
            # We don't insert CustomerID because it's IDENTITY (auto-increment)
            cursor.execute(
                "INSERT INTO [Students Information] ([Name], [Email], [PhoneNumber]) VALUES (?, ?, ?)",
                (name, email, phone)
            )

            # Step 4: Commit saves the changes permanently to the database
            # Without commit(), the data is lost when connection closes!
            conn.commit()

            # Step 5: Always close connection when done to free resources
            conn.close()

            # st.success → shows a green success message box
            st.success(f"✅ Student '{name}' has been added successfully!")

            # st.balloons → fun animation to celebrate! 🎈
            st.balloons()

        except Exception as e:
            # If anything goes wrong, show the error message
            # This catches: connection errors, SQL errors, etc.
            st.error(f"❌ Error while saving: {e}")


st.markdown("---")


# ============================================================
#  SECTION 2: VIEW ALL STUDENTS
# ============================================================
# This section loads ALL rows from the Students Information table
# and displays them as an interactive table using st.dataframe
#
# st.dataframe features:
#   - Sortable columns (click column header)
#   - Searchable
#   - Resizable columns
#   - use_container_width=True → stretches to full page width
# ============================================================

st.subheader("📋 View All Students")

if st.button("🔄 Load Students from Database", use_container_width=True):
    try:
        # Step 1: Connect to database
        conn = get_connection()
        cursor = conn.cursor()

        # Step 2: SELECT all rows from the table
        # * means "all columns"
        cursor.execute("SELECT * FROM [Students Information]")

        # Step 3: fetchall() returns all rows as a list of tuples
        rows = cursor.fetchall()

        # Step 4: Get column names from cursor description
        # cursor.description contains metadata about each column
        columns = [desc[0] for desc in cursor.description]

        # Step 5: Close connection
        conn.close()

        # Step 6: Check if there is any data
        if rows:
            # Convert list of tuples to a pandas DataFrame
            # DataFrame is like an Excel table in Python
            df = pd.DataFrame.from_records(rows, columns=columns)

            # Display the DataFrame as an interactive table
            st.dataframe(df, use_container_width=True)

            # st.info → shows a blue info message box
            st.info(f"📊 Total students in database: **{len(df)}**")
        else:
            # st.warning → shows a yellow warning message box
            st.warning("⚠️ No students found in the database yet. Add some students above!")

    except Exception as e:
        st.error(f"❌ Connection Error: {e}")


# ============================================================
#  FOOTER
# ============================================================

st.markdown("---")
st.markdown("Built with ❤️ using **Streamlit** + **Azure SQL Database**")