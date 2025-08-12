import RPi.GPIO as GPIO
import sys

# --- 設定 ---
LED_PIN = 18      # BCMピン番号 (物理ピン12)
PWM_FREQ = 100    # PWM周波数 (Hz)

# --- GPIOのセットアップ ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# --- PWMの初期化 ---
pwm = GPIO.PWM(LED_PIN, PWM_FREQ)
pwm.start(0) # デューティーサイクル0%で開始

# デューティーサイクルの現在値を保持する変数
duty_cycle = 0

print(f"GPIO {LED_PIN}番ピンのPWM増減テストを開始します。")
print("--------------------------------------------------")
print("操作方法:")
print("  ・エンターキー   : 明るさを1%上げます。")
print("  ・'z' + エンター : 明るさを1%下げます。")
print("  ・'r' + エンター : プログラムを終了します。")
print("--------------------------------------------------")

try:
    # 無限ループでユーザーの入力を待ち続ける
    while True:
        # ユーザーからの入力を待つ
        prompt = f"現在の明るさ: {duty_cycle}% -> "
        key_input = input(prompt)

        # 'r'が入力されたらループを抜けて終了
        if key_input.lower() == 'r':
            print("終了コマンドを受け付けました。")
            break
        # 'z'が入力されたら明るさを下げる
        elif key_input.lower() == 'z':
            duty_cycle -= 1
        # それ以外（エンターキーのみを含む）の場合は明るさを上げる
        else:
            duty_cycle += 1
        
        # デューティーサイクルが0-100の範囲に収まるように調整
        if duty_cycle > 100:
            duty_cycle = 100
        if duty_cycle < 0:
            duty_cycle = 0
            
        # PWMのデューティーサイクルを更新して明るさを変更
        pwm.ChangeDutyCycle(duty_cycle)

except KeyboardInterrupt:
    # Ctrl+Cが押された場合の処理
    print("\nプログラムが中断されました。")

finally:
    # --- クリーンアップ処理 ---
    # プログラム終了時には必ずここが実行される
    print("GPIOをクリーンアップします...")
    pwm.stop()      # PWMを停止
    GPIO.cleanup()  # GPIOの設定をリセット
    print("完了しました。")