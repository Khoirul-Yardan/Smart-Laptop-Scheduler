import streamlit as st
from utils.system_monitor import get_system_usage
from utils.process_manager import get_heavy_processes, safe_kill_process, get_top_ram_processes
from streamlit_autorefresh import st_autorefresh

import pandas as pd

def get_recommendation(cpu, ram):
    if ram > 85:
        return "⚠️ RAM tinggi. Tutup aplikasi berat atau upgrade RAM jika memungkinkan."
    elif cpu > 80:
        return "⚠️ CPU sedang penuh. Hindari multitasking berat sekarang."
    else:
        return "✅ Sistem dalam kondisi baik."



def run_dashboard():
    st.set_page_config(page_title="Smart Laptop Scheduler", layout="wide")
    st_autorefresh(interval=5000, key="auto_refresh")  # Auto-refresh 5 detik

    st.title("💻 Smart Laptop Scheduler")

    usage = get_system_usage()
    st.metric("CPU Usage", f"{usage['cpu']}%")
    st.metric("RAM Usage", f"{usage['ram']}%")

    st.warning(get_recommendation(usage['cpu'], usage['ram']))

    st.subheader("🔍 Heavy Processes")
    processes = get_heavy_processes()
    if processes:
        df = pd.DataFrame(processes)
        st.dataframe(df)
        for proc in processes:
            name = proc['name']
            pid = proc['pid']
            if st.button(f"Kill {name} ({pid})", key=f"kill_{pid}"):
                status, msg = safe_kill_process(pid, name)
                st.info(msg)
    else:
        st.success("Tidak ada proses berat saat ini.")

    st.subheader("📈 Top RAM Consumers")
    ram_proc = get_top_ram_processes()
    if ram_proc:
        st.dataframe(pd.DataFrame(ram_proc))
    else:
        st.info("Tidak ada proses RAM tinggi.")
