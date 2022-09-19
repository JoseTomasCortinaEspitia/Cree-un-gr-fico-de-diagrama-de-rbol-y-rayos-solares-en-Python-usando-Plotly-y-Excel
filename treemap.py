import plotly_express as px
import pandas as pd
import plotly

#Leer los Datos de Excel

df =pd.read_excel('data.xlsx')
#print(df)

country = df['Country']
continent = df['Continent']
region = df['Region']
sales = df['Sales']
margin = df['Profit Margin %']
remark = df['Remark']
#print(continent)


#Crear el grafico y almacenar la figura [fig]

fig = px.treemap(df,
                path=[continent,region,country],
                values=sales,
                color=margin,
                color_continuous_scale=['red','yellow','green'],
                title='Sales/Profit Overview',
                hover_name=remark)


#Actualizar/cambiar diseño

fig.update_layout(
    title_font_size=42,
    title_font_family='Arial'
)

#Guardar Gráfico y exportar a HTML

plotly.offline.plot(fig, filename='Chart.html')

