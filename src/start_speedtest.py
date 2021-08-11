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
    name_server = results_dict ['client'] ['isp']
    latencia = results_dict['server'] ['lat']


    # FORMATANDO DADOS
    down = int(down) / 1000 / 1000
    down = round(down, 2)

  
    upld = int(upld) / 1000 / 1000
    upld = round(upld, 2)

    latencia = float(latencia)
    latencia = round(latencia, 2)

    return [down, upld, latencia, name_server]

