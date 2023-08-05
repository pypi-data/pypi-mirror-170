from urllib.request import urlretrieve as _urlretrieve
import math

from extcolors import extract_from_image as _extract_from_image
from PIL import Image as _Image, ImageDraw as _ImageDraw
from matplotlib import gridspec as _gridspec
import matplotlib.pyplot as _plt
import PIL as _PIL

from .misc import cFormatter

__all__ = [
    "study_image",
    "_fetch_img",
    "_sch_extract_colors",
]


def study_image(image_path):
    print(cFormatter("Estudiando la imagen via HTTPS...", color="green"))
    img = _fetch_img(image_path)
    colors = _sch_extract_colors(img)
    color_palette = _render_color_palette(colors)
    _overlay_palette(img, color_palette)
    print(cFormatter("Estudio finalizado.Se ha creado una pestaña con el estudio de la imagen correctamente", color="green"))

def _fetch_img(image_path):
    print(cFormatter("Leyendo la imagen y creando un espacio temporal en su disco...", color="green"))
    try:
        _urlretrieve(image_path, "image")
    except Exception as e:
        print(cFormatter(f"Error al leer la imagen: {e}", color="red"))
        exit()
    finally:
        img = _PIL.Image.open("image")
    return img

def _sch_extract_colors(img):
    print(cFormatter("Extrayendo el patron de colores de la imagen...", color="green"))
    tolerance = 32
    limit = 24
    colors, pixel_count = _extract_from_image(img, tolerance, limit)
    return colors

def _render_color_palette(colors):
    print(cFormatter("Renderizando la paleta y creando una capa...", color="green"))
    size = 100
    columns = 6
    width = int(min(len(colors), columns) * size)
    height = int((math.floor(len(colors) / columns) + 1) * size)
    result = _Image.new("RGBA", (width, height), (0, 0, 0, 0))
    canvas = _ImageDraw.Draw(result)
    for idx, color in enumerate(colors):
        x = int((idx % columns) * size)
        y = int(math.floor(idx / columns) * size)
        canvas.rectangle([(x, y), (x + size - 1, y + size - 1)], fill=color[0])
    return result

def _overlay_palette(img, color_palette):
    print(cFormatter("Creando una pestaña con el estudio de la imagen y la paleta renderizada...", color="green"))
    nrow = 2
    ncol = 1
    f = _plt.figure(figsize=(20,30), facecolor='None', edgecolor='k', dpi=55, num=None)   # Crea una figura de 20x30 pixeles para la paleta de colores
    gs = _gridspec.GridSpec(nrow, ncol, wspace=0.0, hspace=0.0)                           # Crea un grid de 2x1, con un espacio de 0 entre filas y columnas
    f.add_subplot(2, 1, 1)
    _plt.imshow(img, interpolation='nearest')                                             # Muestra la imagen original en la primera fila del grid
    _plt.axis('off')                                                                      # Deshabilita los ejes de la imagen
    f.add_subplot(1, 2, 2)
    _plt.imshow(color_palette, interpolation='nearest')
    _plt.axis('off')
    _plt.subplots_adjust(wspace=0, hspace=0, bottom=0)
    _plt.show(block=True)