import platform
import os
import psutil
import subprocess

# CPU信息
def get_cpu_info():
    try:
        import cpuinfo
        info = cpuinfo.get_cpu_info()
        return {
            'brand': info.get('brand_raw'),
            'arch': info.get('arch'),
            'cores': psutil.cpu_count(logical=False),
            'threads': psutil.cpu_count(logical=True),
            'freq': psutil.cpu_freq().current if psutil.cpu_freq() else None
        }
    except ImportError:
        return {
            'brand': platform.processor(),
            'cores': psutil.cpu_count(logical=False),
            'threads': psutil.cpu_count(logical=True),
            'freq': psutil.cpu_freq().current if psutil.cpu_freq() else None
        }

# 内存信息
def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        'total': mem.total,
        'available': mem.available,
        'used': mem.used,
        'percent': mem.percent
    }

# 硬盘信息
def get_disk_info():
    partitions = psutil.disk_partitions()
    disks = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disks.append({
            'device': partition.device,
            'mountpoint': partition.mountpoint,
            'fstype': partition.fstype,
            'total': usage.total,
            'used': usage.used,
            'free': usage.free,
            'percent': usage.percent
        })
    return disks

# 主板信息（Linux，需root权限）
def get_mainboard_info():
    if os.name == "posix":
        try:
            output = subprocess.check_output("sudo dmidecode -t baseboard", shell=True, text=True)
            return output
        except Exception as e:
            return str(e)
    elif os.name == "nt":
        try:
            import wmi
            c = wmi.WMI()
            for board in c.Win32_BaseBoard():
                return {
                    "Manufacturer": board.Manufacturer,
                    "Product": board.Product,
                    "SerialNumber": board.SerialNumber
                }
        except ImportError:
            return "请安装wmi库: pip install wmi"
    else:
        return "未知操作系统"

# GPU信息（NVIDIA显卡，需安装nvidia-smi）
def get_gpu_info():
    try:
        output = subprocess.check_output("nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader", shell=True, text=True)
        return output.strip()
    except Exception:
        return "未检测到NVIDIA GPU或nvidia-smi未安装"

if __name__ == "__main__":
    print("CPU信息：", get_cpu_info())
    print("内存信息：", get_memory_info())
    print("硬盘信息：", get_disk_info())
    print("主板信息：", get_mainboard_info())
    print("GPU信息：", get_gpu_info())