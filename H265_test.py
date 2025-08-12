import time
from picamera2 import Picamera2
from picamera2.encoders import H265Encoder

# --- 設定項目 ---
RECORD_SECONDS = 10  # 録画する秒数
OUTPUT_FILENAME = "mission_log_01.h265"  # 保存するファイル名
# ビットレート (bps)。数値を下げるとファイルサイズは軽くなるが画質も落ちる。
# 1080pの目安: 高画質 5Mbps=5000000, 中画質 2Mbps=2000000
BITRATE = 2000000

# 1. Picamera2のインスタンスを初期化
picam2 = Picamera2()

# 2. 動画撮影用の設定を作成
# main={"size": (横, 縦)} で解像度を指定できます。例: (1920, 1080)
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

# 3. H.265エンコーダーを作成し、ビットレートを設定
encoder = H265Encoder(bitrate=BITRATE)

print(f"カメラ準備完了。")
print(f"これから {OUTPUT_FILENAME} に {RECORD_SECONDS}秒間録画します...")

# 4. 録画を開始
# エンコーダーと出力ファイル名を指定
picam2.start_recording(encoder, OUTPUT_FILENAME)

# 5. 指定した秒数だけ待機
time.sleep(RECORD_SECONDS)

# 6. 録画を停止
picam2.stop_recording()

print(f"録画完了！ファイルサイズと画質を確認してください。")