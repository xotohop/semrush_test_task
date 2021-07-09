# -*- coding: utf-8 -*-
# pip install pycryptodomex
from Cryptodome.Cipher import AES

# сообщение, отправленное в 99 строке
b64_message = "bVRHZWxqaERSS0FTS0toUSxGTHJzU0V2ZVFRaWxvUFJuLFhlZFhIWUJVSHBJWERCSlAsSU9HUEVyam9zeE5pUXJOTSxSenZwYkVVUkxkRmZhR0ZNLHZkQlZEQ3ZpeGpTaENRdnksRVFsY3NuVXR6Q0h5RlBITSxKa0RpamdBRmlWQldKYUx6LGdoY1BJT1NxQ2RDVHFPcEQsRG5lQ3dia0RIa29qcHBIbSxsVlJaUmVBbGFJekhnaXNjLE5kamNnVlZqaWlueGZ0Q0MsUmtnTHBSQ3FybmlicnFzTixremV3dGVBZ1BFWmRrelFKLEhucEdvVWVxY2tFcXhwUW0sTFNOV1JhclRoUmRpUExwTQ=="

# судя по строкам 89-91 и 101, используется последний ключ
keys = [b'mTGeljhDRKASKKhQ',
        b'FLrsSEveQQiloPRn',
        b'XedXHYBUHpIXDBJP',
        b'IOGPErjosxNiQrNM',
        b'RzvpbEURLdFfaGFM',
        b'vdBVDCvixjShCQvy',
        b'EQlcsnUtzCHyFPHM',
        b'JkDijgAFiVBWJaLz',
        b'ghcPIOSqCdCTqOpD',
        b'DneCwbkDHkojppHm',
        b'lVRZReAlaIzHgisc',
        b'NdjcgVVjiinxftCC',
        b'RkgLpRCqrnibrqsN',
        b'kzewteAgPEZdkzQJ',
        b'HnpGoUeqckEqxpQm',
        b'LSNWRarThRdiPLpM']

key = b'LSNWRarThRdiPLpM'
cipher = AES.new(key, AES.MODE_ECB)
with open("secrets.txt.enc", "rb") as file:
    encrypted = file.read()
decrypted = cipher.decrypt(encrypted[AES.block_size:]).decode('utf-8')
with open("secrets.txt", "w") as file:
    file.write(decrypted)
