# id no servidor da netware 39487
# Coxim TJNET 11038
# ideal gigarede anastácio 37365
import speedtest

servidores = [37365]

threads = 32

speed = speedtest.Speedtest()

down = speed.download(threads=threads) 
upld = speed.upload(threads=threads) 

print(f'Download - {down}')
print((f'Upload - {upld}'))

