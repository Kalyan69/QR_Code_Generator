# darkblue_qrcode.py

import segno

qrcode = segno.make_qr("Lija gate, pati mankara")
qrcode.save(
    "darkblue_qrcode.png",
    scale=5,
    dark="darkblue",
)