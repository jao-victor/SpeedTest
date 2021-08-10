# id no servidor da netware 39487
# Coxim TJNET 11038
# ideal gigarede anastácio 37365
import speedtest

servidores = [37365]
speed = speedtest.Speedtest()


try:
    speed.get_servers(servidores)
except Exception:
    speed.get_closest_servers()
    speed.get_best_server()


threads = 32

down = speed.download(threads=threads) 
upld = speed.upload(threads=threads) 


print(f'Download - {down} Mbps')
print(f'Upload - {upld} Mbps')
#print(f'Ping {ping}')
print('...')

results_dict = s.results.dict()
print(results_dict)
