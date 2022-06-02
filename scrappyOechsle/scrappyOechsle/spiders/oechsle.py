import scrapy
import pandas as pd
from scrapy.spiders import CrawlSpider, Rule #librería para extarcción de datos
from scrapy.linkextractors import LinkExtractor
from numpy import nan #librería para datos
#from bs4 import BeautifulSoup
from lxml import etree
import requests


#busqueda = input("¿que artículo deseas buscar en Mercado Libre?: ")

class OechsleSpider(scrapy.Spider):
    name = 'oechsle' # Nombre de la web a escanear
    

    def start_requests(self):
        file = pd.read_csv("links_totales.csv")
        #next_links = list(file['links'])
        next_links = file['list_link']
        for url in next_links:
            yield scrapy.Request(url=url, callback=self.parse_filter)
        
    

    def parse_filter(self, response):

        # Titulo
        titulo = response.xpath("//div[@class='mt-20 d-none d-lg-block']/h2/div/text()").get()

        # Link
        link = response.xpath("//meta[@property='og:url']/@content").get()
        
        # link imagen
        link_imagen = response.xpath("//*[@id='image']/a/div/div[2]/div/div[2]/img/@src").get()

        # Precio normal
        precio_normal = response.xpath("//strong[@class='skuListPrice']/text()").get()
        
        # descripcion nombres
        try:
            # Precio Online
            precio_online = response.xpath("//strong[@class='skuBestPrice']/text()").get()
            # Precio Online oh
            precio_tarjeta_oh = response.xpath("//*[@id='precios']/div[2]/div[3]/div[2]/span[1]/text()").get()
            # lector de trajetas
            tarjeta = response.css(".Lector-de-Tarjetas::text")[1].getall()

            # Teclado Iluminado
            teclado_iluminado = response.css(".Teclado-Iluminado::text")[1].getall()

            # cantidad entrada usb
            cantidad_entrada_usb = response.css(".Entradas-USB::text")[1].getall()

            # Lector de huella
            lector_de_huella = response.css(".Lector-de-Huella::text")[1].getall()

            # camara web
            camara_web = response.css(".Camara-web::text")[1].getall()

            # conectividad
            conectividad = response.css(".Conectividad::text")[1].getall()

            # bluetooh
            bluetooh = response.css(".Bluetooth::text")[1].getall()

            # disco duro
            disco_duro = response.css(".Disco-Duro::text")[1].getall()

            # cantidad entrada hdmi
            cantidad_entrada_hdmi = response.css(".Entradas-HDMI::text")[1].getall()

            # SKU
            sku = response.css(".SKU::text")[1].getall()

            # garantia
            garantia = response.css(".Garantia::text")[1].getall()

            # ram
            ram = response.css(".Memoria-RAM::text")[1].getall()

            # modelo
            modelo = response.css(".Modelo::text")[1].getall()

            #procesador
            procesador = response.css(".Procesador::text")[1].getall()

            # velocidad del procesador
            velocidad_del_procesador = response.css(".Velocidad-del-procesador::text")[1].getall()

            # resolución de pantalla
            resolucion_pantalla = response.css(".Resolucion-de-la-pantalla::text")[1].getall()

            #sistema operativo
            sistema_operativo = response.css(".Sistema-operativo::text")[1].getall()

            # tamaño de pantalla
            tamaño_de_pantalla = response.css(".Tamano-de-la-pantalla::text")[1].getall()

            # tarjeta de video 
            tarjeta_de_video = response.css(".Tarjeta-de-video::text"[1]).getall()

            # tipo de pantalla
            tipo_de_pantalla = response.css(".Tipo-de-pantalla::text")[1].getall()

            # pantalla touch
            pantalla_touch = response.css(".Pantalla-Touch::text")[1].getall()

            #batería
            bateria = response.css(".Bateria::text")[1].getall()

            #duración de la batería
            duracion_bateria = response.css(".Duracion-de-la-bateria::text")[1].getall()       

            # tipo de producto
            tipo_producto = response.css(".Tipo-de-Producto::text")[1].getall()

            # parlantes
            parlantes = response.css(".Parlantes::text")[1].getall()

            # largo(cm)
            largo_cm = response.css(".Largo-cm-::text")[1].getall()

            # ancho(cm)
            ancho_cm = response.css(".Ancho-Cm-::text")[1].getall()

            # espesor(cm)
            espesor_cm = response.css(".Espesor-cm-::text")[1].getall()

            # peso (kg)
            peso_kg = response.css(".Peso::text")[1].getall()

            # Disponible
            disponibilidad = response.xpath("//div[@class='border']/div/p[4]/text()").getall()

            # Marca
            marca = response.xpath("//*[@id='titulo-marca']/div/div[1]/h2/div/a/text()").get()
            

        except:

            precio_online = None
            precio_tarjeta_oh = None
            tarjeta = None
            teclado_iluminado = None
            cantidad_entrada_usb = None
            lector_de_huella = None
            camara_web = None
            conectividad = None
            bluetooh = None
            disco_duro = None
            cantidad_entrada_hdmi = None
            sku = None
            garantia = None
            ram = None
            modelo = None
            procesador = None
            velocidad_del_procesador = None
            resolucion_pantalla = None
            sistema_operativo = None
            tamaño_de_pantalla = None
            tarjeta_de_video = None
            tipo_de_pantalla = None
            pantalla_touch = None
            bateria = None
            duracion_bateria = None
            tipo_producto = None
            parlantes = None
            largo_cm = None
            ancho_cm = None
            espesor_cm = None
            peso_kg = None
            disponibilidad = None
            marca = None
        

        
         
        # Retorno de los valores de las columnas específicadas
        yield {
            'Titulo': titulo,
            'Link': link,
            'precio_normal': precio_normal,
            'precio_online':precio_online,
            'precio_tarjeta_oh':precio_tarjeta_oh,
            'disponible': disponibilidad,
            'marca': marca,
            'link_imagen': link_imagen,
            'tarjeta': tarjeta,
            'sku': sku,
            'teclado_iluminado': teclado_iluminado,
            'lector_de_huella': lector_de_huella,
            'camara_web': camara_web,
            'conectividad':conectividad,
            'bluetooh': bluetooh,
            'disco_duro': disco_duro,
            'cantidad_entrada_hdmi': cantidad_entrada_hdmi,
            'cantidad_entrada_usb': cantidad_entrada_usb,
            'garantia': garantia,
            'ram': ram,
            'modelo': modelo,
            'procesador': procesador,
            'velocidad_del_procesador': velocidad_del_procesador,
            'resolucion_pantalla': resolucion_pantalla, 
            'sistema_operativo': sistema_operativo,
            'tamaño_de_pantalla': tamaño_de_pantalla,
            'tarjeta_de_video': tarjeta_de_video,
            'tipo_de_pantalla': tipo_de_pantalla,
            'pantalla_touch': pantalla_touch,
            'bateria': bateria,
            'duracion_bateria': duracion_bateria,
            'tipo_producto': tipo_producto,
            'parlantes': parlantes,
            'largo_cm': largo_cm, 
            'ancho_cm': ancho_cm,
            'espesor_cm': espesor_cm, 
            'peso_kg': peso_kg, 
            'disponibilidad': disponibilidad, 
            }

        

'''  
Salida en formato CSV: scrapy runspider oechsle.py -o oechsle.csv
'''
