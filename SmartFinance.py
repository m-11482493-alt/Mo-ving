import streamlit as st

st.title("💰 SaveSmart Lite (Web Version)")

# --- Input Data ---
income = st.number_input("Pendapatan (RM):", min_value=0.0, step=100.0)
challenge_goal = st.number_input("Cabaran Menabung (Sasaran RM):", min_value=0.0, step=10.0)
goal_name = st.text_input("Tabung Matlamat (Nama):")
goal_target = st.number_input("Tabung Matlamat (Sasaran RM):", min_value=0.0, step=50.0)

# --- Default values in session_state ---
if "challenge_saved" not in st.session_state:
    st.session_state.challenge_saved = 0
if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 0

# --- Set Data ---
if st.button("Set Data"):
    needs = income * 0.5
    wants = income * 0.3
    savings = income * 0.2

    st.session_state.challenge_saved = 0
    st.session_state.goal_saved = 0

    st.subheader("📊 Automasi Bajet Pintar")
    st.write(f"Pendapatan: RM{income}")
    st.write(f"Keperluan: RM{needs}")
    st.write(f"Kehendak: RM{wants}")
    st.write(f"Simpanan: RM{savings}")

# --- Cabaran Menabung ---
st.subheader("🏆 Cabaran Menabung")
st.write(f"Sasaran: RM{challenge_goal}, Terkumpul: RM{st.session_state.challenge_saved}")

col1, col2 = st.columns(2)
with col1:
    if st.button("Tambah Simpanan +RM10", disabled=(challenge_goal == 0)):
        if st.session_state.challenge_saved < challenge_goal:
            st.session_state.challenge_saved = min(
                st.session_state.challenge_saved + 10, challenge_goal
            )
        else:
            st.info("🎉 Tahniah! Cabaran menabung sudah capai sasaran.")
        st.rerun()

with col2:
    if st.button("Reset Cabaran", disabled=(challenge_goal == 0)):
        st.session_state.challenge_saved = 0
        st.rerun()

# --- Tabung Matlamat ---
st.subheader("🎯 Tabung Matlamat")
st.write(f"{goal_name}: RM{st.session_state.goal_saved}/{goal_target}")

col3, col4 = st.columns(2)
with col3:
    if st.button("Tambah ke Tabung +RM50", disabled=(goal_target == 0)):
        if st.session_state.goal_saved < goal_target:
            st.session_state.goal_saved = min(
                st.session_state.goal_saved + 50, goal_target
            )
        else:
            st.info(f"🎉 Tahniah! Tabung {goal_name} sudah penuh.")
        st.rerun()

with col4:
    if st.button("Reset Tabung", disabled=(goal_target == 0)):
        st.session_state.goal_saved = 0
        st.rerun()
