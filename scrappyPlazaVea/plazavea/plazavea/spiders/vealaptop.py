import scrapy
import pandas as pd
from scrapy_splash import SplashRequest
from numpy import nan

class VealaptopSpider(scrapy.Spider):
    name = 'vealaptop'
    
    file = pd.read_csv("links.csv")
    links =list(file['links'])

    #def start_requests(self):
    #    url = 'https://www.plazavea.com.pe/laptops?ft=laptops'
    #    yield SplashRequest(url)

    def start_requests(self):
        for url in self.links:
            yield SplashRequest(url=url, callback=self.parse_products)
        

    def parse_products(self,response):

        titulo = response.xpath("/html/body/div[4]/div[4]/div[1]/div[4]/div[1]/div[1]/h6/div/text()").get()
        link = response.url
        
        # precio
        #precio_normal = response.xpath("//div[@class='ProductCard__price ProductCard__price--regular']/div/span[2]/text()").get()
        #precio_internet = response.css("//div[@class='ProductCard__price ProductCard__price--online']/div/span[2]/text()").get()
        #precio_tarjeta_oh = response.xpath("/html/body/div[4]/div[4]/div[1]/div[4]/div[2]/div[3]/div[4]/div[1]/span[2]/text()").get()
        # precio_normal = response.css(".ProductCard__price__integer::text").getall()


        #marca
        try:
            marca = response.xpath("//div[@class='ProductCard__information__productdata__name']/span/div/a/text()")[1].get()

        except:
            marca = None

        #modelo
        try:
            modelo = response.css(".Modelo::text")[1].getall()
        except:
            modelo = None

        # tarjeta de video
        try:
            tarjeta_de_video = response.css(".Tarjeta-de-Video::text")[1].getall()
        except:
            tarjeta_de_video = None

        # procesador  computo
        try:
            procesador_de_video = response.css(".Procesador-Computo::text")[1].getall()
        except:
            procesador_de_video = None

        # ram
        try:
            ram = response.css(".Memoria-RAM::text")[1].getall()
        except:
            ram = None

        #entrada usb
        try:
            cant_entrada_usb = response.css(".Entradas-USB::text")[1].getall()
        except:
            cant_entrada_usb = None

        # entrada hdmi
        try:
            hdmi = response.css(".Entradas-HDMI::text")[1].getall()
        except:
            hdmi = None

        # sistema operativo
        try:
            sistema_operativo = response.css(".Sistema-Operativo::text")[1].getall()
        except:
            sistema_operativo = None


        # tamaño de pantalla
        try:
            pantalla = response.css(".Pantalla-Computo-Pulgadas-::text")[1].getall()
        except:
            pantalla = None

        # tipo de pantalla
        try:
            tipo_de_pantalla = response.css(".Tipo-De-Pantalla::text")[1].getall()

        except:
            tipo_de_pantalla =  None

        # tipo de disco
        try:
            tipo_disco = response.css(".Tipo-De-Disco-Duro::text")[1].getall()
        except:
            tipo_disco = None

        # disco duro
        try:
            disco_duro = response.css(".Capacidad-De-Disco-Duro::text")[1].getall()
        except:
            disco_duro = None

        # disco solido
        try:
            disco_solido = response.css(".Disco-Duro-Solido::text")[1].getall()
        except:
            disco_solido = None

        #camara
        try:
            camara = response.css(".Camara::text")[1].getall()
        except:
            camara = None

        # alto (cm)
        try:
            alto_cm = response.css(".Alto-cm-::text")[1].getall()

        except:
            alto_cm = None

        # ancho (cm)
        try:
            ancho_cm = response.css(".Ancho-cm-::text")[1].getall()

        except:
            ancho_cm = None

        # profundidad (cm)
        try:
            profundidad_cm = response.css(".Profundidad-cm-::text")[1].getall()

        except:
            profundidad_cm = None

        yield{
            'titulo': titulo,
            'link': link,
            #'precio_normal': precio_normal,
            #'precio_internet': precio_internet,
            #'precio_tarjeta_oh': precio_tarjeta_oh,
            'modelo': modelo,
            'marca': marca,
            'tarjeta_de_video': tarjeta_de_video,
            'procesador_de_video': procesador_de_video,
            'ram': ram,
            'cant_entrada_usb': cant_entrada_usb,
            'hdmi': hdmi,
            'pantalla': pantalla,
            'tipo_disco': tipo_disco,
            'disco_duro': disco_duro,
            'disco_solido': disco_solido,
            'camara': camara,
            'tipo_de_pantalla': tipo_de_pantalla,
            'sistema_operativo': sistema_operativo,
            'alto_cm': alto_cm,
            'ancho_cm': ancho_cm,
            'profundidad_cm': profundidad_cm,
        }


