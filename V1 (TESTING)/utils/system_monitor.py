import psutil

def get_system_usage():
    """Return CPU and RAM usage in percentage"""
    return {
        'cpu': psutil.cpu_percent(interval=1),
        'ram': psutil.virtual_memory().percent
    }
