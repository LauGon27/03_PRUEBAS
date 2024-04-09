# Proyecto Crímenes y Víctimas


## Alcance del Proyecto y captura de Datos

Los datos que se utilizaron para este estudio están relacionados con incidentes de crímenes de la ciudad de Chicago desde el año 2001 hasta la actualidad (Exceptuando asesinatos). La información es extraída del sistema CLEAR (Citizen Law Enforcement Analysis and Reporting) del Departamento de Policía de Chicago.

- Crimes - 2001 to Present | City of Chicago | Data Portal (https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data)
- Crimes - 2001 to Present - Catalog (https://catalog.data.gov/dataset/crimes-2001-to-present)

Para este caso, se plantea como objetivo tener una tabla(incidentes de crímenes) que pertenezca a la base de datos de fuentes de  verdad con este objetivo se debe tener en cuenta que se busca mantener una calidad de datos por lo que se debe tener en cuenta varios aspectos como precisión, integridad, consistencia, seguridad, documentación adecuada,también deben de estar dentro de la política de gobierno de datos que se tenga establecida y ser actualizados regularmente.

De igual forma el objetivo final es que esta fuente de datos pueda ser usada para realizar análisis de crímenes por lo que debe estar disponible para cualquier usuario final que lo necesite.


## Explorar y evaluar los datos, el EDA.


En este caso se realizó un análisis exploratorio de datos que se encuentra en la carpeta 02_eda donde se encuentra tanto para crímenes y víctimas.

Los pasos necesarios para limpiar los datos se muestran en el diagrama a continuación que es el proceso de limpieza propuesto para crímenes

![Diagram](https://github.com/LauGon27/03_PRUEBAS/blob/e615a7aee198ff18cfd5ae978ef8414936288f75/05_readme_info/limpieza.png)

## Definir el modelo de datos

El modelo que se definió en este caso es un modelo entidad-relación:

![Diagram](https://github.com/LauGon27/03_PRUEBAS/blob/e615a7aee198ff18cfd5ae978ef8414936288f75/05_readme_info/modelo_conceptual.png)

La arquitectura que se propone para el proceso se desarrolla en AWS como se muestra a continuación:

![Diagram](https://github.com/LauGon27/03_PRUEBAS/blob/e615a7aee198ff18cfd5ae978ef8414936288f75/05_readme_info/Arquitectura.png)

La razón de seleccionar los servicios de AWS es debido a que es la nube con la que he interactuado en el momento, al igual que las demás herramientas utilizadas para desarrollar el ejercicio. Pero esto no significa que no este dispuesta a trabajar en otras herramientas.

Según la fuente de información los datos que se encuentran disponibles son actualizados diariamente pero no se tienen registros de los últimos 7 días por lo que para este caso propongo que la información se debería obtener cada semana teniendo en cuenta que se puede consultar por la API pero presenta algunas limitaciones cuando se realiza la consulta por pues tiene un limite de 1000 por defecto y al modificarlo se pueden tener hasta 2900 según lo explorado

# Ejecutar la ETL

En este caso se hizo el proceso para crímenes pero teniendo en cuenta que se tomaron todos los datos disponibles por lo que no se construyó la función lambda de origen de datos teniendo en cuenta que la API de consulta tiene una limitación de 1000 registros por consulta por lo que para este ejercicio no era viable, de igual forma utilizando la función lambda se puede hacer una carga incremental de datos aunque es necesario entender que con esto los costos de la operación por lo que se recomendaría descargar primero todos los datos y luego si generar la carga incremental de forma condicionada.

Dentro del script del Job se agregó un componente de registro de información sobre el funcionamiento del programa(loggings) aunque idealmente en toda la arquitectura se debe considerar que al estar en AWS se pueda utilizar CloudWatch para registrar los eventos de ejecución y registrar los eventos de funcionamiento de los demás componentes de la arquitectura.
Adicionalmente, para verificar que la tubería funcione correctamente, desarrollaría un orquestador que ejecute la arquitectura propuesta y que cuente con sensores para tener el seguimiento de la ejecución del flujo de trabajo.

Adicionalmente, para verificar que la tubería funcione correctamente, desarrollaría un orquestador que ejecute la arquitectura propuesta y que cuente con sensores para tener el seguimiento de la ejecución del flujo de trabajo

En este caso se recomienda utilizar un sistema de calidad de datos para tener un control en la calidad de datos, en este caso se puede utilizar AWS Data Quality o con el que estoy familizarizada es Great Expectations que permite crear las expectativas de calidad de datos como uno lo requiera y se puedan hacer distintas integraciones además que es software libre.

En la carpeta 03_jobs se encuentra dividida por el código fuente (src) y el código de test unitarios (test) de las funciones utilizadas, para esto se hizo uso de la librería Pytest y se hicieron las pruebas en local

Para este punto se hizo el uso de Terraform para crear la infraestructura de la solución que se encuentra en la carpeta 01_iac. Es necesario aclarar que no se hizo el desarrollo por medio de módulos debido a que es una infraestructura simple además por temas de tiempo y teniendo en cuenta que solo se creo un usuario para la creación de los elementos, en el caso de permisos o accesos,creación de usuarios o roles no se hizo la automatización pero si es necesario tener claro que se deben dar accesos a Lambda, Glue, Athena, en este caso se dieron accesos completos al usuario o rol que fuera necesario.

# Completar la redacción del proyecto

-**¿Cuál es el objetivo del proyecto?**

El objetivo del proyecto es disponibilizar la información de crímenes históricos para permitir el uso, estudio y facilitar su acceso a los usuarios por medio de un catálogo de datos de forma sencilla y segura, donde se pueda garantizar la información.
-**¿Qué preguntas quieres hacer?**

En este caso sería interesante realizar diferentes estudios por ubicación dentro de la ciudad de Chicago, estudiar las zonas que presentan mayor violencia, el comportamiento de los crímenes a través del tiempo.
-**¿Por qué eligió el modelo que eligió?**

Elegí el modelo por la forma de origen de los datos al mismo tiempo por que se puede relacionar a partir del número de caso con las víctimas, con los arrestos, o a partir del distrito con la estación de policía donde se llevó el caso.

-**Incluya una descripción de cómo abordaría el problema de manera diferente en los siguientes escenarios:**
    - Si los datos se incrementaran en 100x.

En este caso seguiría trabajando desde la nube, se debe es mirar directamente  el tema del aprovisionamiento de los Jobs para que tengan una ejecución ideal y no gastar recursos innecesarios, lo que si sería importante revisar, es si la forma de ingestión de datos sería correcta o si se deben hacer modificaciones para hacer este proceso de una mejor forma, también se puede ver si es necesario ejecutarlo con una frecuencia menor  y  pues agregaría un orquestador que primero sea el encargado de ejecutar pero también que tenga la capacidad de mantener la integridad de los datos

 - Si las tuberías se ejecutaran diariamente en una ventana de tiempo especifica.

Similar a lo anterior, utilizaría un orquestador que ejecutara el proceso diariamente en el momento especificado

- Si la base de datos necesitara ser accedido por más de 100 usuarios funcionales.

En este caso como se esta creando en AWS, crearía un grupo (con los accesos necesarios) donde los usuarios se puedan incluir sin necesidad de estar modificando para cada uno de ellos estos permisos.

- Si se requiere hacer analítica en tiempo real, ¿Cuáles componentes cambiarias a su
arquitectura propuesta?

En este punto y bajo mis conocimientos, tengo claro que Glue en específico no es para trabajar procesos en tiempo real si no batch por lo que de pronto será necesario cambiar esta parte de la arquitectura y utilizar un Kinesis o un Lambda.