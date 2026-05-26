#Pregunta 1
import arcpy
import os

arcpy.env.workspace = r"C:\PIG\Test.gdb"
arcpy.env.overwriteOutput = True

print("Entorno de ArcPy inicializado correctamente.")
print("Workspace:", arcpy.env.workspace)

#Pregunta 2
import arcpy

arcpy.env.workspace = r"C:\PIG\Test.gdb"

puntos = arcpy.ListFeatureClasses(feature_type="Point")
lineas = arcpy.ListFeatureClasses(feature_type="Line")

print("Clases de entidad de puntos:", puntos)
print("Clases de entidad de líneas:", lineas)

#Pregunta 3
import arcpy

arcpy.env.workspace = r"C:\PIG\Test.gdb"

capa_puntos = "points_3857"
desc = arcpy.Describe(capa_puntos)

print(f"Nombre de la entidad: {desc.name}")
print(f"Tipo de geometría: {desc.shapeType}")
print(f"Campo ID interno: {desc.OIDFieldName}")
print(f"Sistema de coordenadas: {desc.spatialReference.name}")
print(f"Unidades lineales: {desc.spatialReference.linearUnitName}")

#Pregunta 4
import arcpy
import os

gdb_path = r"C:\PIG\Test.gdb"
dataset_name = "autumn"

referencia_capa = os.path.join(gdb_path, "points_3857")
dataset_completo = os.path.join(gdb_path, dataset_name)

if arcpy.Exists(dataset_completo):
    print(f"El Feature Dataset '{dataset_name}' ya existe.")
else:
    spatial_ref = arcpy.Describe(referencia_capa).spatialReference
    arcpy.management.CreateFeatureDataset(
        out_dataset_path=gdb_path,
        out_name=dataset_name,
        spatial_reference=spatial_ref
    )
    print(f"Feature Dataset '{dataset_name}' creado correctamente.")

#Pregunta 5
import arcpy

arcpy.env.workspace = r"C:\PIG\Test.gdb"

campos = arcpy.ListFields("points_3857")

print("Estructura de campos:")
for campo in campos:
    print(f"Campo: {campo.name} | Tipo: {campo.type} | Longitud: {campo.length}")

#Pregunta 5
import arcpy

arcpy.env.workspace = r"C:\PIG\Test.gdb"

resultado_conteo = arcpy.management.GetCount("points_3857")
total = int(resultado_conteo[0])

print(f"Total de registros en points_3857: {total}")


#Pregunta 6
import arcpy

arcpy.env.workspace = r"C:\PIG\Test.gdb"

arcpy.management.MakeFeatureLayer(
    in_features="points_3857",
    out_layer="lyr_puntos"
)

print("Capa temporal creada: lyr_puntos")

#Pregunta 7
import arcpy

arcpy.env.workspace = r"C:\PIG\Test.gdb"

arcpy.management.MakeFeatureLayer("points_3857", "lyr_puntos")

consulta = "bird_name IN ('Folkert', 'Kees', 'Ale')"

arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="lyr_puntos",
    selection_type="NEW_SELECTION",
    where_clause=consulta
)

conteo = int(arcpy.management.GetCount("lyr_puntos")[0])
print("Registros seleccionados:", conteo)

#pregunta 8
import arcpy

arcpy.env.workspace = r"C:\PIG\Test.gdb"
arcpy.env.overwriteOutput = True

capa = r"C:\PIG\Test.gdb\points_3857"
lyr = "lyr_tiempo"

if arcpy.Exists(lyr):
    arcpy.management.Delete(lyr)

arcpy.management.MakeFeatureLayer(capa, lyr)

campo_fecha = '"timestamp"'

consulta = (
    f"{campo_fecha} >= '2007-03-01 00:00:00' "
    f"AND {campo_fecha} <= '2007-06-01 00:00:00'"
)

print("Consulta usada:")
print(consulta)

arcpy.management.SelectLayerByAttribute(
    in_layer_or_view=lyr,
    selection_type="NEW_SELECTION",
    where_clause=consulta
)

conteo = int(arcpy.management.GetCount(lyr)[0])
print("Registros dentro del intervalo temporal:", conteo)

# Solución a la Pregunta 9
import arcpy

# Configurar el espacio de trabajo real
arcpy.env.workspace = r"C:\PIG\Test.gdb"

# 1. Crear la capa temporal en memoria
if arcpy.Exists("lyr_filtro_ambiental"):
    arcpy.management.Delete("lyr_filtro_ambiental")

arcpy.management.MakeFeatureLayer("points_3857", "lyr_filtro_ambiental")

# 2. Sentencia compuesta utilizando los nombres de campo reales verificados
sql_compuesta = "vw_mtss IS NOT NULL AND vg_mtss_gcd > 4"

try:
    # 3. Ejecutar la selección atributiva sobre la capa temporal
    arcpy.management.SelectLayerByAttribute("lyr_filtro_ambiental", "NEW_SELECTION", sql_compuesta)
    
    # 4. Obtener el conteo de registros que cumplen la condición
    resultado_conteo = arcpy.management.GetCount("lyr_filtro_ambiental")
    total_puntos = int(resultado_conteo.getOutput(0))
    
    print(f"Éxito: Consulta SQL ejecutada correctamente.")
    print(f"Puntos que cumplen con el criterio de vuelo activo con datos de viento: {total_puntos}")

except arcpy.ExecuteError:
    print("Error de geoprocesamiento de ArcGIS:")
    print(arcpy.GetMessages(2))
except Exception as e:
    print(f"Error general del script: {str(e)}")


