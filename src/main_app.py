from mysql.connector import Error
import mysql.connector




try:
	connection = mysql.connector.connect(
			host = "localhost",
			port = 3306,
			user = "root",
			password = "",
			database = "python_inserciones_masivas"
		)

	if connection.is_connected():
		print("Conexión establecida")
	else:
		print("No se pudo establecer la conexión")
except Error as ex:
	print(f"Error durante la conexión{ex}")
else:
	pass
finally:
    if connection.is_connected():
        connection.close()
        print("Conexión cerrada")

        