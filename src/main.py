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
results_dict = speed.results.dict()
name_server = results_dict.get('client', 'erro').get('isp', 'erro')
latencia = results_dict.get('server').get('lat')

print(f'Download - {down} Mbps')
print(f'Upload - {upld} Mbps')
print(f'Servidor: {name_server}')
print(f'Latência: {latencia} ms')

