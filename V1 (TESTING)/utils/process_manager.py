import psutil

def get_heavy_processes(threshold=20):
    """Return list of processes using more than threshold % of CPU"""
    heavy = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            if proc.info['cpu_percent'] > threshold:
                heavy.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return heavy
