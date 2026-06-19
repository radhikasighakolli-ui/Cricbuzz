<<<<<<< HEAD
import streamlit as st
import pandas as pd
from utils.cricbuzz_api import get_live_matches
from utils.db_connection import get_engine

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page", [
    "Home", "Live Matches", "Top Player Stats", "SQL Analytics", "CRUD Operations"
])

if page == "Home":
    st.title("🏏 Cricbuzz LiveStats")
    st.write("Welcome! Use the sidebar to explore live matches, player stats, SQL queries, and admin panel.")

elif page == "Live Matches":
    st.header("Live Matches")
    if st.button("Show Live Matches"):
        try:
            data = get_live_matches()
            matches = data.get("typeMatches", [])
            for match_type in matches:
                for series in match_type.get("seriesMatches", []):
                    st.subheader(series.get("seriesAdWrapper", {}).get("seriesName"))
                    for match in series.get("seriesAdWrapper", {}).get("matches", []):
                        info = match.get("matchInfo", {})
                        desc = info.get("matchDesc")
                        team1 = info.get("team1", {}).get("teamName")
                        team2 = info.get("team2", {}).get("teamName")
                        venue = info.get("venueInfo", {}).get("ground")
                        st.write(f"{desc}: {team1} vs {team2} at {venue}")
        except Exception as e:
            st.error(f"Failed fetching live matches: {e}")

elif page == "Top Player Stats":
    st.header("Top Run Scorers")
    engine = get_engine()
    try:
        df = pd.read_sql("""
            SELECT players.full_name, SUM(performances.runs) as total_runs
            FROM players
            JOIN performances ON players.player_id = performances.player_id
            GROUP BY players.full_name
            ORDER BY total_runs DESC
            LIMIT 10;
        """, engine)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error loading player stats: {e}")

elif page == "SQL Analytics":
    st.header("Run SQL Query")
    query = st.text_area("Enter your SQL query here:")
    if st.button("Run Query") and query.strip():
        try:
            engine = get_engine()
            df = pd.read_sql(query, engine)
            st.dataframe(df)
        except Exception as e:
            st.error(f"Query error: {e}")

elif page == "CRUD Operations":
    st.header("Add New Player")
    with st.form("add_player"):
        name = st.text_input("Full Name")
        country = st.text_input("Country")
        role = st.text_input("Role")
        batting = st.text_input("Batting Style")
        bowling = st.text_input("Bowling Style")
        submitted = st.form_submit_button("Add Player")
        if submitted:
            try:
                engine = get_engine()
                with engine.connect() as conn:
                    conn.execute(
                        "INSERT INTO players (full_name, country, role, batting_style, bowling_style) VALUES (%s, %s, %s, %s, %s)",
                        (name, country, role, batting, bowling)
                    )
                st.success("Player added successfully!")
            except Exception as e:
                st.error(f"Failed to add player: {e}")
=======
import streamlit as st
import pandas as pd
from utils.cricbuzz_api import get_live_matches
from utils.db_connection import get_engine

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page", [
    "Home", "Live Matches", "Top Player Stats", "SQL Analytics", "CRUD Operations"
])

if page == "Home":
    st.title("🏏 Cricbuzz LiveStats")
    st.write("Welcome! Use the sidebar to explore live matches, player stats, SQL queries, and admin panel.")

elif page == "Live Matches":
    st.header("Live Matches")
    if st.button("Show Live Matches"):
        try:
            data = get_live_matches()
            matches = data.get("typeMatches", [])
            for match_type in matches:
                for series in match_type.get("seriesMatches", []):
                    st.subheader(series.get("seriesAdWrapper", {}).get("seriesName"))
                    for match in series.get("seriesAdWrapper", {}).get("matches", []):
                        info = match.get("matchInfo", {})
                        desc = info.get("matchDesc")
                        team1 = info.get("team1", {}).get("teamName")
                        team2 = info.get("team2", {}).get("teamName")
                        venue = info.get("venueInfo", {}).get("ground")
                        st.write(f"{desc}: {team1} vs {team2} at {venue}")
        except Exception as e:
            st.error(f"Failed fetching live matches: {e}")

elif page == "Top Player Stats":
    st.header("Top Run Scorers")
    engine = get_engine()
    try:
        df = pd.read_sql("""
            SELECT players.full_name, SUM(performances.runs) as total_runs
            FROM players
            JOIN performances ON players.player_id = performances.player_id
            GROUP BY players.full_name
            ORDER BY total_runs DESC
            LIMIT 10;
        """, engine)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error loading player stats: {e}")

elif page == "SQL Analytics":
    st.header("Run SQL Query")
    query = st.text_area("Enter your SQL query here:")
    if st.button("Run Query") and query.strip():
        try:
            engine = get_engine()
            df = pd.read_sql(query, engine)
            st.dataframe(df)
        except Exception as e:
            st.error(f"Query error: {e}")

elif page == "CRUD Operations":
    st.header("Add New Player")
    with st.form("add_player"):
        name = st.text_input("Full Name")
        country = st.text_input("Country")
        role = st.text_input("Role")
        batting = st.text_input("Batting Style")
        bowling = st.text_input("Bowling Style")
        submitted = st.form_submit_button("Add Player")
        if submitted:
            try:
                engine = get_engine()
                with engine.connect() as conn:
                    conn.execute(
                        "INSERT INTO players (full_name, country, role, batting_style, bowling_style) VALUES (%s, %s, %s, %s, %s)",
                        (name, country, role, batting, bowling)
                    )
                st.success("Player added successfully!")
            except Exception as e:
                st.error(f"Failed to add player: {e}")
>>>>>>> e001a984a07ce756997db40c52bcf4d921037760
