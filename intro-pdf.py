#!/usr/bin/env python3

# imports
import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

# data
cbd_onhand = {
    "lotion": 20, 
    "tincture": 10, 
    "flower": 87, 
    "oil": 55, 
    "t-shirts": 20, 
    "hats": 10 
}
path = os.getcwd()
os.chdir(path)
report_pie = Pie(width=4, height=4)
report = SimpleDocTemplate(
    "/Users/nathanchilton/desktop/code-library/python/pdf/cbdreport.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A complete inventory of our CBD items", styles["h1"])
table_data = []
for k, v in cbd_onhand.items():
    table_data.append([k, v])
table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
report_pie.data = []
report_pie.labels = []
for item_name in sorted(cbd_onhand):
    report_pie.data.append(cbd_onhand[item_name])
    report_pie.labels.append(item_name)


report_chart = Drawing()
report_chart.add(report_pie)
report_table = Table(data=table_data, style=table_style, hAlign="CENTER")
report.build([report_title, report_table, report_chart])
