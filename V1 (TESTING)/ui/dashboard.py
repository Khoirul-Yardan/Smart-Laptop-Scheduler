import streamlit as st
from utils.system_monitor import get_system_usage
from utils.process_manager import get_heavy_processes
import pandas as pd

def run_dashboard():
    st.set_page_config(page_title="Smart Laptop Scheduler", layout="wide")
    st.title("💻 Smart Laptop Scheduler")

    usage = get_system_usage()
    st.metric("CPU Usage", f"{usage['cpu']}%")
    st.metric("RAM Usage", f"{usage['ram']}%")

    st.subheader("🔍 Heavy Processes")
    processes = get_heavy_processes()
    if processes:
        df = pd.DataFrame(processes)
        st.dataframe(df)
    else:
        st.success("Tidak ada proses berat saat ini.")
