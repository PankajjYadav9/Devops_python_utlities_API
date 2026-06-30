import psutil

def get_system_metrics():
    """
    This API gets the SYStem matrics (CPU memory  disk system health)
    based on a CPU threshold  i.e 10 percentage
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    cpu_threshold = 10
    status = "High CPU" if cpu_percent > cpu_threshold else "Healthy"

    return{
        "cpu_percentage": cpu_percent,
        "memory_percentage":memory_percent,
        "disk_percentage": disk_percent,
        "cpu_threshold":cpu_threshold,
        "systemstatus":status
    }