import streamlit as st

st.set_page_config(page_title="Spark — Creator Ignition", page_icon="🔥", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
html, body, [class*="css"] { font-family: 'Roboto', sans-serif; background-color: #FFFFFF; color: #0F0F0F; }.stApp { background-color: #FFFFFF; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem; max-width: 1400px; }
.stButton > button { background-color: #FF0000 !important; color: white !important; border: none !important; border-radius: 20px !important; font-weight: 500 !important; padding: 0.5rem 1.5rem !important; }
.stButton > button:hover { background-color: #CC0000 !important; }
.trend-card { background: #1A1A1A; border: 1px solid #2F2F2F; border-radius: 12px; overflow: hidden; margin-bottom: 12px; transition: border-color 0.2s; }
.trend-card:hover { border-color: #FF0000; }
.card-thumb { width: 100%; height: 90px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; }
.card-body { padding: 12px; }
.creator-card { background: #1A1A1A; border: 1px solid #2F2F2F; border-radius: 12px; padding: 14px; margin-bottom: 12px; }
.action-card { background: #1A1A1A; border: 1px solid #2F2F2F; border-radius: 12px; padding: 12px; margin-bottom: 12px; }
.nudge-box { font-size: 0.85rem; border-left: 3px solid #FF0000; border-radius: 0 6px 6px 0; padding: 8px 10px; background: rgba(255,0,0,0.06); line-height: 1.5; margin-bottom: 8px; color: #F1F1F1; }
.tool-chip { display: inline-block; font-size: 0.78rem; background: #272727; border: 1px solid #3F3F3F; border-radius: 20px; padding: 3px 10px; color: #AAAAAA; }
.badge { font-size: 0.7rem; font-weight: 600; text-transform: uppercase; background: rgba(255,255,255,0.1); padding: 2px 8px; border-radius: 20px; }
</style>
""", unsafe_allow_html=True)

# ── Static data ───────────────────────────────────────────────────────────────
DATA = {
    "Music artist / singer": {
        "trending": [
            {"type": "Challenge", "color": "#534AB7", "name": "#SlowedReverb wave", "why": "Slowed and reverb remixes are surging across R&B and bedroom pop. Creators who engage early ride the algorithmic lift before saturation.", "nudge": "Slow your most recent track to 0.8x speed, add light reverb, and post a 30-second Shorts reaction with the hashtag.", "tool": "YouTube Shorts"},
            {"type": "Rising Song", "color": "#0F6E56", "name": "Espresso — Sabrina Carpenter", "why": "Espresso has a viral cover and dance trend growing fast on YouTube. The cover window is still open for organic search ranking.", "nudge": "Record a genre-swap cover. Try 'If Espresso was an R&B ballad' — contrast in the title outperforms straight covers.", "tool": "AI-generated thumbnails"},
            {"type": "News", "color": "#854F0B", "name": "Kendrick Lamar Grammy sweep", "why": "The Kendrick Grammy moment is generating massive analysis content. Songwriter POV is underserved and high-performing right now.", "nudge": "Post a songwriter's lyric breakdown — your music background gives you credibility most creators don't have here.", "tool": "YouTube Create app"},
        ],
        "creators": [
            {"initials": "JC", "color": "#2A2A3E", "name": "Jacob Collier", "tag": "Music theory / harmony", "why": "Deep-dive theory content is growing fast. Creators who explain complex ideas simply build highly engaged niche audiences.", "nudge": "Post a 90-second Short explaining one concept from your own production process.", "tool": "YouTube Shorts"},
            {"initials": "SZ", "color": "#1A3A2E", "name": "SZA — audience signal", "tag": "R&B / Neo-soul", "why": "SZA's audience is actively discovering new R&B voices. Cover content in this space is pulling strong impressions.", "nudge": "Post a response or cover that places your voice in this conversation.", "tool": "Dream Track"},
        ]
    },
    "Streamer / gaming": {
        "trending": [
            {"type": "Live Stream", "color": "#A32D2D", "name": "iShowSpeed x MrBeast IRL collab", "why": "The IRL collab format is pulling record viewership. Reaction and commentary on viral streams performs strongly right now.", "nudge": "React to their most viral clip today and post as a Short with your own commentary. Timing is everything here.", "tool": "YouTube Shorts"},
            {"type": "Viral Clip", "color": "#0C447C", "name": "GTA VI gameplay discourse", "why": "GTA VI is dominating gaming YouTube. Opinion and hot-take content is outperforming standard gameplay coverage 3:1.", "nudge": "Post your honest GTA VI reaction today — strong opinion titles beat neutral coverage by a wide margin right now.", "tool": "AI-generated thumbnails"},
            {"type": "Drama", "color": "#791F1F", "name": "Streamer community drama", "why": "Community moments are historically the highest-click content for entertainment streamers. The commentary window is 48 hours.", "nudge": "Post a neutral breakdown clip — framing as analysis rather than taking sides appeals beyond each creator's fanbase.", "tool": "YouTube Create app"},
        ],
        "creators": [
            {"initials": "MO", "color": "#3A2A1A", "name": "Penguinz0", "tag": "Gaming commentary", "why": "Long-form gaming commentary with humor is making a comeback. His format is replicable in any gaming niche.", "nudge": "Try one 'commentary + gameplay' video where you talk over a session like a podcast.", "tool": "YouTube Studio analytics"},
            {"initials": "VK", "color": "#3A1A1A", "name": "Valkyrae", "tag": "Variety streaming", "why": "Variety streamers blending gaming with personality content are growing 2x faster than single-game channels.", "nudge": "Mirror her variety format for one stream, then compare retention against your standard content.", "tool": "YouTube Studio analytics"},
        ]
    }
}

# ── Session state ─────────────────────────────────────────────────────────────
if "onboarded" not in st.session_state:
    st.session_state.onboarded = False
if "niche" not in st.session_state:
    st.session_state.niche = ""

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("<h1 style='font-size:1.8rem;font-weight:700;margin-bottom:4px;'>🔥 Spark<span style='color:#FF0000'>.</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#AAAAAA;font-size:0.9rem;margin-bottom:2rem;'>Your daily creator ignition dashboard. Know what to create. Start today.</p>", unsafe_allow_html=True)

# ── Onboarding ────────────────────────────────────────────────────────────────
if not st.session_state.onboarded:
    with st.container():
        st.markdown("#### Set up your dashboard")
        st.markdown("<p style='color:#AAAAAA;font-size:0.9rem;'>Tell Spark about your niche so your dashboard is personalized to you.</p>", unsafe_allow_html=True)
        niche = st.radio("What best describes you?", list(DATA.keys()), horizontal=True)
        st.text_area("Drop 2–3 recent video titles (optional)", placeholder="e.g.\nMy Bedroom R&B Cover Session\nReacting to Grammy Nominees 2025", height=90)
        if st.button("Open my dashboard ⚡"):
            st.session_state.niche = niche
            st.session_state.onboarded = True
            st.rerun()

# ── Dashboard ─────────────────────────────────────────────────────────────────
else:
    niche = st.session_state.niche
    dash = DATA[niche]

    c1, c2, c3 = st.columns([5, 1, 1])
    with c1:
        st.markdown(f"<p style='font-size:0.85rem;color:#AAAAAA;background:#1A1A1A;border:1px solid #2F2F2F;border-radius:8px;padding:8px 14px;display:inline-block;'>🎯 Niche: <strong style='color:#F1F1F1;'>{niche}</strong></p>", unsafe_allow_html=True)
    with c2:
        if st.button("↻ Refresh"):
            st.rerun()
    with c3:
        if st.button("⟵ Edit"):
            st.session_state.onboarded = False
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("**🔥 Trending now**")
        for item in dash["trending"]:
            st.markdown(f"""
            <div class="trend-card">
                <div class="card-thumb" style="background:{item['color']};">▶</div>
                <div class="card-body">
                    <span class="badge">{item['type']}</span>
                    <p style="font-size:0.9rem;font-weight:500;margin:6px 0 4px;color:#F1F1F1;">{item['name']}</p>
                    <p style="font-size:0.82rem;color:#AAAAAA;margin:0;line-height:1.5;">{item['why']}</p>
                </div>
            </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("**👀 Creators to watch**")
        for item in dash["creators"]:
            st.markdown(f"""
            <div class="creator-card">
                <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
                    <div style="width:38px;height:38px;border-radius:50%;background:{item['color']};display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:500;flex-shrink:0;color:#F1F1F1;">{item['initials']}</div>
                    <div>
                        <p style="font-size:0.88rem;font-weight:500;margin:0;color:#F1F1F1;">{item['name']}</p>
                        <p style="font-size:0.75rem;color:#AAAAAA;margin:0;">{item['tag']}</p>
                    </div>
                </div>
                <p style="font-size:0.82rem;color:#AAAAAA;margin:0;line-height:1.5;">{item['why']}</p>
            </div>""", unsafe_allow_html=True)

    with col3:
        st.markdown("**⚡ Take action**")
        for item in dash["trending"] + dash["creators"]:
            st.markdown(f"""
            <div class="action-card">
                <p style="font-size:0.75rem;color:#717171;margin:0 0 5px;">{item['name']}</p>
                <div class="nudge-box">{item['nudge']}</div>
                <span class="tool-chip">▶ {item['tool']}</span>
            </div>""", unsafe_allow_html=True)

    st.markdown("<p style='font-size:0.75rem;color:#717171;text-align:center;margin-top:2rem;border-top:1px solid #2F2F2F;padding-top:1rem;'>Spark prototype · PC layout · Mobile stacked in next iteration · Built by Fate Yarahmady</p>", unsafe_allow_html=True)
