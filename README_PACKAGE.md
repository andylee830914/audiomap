# PyAudio Detector

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/pyaudio-detector)

跨平台音頻設備檢測庫，支援 macOS、Windows 和 Linux 平台的音頻輸入和輸出設備檢測。

## 功能特點

- 🔍 **跨平台支援**: 支援 macOS、Windows 和 Linux
- 🎤 **輸入設備檢測**: 檢測麥克風、線路輸入等音頻輸入設備
- 🔊 **輸出設備檢測**: 檢測揚聲器、耳機等音頻輸出設備
- 📝 **統一 API**: 所有平台使用相同的 API 介面
- 🛠️ **原生實作**: 
  - macOS: 使用 CoreAudio API
  - Windows: 使用 pycaw + comtypes
  - Linux: 使用 ALSA 工具
- 🎯 **輕量級**: 最小依賴，高效能
- 📱 **命令行工具**: 內建命令行介面

## 安裝

### 基本安裝

```bash
pip install pyaudio-detector
```

### 平台特定依賴

**Windows 用戶需要額外安裝：**
```bash
pip install pyaudio-detector[windows]
```

**開發者安裝：**
```bash
pip install pyaudio-detector[dev]
```

## 快速開始

### 基本使用

```python
from pyaudio_detector import list_audio_input_devices, list_audio_output_devices

# 列出所有輸入設備
input_devices = list_audio_input_devices()
for device in input_devices:
    print(f"輸入設備: {device['name']} (UID: {device['id']})")

# 列出所有輸出設備
output_devices = list_audio_output_devices()
for device in output_devices:
    print(f"輸出設備: {device['name']} (UID: {device['id']})")
```

### 使用類別介面

```python
from pyaudio_detector import AudioDeviceDetector

detector = AudioDeviceDetector()

# 獲取所有設備
all_devices = detector.list_all_devices()
print(f"輸入設備: {len(all_devices['input'])} 個")
print(f"輸出設備: {len(all_devices['output'])} 個")

# 查找特定設備
macbook_devices = detector.find_device_by_name("MacBook")
for device in macbook_devices:
    print(f"找到設備: {device['name']}")

# 獲取設備統計
stats = detector.get_device_count()
print(f"總計: {stats['total']} 個音頻設備")
```

### 命令行使用

```bash
# 列出所有設備
pyaudio-detector

# 只列出輸入設備
pyaudio-detector --input-only

# 只列出輸出設備
pyaudio-detector --output-only

# JSON 格式輸出
pyaudio-detector --json

# 查找特定設備
pyaudio-detector --find "MacBook"

# 只顯示統計
pyaudio-detector --count-only
```

## API 文檔

### 便利函數

#### `list_audio_input_devices()`
返回所有音頻輸入設備列表。

**返回值:**
- `List[Dict[str, str]]`: 設備列表，每個設備包含：
  - `id`: 設備唯一識別碼
  - `name`: 設備名稱
  - `platform`: 平台名稱 ("Windows", "Darwin", "Linux")

#### `list_audio_output_devices()`
返回所有音頻輸出設備列表。

**返回值:**
- `List[Dict[str, str]]`: 設備列表（格式同上）

### AudioDeviceDetector 類別

#### `list_input_devices()`
列出所有音頻輸入設備。

#### `list_output_devices()`
列出所有音頻輸出設備。

#### `list_all_devices()`
列出所有音頻設備。

**返回值:**
```python
{
    "input": List[Dict[str, str]],
    "output": List[Dict[str, str]]
}
```

#### `get_device_count()`
獲取設備數量統計。

**返回值:**
```python
{
    "input": int,    # 輸入設備數量
    "output": int,   # 輸出設備數量  
    "total": int     # 總設備數量
}
```

#### `find_device_by_name(name, device_type="both")`
根據名稱查找設備。

**參數:**
- `name (str)`: 設備名稱（支援部分匹配）
- `device_type (str)`: 設備類型，可選 "input", "output", "both"

## 平台需求

### macOS
- 無額外依賴（使用系統內建的 CoreAudio）
- 支援所有音頻設備類型

### Windows
- 需要安裝: `pip install pycaw comtypes`
- 支援 WASAPI 設備

### Linux
- 需要安裝 ALSA 工具: `sudo apt-get install alsa-utils`
- 支援 ALSA 和 PulseAudio/PipeWire 設備

## 錯誤處理

```python
from pyaudio_detector import AudioDeviceDetector
from pyaudio_detector.exceptions import AudioDetectionError, DependencyMissingError

try:
    detector = AudioDeviceDetector()
    devices = detector.list_input_devices()
except DependencyMissingError as e:
    print(f"缺少依賴: {e}")
except AudioDetectionError as e:
    print(f"檢測錯誤: {e}")
```

## 輸出範例

### macOS 輸出範例
```
=== 音頻輸入設備 ===
找到 3 個輸入設備:
  1. MacBook Pro的麥克風 (UID: BuiltInMicrophoneDevice)
  2. WH-1000XM6 (UID: 58-18-62-13-51-61:input)
  3. BlackHole 2ch (UID: BlackHole2ch_UID)

=== 音頻輸出設備 ===
找到 4 個輸出設備:
  1. MacBook Pro的揚聲器 (UID: BuiltInSpeakerDevice)
  2. WH-1000XM6 (UID: 58-18-62-13-51-61:output)
  3. BlackHole 2ch (UID: BlackHole2ch_UID)
  4. 多重輸出裝置 (UID: ~:AMS2_StackedOutput:0)
```

## 開發

### 設置開發環境

```bash
git clone https://github.com/yourusername/pyaudio-detector.git
cd pyaudio-detector
pip install -e .[dev]
```

### 執行測試

```bash
pytest tests/
```

### 建構套件

```bash
python -m build
```

## 授權

MIT License - 詳見 [LICENSE](LICENSE) 檔案。

## 貢獻

歡迎提交 Issue 和 Pull Request！

## 更新日誌

### v1.0.0
- 初始版本
- 支援 macOS、Windows、Linux 三大平台
- 提供命令行工具
- 完整的錯誤處理
