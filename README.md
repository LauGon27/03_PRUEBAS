# Proyecto Crímenes y Víctimas
.

## Alcance del Proyecto y captura de Datos
--- 

Los datos que se utilizaran para este estudio están relacionados con incidentes de crímenes de la ciudad de Chicago desde el año 2001 hasta la actualidad (Exceptuando asesinatos). La información es extraída del sistema CLEAR (Citizen Law Enforcement Analysis and Reporting) del Departamento de Policía de Chicago.
Crimes - 2001 to Present | City of Chicago | Data Portal (https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data)
Crimes - 2001 to Present - Catalog (https://catalog.data.gov/dataset/crimes-2001-to-present)

En este caso será una tabla que pertenece a la base de datos verdad por lo que se debe tener en cuenta que para usarla con este objetivo se debe tener en cuenta que se busca mantener una calidad de datos por lo que se debe tener en cuenta varios aspectos como precisión, integridad, consistencia, seguridad, documentación adecuada,también deben de estar dentro de la política de gobierno de datos que se tenga establecida y ser actualizados regularmente. 

De igual forma el objetivo final es que esta fuente de datos pueda ser usada para realizar análisis de crímenes por lo que debe estar disponible para cualquier usuario final que lo necesite.


## Explorar y evaluar los datos, el EDA.
---

En este caso se realizó un análisis exploratorio de datos que se encuentra en la carpeta 02_EDA donde se encuentra tanto para crímenes y víctimas. 

Los pasos necesarios para limpiar los datos se muestran en el diagrama a continuación donde se muestra el proceso de limpieza propuesto para crímenes

![Diagram](https://github.com/LauGon27/03_PRUEBAS/blob/e615a7aee198ff18cfd5ae978ef8414936288f75/05_readme_info/limpieza.png)

## Definir el modelo de datos

El modelo que se definió en este caso es un modelo entidad relación:

![Diagram](https://github.com/LauGon27/03_PRUEBAS/blob/e615a7aee198ff18cfd5ae978ef8414936288f75/05_readme_info/modelo_conceptual.png)

La arquitectura que se propone para el proceso se desarrolla en AWS como se muestra a continuación:

![Diagram](https://github.com/LauGon27/03_PRUEBAS/blob/e615a7aee198ff18cfd5ae978ef8414936288f75/05_readme_info/Arquitectura.png)

La razón de seleccionar los servicios de AWS es debido a que es la nube con la que he interactuado en el momento, al igual que las demás herramientas utilizadas para desarrollar el ejercicio, de igual forma el ejercicio realizado fue útil como preparación para la certificación de AWS Cloud Practitioner para la cual me estoy preparando. Pero esto no significa que no este abierta a trabajar en otras herramientas y de igual forma me parece importante estar lista para aprender nuevas herramientas. 

Según la fuente de información los datos que se encuentran disponibles son actualizados diariamente pero no se tienen registros de los últimos 7 días por lo que para este caso propongo que la información se debería obtener cada semana teniendo en cuenta que se puede consultar por la API pero presenta algunas limitaciones cuando se realiza la consulta por este medio