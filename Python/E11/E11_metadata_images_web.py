import argparse
import requests
import os
from bs4 import BeautifulSoup
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image

         
def scrapingBeautifulSoup(url):

    try:
        print("Obteniendo imagenes de la url: "+ url)
        
        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'lxml')
        
        #create directory for save images
        os.system("mkdir Imagenes_descargadas")

        for tagImage in bs.find_all("img"): 
            #print(tagImage['src'])
            if tagImage['src'].startswith("http") == False:
                download = url + tagImage['src']
            else:
                download = tagImage['src']
            # download images in img directory
            r = requests.get(download)
            f = open('Imagenes_descargadas/%s' % download.split('/')[-1], 'wb')
            f.write(r.content)
            f.close()
    
    except Exception as e:
            print(e)
            print("Error conexion " + url)
            pass

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
 
def get_exif_metadata(image_path):
    ret = {}
    try:
        image = Image.open(image_path)
        if hasattr(image, '_getexif'):
            exifinfo = image._getexif()
            if exifinfo is not None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
        decode_gps_info(ret)
        return ret
    except Exception as e:
        import sys, traceback
        pass
    
def imagenMeta(ruta):
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            ext = name.rsplit('.', 1)[-1]
            name_file = name.rsplit('.', 1)
            if (ext in ['jpg']) or (ext in ['jpeg']):
                #print(os.path.join(root, name))
                try:
                    exifData = {}
                    exif = get_exif_metadata(name)
                    if len(exif) != 0:
                        archivo = open(name_file[0]+'.txt', 'a')
                        archivo.write("[+] Metadata for file: %s " %(name))
                        archivo.write("\n")
                        for metadata in exif:
                            archivo.write(metadata)
                            archivo.write("Metadata:"+ str(metadata)+ " - Value: "+ str(exif[metadata]))
                            archivo.write("\n")
                        archivo.close()
                except Exception as e:
                    pass
    print("Imagenes analizadas.")

if __name__ == '__main__':
    description = """Ejemplo de uso:
            + Brindar informacion del script
                    py E11_metadata_images_web.py -h

            + Ingresar url para buscar imagenes:
                    py E11_metadata_images_web.py -link https://www.uanl.mx/enlinea/ """
    parser = argparse.ArgumentParser(description='Metadata de Imagenes Web', epilog=description,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-link', dest='link', help='URL de las imagenes a buscar')
    args = parser.parse_args()
    link = args.link
    scrapingBeautifulSoup(link)
    os.chdir("Imagenes_descargadas")
    dir = os.getcwd()
    imagenMeta(dir)
