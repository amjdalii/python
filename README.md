import requests
from time import sleep
from webbrowser import open_new_tab
print("""

⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩⬜⬜🟩🟩⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟩🟩🟩⬜⬜⬜⬜🟩⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟩🟩⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜🟩⬜🏽⬜⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜⬜🏽⬜⬜⬛⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬜🏽⬜⬜⬛⬛⬜⬛⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛
⬜⬜⬜⬜⬜⬛⬛⬜⬜🟥⬜⬜⬜⬜⬜⬜⬛⬜⬛🏽🏽🏽🏽🏽🏽🏽⬛
⬜⬜⬜⬛⬛🟪🟪⬛⬜⬜🟥🟥🟥🟥⬜⬛⬛⬛⬛🏽🏽🏽🏽🏽🏽⬛⬛
⬜⬜⬛🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬛🟪🟪🟪⬛🌫️🌫️🏽🌫️🏽⬛⬜⬜
⬜⬜⬛🟪🟪⬛⬛🟪⬜⬛⬛⬛⬛⬛🟪🟪🟪🟪⬛🌫️🏽🌫️⬛⬛⬜⬜⬜
⬜⬛⬛⬛🟪⬛⬛⬜🟥⬜🟩⬛🟩🟪🟪🟪🟪🟪⬛🌫️🏽🌫️⬛⬜⬜⬜⬜
⬜⬛⬜⬜⬛⬛⬛🟪⬜🟪🟧🟧🟧🟪⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬛⬜⬜⬜⬛⬛🟪🟪🟪🟧⬛🟧🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬜⬜⬜⬛⬛🟪🟪🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬛⬛⬜⬛🟧🟧🟧🟧⬛🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟪🟪🟪🟪⬛⬛⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟪🟪🟪🟪⬛⬛🟪⬛⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪🟪🟪🟪⬛🟪🟪🟪⬛🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬛🟪⬜🟪⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜""")
print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
print('\x1b[31;40mLOODING');sleep(2)
print('المطور ســـكـــار @S_C_A_R1');sleep(2)
open_new_tab('n')
print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
visa = str(input('\x1b[32;23m ادخل الفيزا : '))
print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
url = 'https://checker.visatk.com/ccn1/alien07.php'
cookies = {
    '__gads': 'ID=cfac8362929ba58b:T=1708544364:RT=1708544364:S=ALNI_Mb5mRcS4hY0XtxqQcNhRfjmjHoKJw',
    '__gpi': 'UID=00000d5eeac1f2de:T=1708544364:RT=1708544364:S=ALNI_MbyR8pzSZnS3X3mGtezsqfpBVHAOw',
    '__eoi': 'ID=fdb0f66bcdd2b012:T=1708544364:RT=1708544364:S=AA-Afjby0bwDTSUdTxiCdAv2fNt0',
    'FCNEC': '%5B%5B%22AKsRol91zT-yKMi3C8MaP6Kn0c9nISBY26G0oDe1rVh5y2Xk_VSrIFgPmDdSwRoz9eUwNYCc7lmCQJN6Z-cI4yPBrGAb7wmbNnwoHJvYJkx5QsbAympL6b81YA96zKMMCd2si42vVqptPxXo-MAr_bwCqPMwOa--VQ%3D%3D%22%5D%5D',
}

headers = {
    'authority': 'checker2.visatk.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__gads=ID=cfac8362929ba58b:T=1708544364:RT=1708544364:S=ALNI_Mb5mRcS4hY0XtxqQcNhRfjmjHoKJw; __gpi=UID=00000d5eeac1f2de:T=1708544364:RT=1708544364:S=ALNI_MbyR8pzSZnS3X3mGtezsqfpBVHAOw; __eoi=ID=fdb0f66bcdd2b012:T=1708544364:RT=1708544364:S=AA-Afjby0bwDTSUdTxiCdAv2fNt0; FCNEC=%5B%5B%22AKsRol91zT-yKMi3C8MaP6Kn0c9nISBY26G0oDe1rVh5y2Xk_VSrIFgPmDdSwRoz9eUwNYCc7lmCQJN6Z-cI4yPBrGAb7wmbNnwoHJvYJkx5QsbAympL6b81YA96zKMMCd2si42vVqptPxXo-MAr_bwCqPMwOa--VQ%3D%3D%22%5D%5D',@S_C_A_R1
    'origin': 'https://checker2.visatk.com',
    'referer': 'https://checker2.visatk.com/card/ccn1/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'ajax': '1',
    'do': 'check',
    'cclist': visa,
}


req = requests.post(url, headers=headers, data=data).text
print('\x1b[35;23m تطوير سكــأر')
if 'Live' in req:
	many = req.split("[Charge :<font color=green>")[1].split("</font>] [BIN:")[0]
	print('\x1b[32;23m✅✅✅✅✅✅✅ ',visa);print('الفيزا مشحونة : ',many+' دولار')
if 'Die' or 'Unknow' in req:
	print('فيزه خربانه❌ متشتغل جرب غيرها ',visa)
