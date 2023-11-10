import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_name = 'Silk Trade.csv'
df= pd.read_csv(file_name,encoding='latin-1')
print(df)


def ExportTrend(data, country_col='Country or Area', year_col='Year', trade_col='Trade Amount', flow_col='Flow'):
    export_data = data[data[flow_col] == 'Export']
    grouped_data = export_data.groupby([year_col, country_col])[trade_col].sum().unstack()

    # Plotting the line chart
    plt.figure(figsize=(8, 8))
    for country in grouped_data.columns:
        plt.plot(grouped_data.index, grouped_data[country], label=country)

    plt.title('Trade(USD) by Year for Each Country (Export Only)')
    plt.xlabel('Year')
    plt.ylabel('Trade(USD)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Country', title_fontsize='12')
    plt.grid(True)
    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
    plt.tight_layout()
    plt.show()

ExportTrend(df)


def QuantityBar(data, commodity_col='Commodity', quantity_col='Quantity', flow_col='Flow'):

    silk_data = data[data[commodity_col].str.lower().str.contains('silk')]
    grouped_data = silk_data.groupby([commodity_col, flow_col])[quantity_col].sum().unstack()
    labels = grouped_data.index
    export_values = grouped_data['Export']
    import_values = grouped_data['Import']

    bar_width = 0.35
    index = np.arange(len(labels))

    plt.figure(figsize=(12, 8))
    plt.bar(index, export_values, width=bar_width, label='Export')
    plt.bar(index + bar_width, import_values, width=bar_width, label='Import')

    plt.xlabel('Commodity')
    plt.ylabel('Quantity')
    plt.title('Quantity of Silk in Export and Import for Each Commodity')
    plt.xticks(index + bar_width / 2, labels, rotation=45, ha='right')
    plt.legend()
    plt.grid(True)
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()
QuantityBar(df)



def TopBrazilExports(data, country_col='Country or Area', quantity_col='Quantity'):
    brazil_exports = data[(data[country_col] == 'Brazil') & (data['Flow'] == 'Export')]
    top3_exports = brazil_exports.groupby('Commodity')[quantity_col].sum().nlargest(3)
    plt.figure(figsize=(8, 8))
    plt.pie(top3_exports, labels=top3_exports.index, autopct='%1.1f%%', startangle=140)
    plt.title('Top 3 Exports from Brazil in Terms of Quantity')
    plt.show()
TopBrazilExports(df)


'''Visualization of line,  bar and pie chart
providing comparison of exports between different
countries over the years. top exports products
in terms of quantity'''






