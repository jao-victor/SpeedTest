import speedtest


def start():

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

    '''print(f'Download - {down} Mbps')
    print(f'Upload - {upld} Mbps')
    print(f'Servidor: {name_server}')
    print(f'Latência: {latencia} ms')'''

    # FORMATANDO DADOS
    down = str(down)
    print(type(down))
    down = down.split('.')
    down = int(down[0]) / 1000 / 1000
    print(down)


    upld = str(upld)
    print(type(upld))
    upld = upld.split('.')
    upld = int(upld[0]) / 1000 / 1000
    print(upld)

    return [down, upld]

