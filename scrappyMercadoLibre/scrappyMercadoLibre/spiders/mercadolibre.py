from scrapy.spiders import CrawlSpider, Rule #librería para extarcción de datos
from scrapy.linkextractors import LinkExtractor
from numpy import nan #librería para datos
from lxml import etree
import requests


#busqueda = input("¿que artículo deseas buscar en Mercado Libre?: ")

class MercadolibreSpider(CrawlSpider):
    name = 'mercadolibre' # Nombre de la web a escanear
    allowed_domains = ['articulo.mercadolibre.com.pe', 'click1.mercadolibre.com.pe', 'listado.mercadolibre.com.pe']
    # start_urls = ['https://listado.mercadolibre.com.pe/{}'.format(busqueda)]
    start_urls = ['https://listado.mercadolibre.com.pe/computacion/laptops']

    rules = (
        Rule(LinkExtractor(allow='_Desde'), follow=True),
        Rule(LinkExtractor(allow='MPE-'), callback='parse_filter', follow=True),
    )

    def parse_filter(self, response):

        # Titulo
        titulo = response.xpath("//div[@class='ui-pdp-header__title-container']/h1/text()").get()

        # Link
        link = response.xpath("//div[@class='ui-pdp-container__row ui-pdp-container__row--main-actions']/form/div/input[2]/@value").get()
        
        # Precio
        precio = response.xpath("//div[@class='ui-pdp-price__second-line']/span[1]/span[1]/text()").get()
        if precio.split(' ')[-1]=='soles':
           precio = float(precio.split(' ')[0] + '.00')
        elif precio.split(' ')[-1]=='céntimos':
            precio = float(precio.split(' ')[0] + '.' + precio.split(' ')[3] + '0')
        else:
            precio = nan

        # Link Imagen
        #linkimagen = response.css(".ui-pdp-gallery__figure__image::text").get()
        
        # Estado
        estado = response.xpath("//div[@class='ui-pdp-header']/div/span/text()").get()
        estado = estado.split(" ")[0]

        # Puntuación
        puntuacion = response.xpath("//p[@class='ui-review-view__rating__summary__average']/text()").get()
        # puntuacion = response.css(".ui-review-view__rating__summary__average::text").extract()

        # Ubicación de procedencia del artículo
        ubicacion = response.xpath("//div[@class='ui-seller-info__status-info']/div/p[2]/text()").get()

        #####

        # Marca
        marca = response.xpath("//div[@class='ui-vpp-highlighted-specs__striped-specs']/div[1]/div[1]/table/tbody/tr[1]/td/span/text()").getall()

        # Modelo linea
        modelo_linea = response.xpath("//div[@class='ui-vpp-highlighted-specs__striped-specs']/div[1]/div[1]/table/tbody/tr[2]/td/span/text()").getall()

        # Modelo
        modelo = response.xpath("//div[@class='ui-vpp-highlighted-specs__striped-specs']/div[1]/div[1]/table/tbody/tr[3]/td/span/text()").getall()

        #####

        ram = response.xpath("//div[@class='ui-vpp-highlighted-specs__striped-specs']/div[2]/div[1]/table/tbody/tr[1]/td/span/text()").getall()

        capacidad = response.xpath("//div[@class='ui-vpp-highlighted-specs__striped-specs']/div[2]/div[1]/table/tbody/tr[2]/td/span/text()").getall()
        
        almacenamiento = response.xpath("//div[@class='ui-vpp-highlighted-specs__striped-specs']/div[2]/div[2]/table/tbody/tr[1]/td/span/text()").getall()

        sistemaoperativo = response.xpath("//div[@class='ui-vpp-highlighted-specs__striped-specs']/div[1]/div[3]/table/tbody/tr[1]/td/span/text()").getall()


        # Volumen
        #capacidad = response.css(".ui-pdp-list__text::text").getall()

        # Condición Envío (gratis ó  no envío gratis)
        condicion = response.css(".ui-pdp-media__title::text").getall()

        # Descripción
        #descripcion = response.css(".ui-pdp-description__content::text").getall()

        # Disponibilidad (cantidad disponible)
        disponibilidad = response.css(".ui-pdp-family--SEMIBOLD::text").getall()

        # Oferta
        oferta = response.css(".andes-money-amount__discount::text").getall()

        # Procesador
        #velocidaddelprocesador = 

        # Memoria Ram
        #caracteristicas1 = response.xpath("//div[@class='ui-vpp-striped-specs__table']/table/tbody/tr[1]/td/span/text()").getall()
        #caracteristicas1 = {"{}".format(i):j for i,j in enumerate(caracteristicas1)}

        # Memoria Ram
        #caracteristicas2 = response.xpath("//div[@class='ui-vpp-striped-specs__table']/table/tbody/tr[2]/td/span/text()").getall()
        #caracteristicas2 = {"{}".format(i):j for i,j in enumerate(caracteristicas2)}

        # Memoria Ram
        #caracteristicas3 = response.xpath("//div[@class='ui-vpp-striped-specs__table']/table/tbody/tr[3]/td/span/text()").getall()
        #caracteristicas3 = {"{}".format(i):j for i,j in enumerate(caracteristicas3)}
        

        # Entrada USB

        # Entradas HDMI

        # Alto
        
        #Ancho
        
        #Peso 

        #Tarjeta de Video
        
        #Tipo De Pantalla
        
        #Lector de Huella
        
        #Disco Duro
        
        #Resolución de la pantalla


        # Comentarios de los Clientes
        comentarios = response.css(".ui-pdp-questions__questions-list__question::text").getall()
        comentarios = {"{}".format(i):j for i,j in enumerate(comentarios)}
        

        # Retorno de los valores de las columnas específicadas
        yield {
            'Titulo': titulo,
            'Link': link,
            'Precio': precio,
            'Estado': estado,
            #'Link_Imagen': linkimagen,
            'Puntuacion': puntuacion,            
            'Ubicacion': ubicacion,
            'Marca': marca,
            'Modelo': modelo,
            'Capacidad': capacidad,
            'Condicion': condicion,
            #'descripcion': descripcion,
            'disponibilidad': disponibilidad,
            'oferta': oferta,
            'Comentarios': comentarios,
            #'características1': caracteristicas1,
            #'características2': caracteristicas2,
            #'características3': caracteristicas3,
            'modelo_linea': modelo_linea,
            'ram': ram,
            'almacenamiento': almacenamiento,
            'sistema_operativo': sistemaoperativo,
            }

        #Página inicial para scraping horizontal↓↓↓
        #pag_inicial = response.find('span', attrs={"class":"andes-pagination__link"}).text
        #pag_inicial = int(pag_inicial)
        #Página final para scraping horizontal↓↓↓
        #pag_final = response.find('li', attrs={"class":"andes-pagination__page-count"}).text.split(" ")[-1]
        #pag_final = int(pag_final)
