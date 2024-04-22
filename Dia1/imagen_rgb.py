import cv2
import matplotlib.pyplot as plt

#%matplotlib inline

# Ruta de la imagen a abrir
ruta_imagen = '/home/stevend/Documents/Notebooks/Dia1/imagenes/acne.jpeg'

# Cargar la imagen
imagen = cv2.imread(ruta_imagen, cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.show()
# Mostrar la imagen en una ventana
#cv2.imshow('Imagen', img_rgb)

# Esperar a que se presione una tecla y luego cerrar la ventana
#cv2.waitKey(0)
#cv2.destroyAllWindows()