import psutil

CRITICAL_PROCESSES = [
    "System", "System Idle Process", "csrss.exe", "wininit.exe", 
    "services.exe", "winlogon.exe", "explorer.exe"
]

def get_heavy_processes(threshold=20):
    heavy = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            if proc.info['cpu_percent'] > threshold:
                heavy.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return heavy

def safe_kill_process(pid, name):
    if name in CRITICAL_PROCESSES:
        return False, "🛑 Proses sistem tidak boleh dihentikan."
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        return True, f"✅ Proses {name} dihentikan."
    except Exception as e:
        return False, f"❌ Gagal menghentikan {name}: {str(e)}"

def get_top_ram_processes(limit=5):
    ram_data = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            mem = proc.info['memory_info'].rss / (1024 * 1024)
            if mem > 50:
                ram_data.append({'name': proc.info['name'], 'pid': proc.info['pid'], 'memory_MB': round(mem, 2)})
        except:
            continue
    ram_data.sort(key=lambda x: x['memory_MB'], reverse=True)
    return ram_data[:limit]
