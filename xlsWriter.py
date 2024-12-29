import xlsxwriter

path = "Test.xlsx"
workbook = xlsxwriter.Workbook(path)
sheet = workbook.add_worksheet(name="hello")
data = [15, 55, 65, 20, 5, 10]
sheet.write_column("A1", data)

# Créer le graphique
chart = workbook.add_chart({"type": "line"})
chart.add_series({"values": "=Hello!$A$1:$A$6"})

# Ajouter le graphique à la feuille
sheet.insert_chart("C1", chart)
workbook.close()
