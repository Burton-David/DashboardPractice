# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

'''
There are a few things to keep in mind when including assets automatically:

1 - The following file types will automatically be included:

A - CSS files suffixed with .css

B - JavaScript files suffixed with .js

C - A single file named favicon.ico (the page tab's icon)

2 - Dash will include the files in alphanumerical order by filename. So, we recommend prefixing your filenames with numbers if you need to ensure their order (e.g. 10_typography.css, 20_header.css)

3 - You can ignore certain files in your assets folder with a regex filter using app = dash.Dash(assets_ignore='.*ignored.*'). This will prevent Dash from loading files which contain the above pattern.

4 - If you want to include CSS from a remote URL, then see the next section.

5 - Your custom CSS will be included after the Dash component CSS

6 - It is recommended to add __name__ to the dash init to ensure the resources in the assets folder are loaded,
eg: app = dash.Dash(__name__, meta_tags=[...]). When you run your application through some other command line (like the
flask command or gunicorn/waitress), the __main__ module will no longer be located where app.py is. By explicitly
setting __name__, D ash will be able to locate the relative assets folder correctly.
'''
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv("KingsCountyHousingLR/kc_house_data.csv")


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# This is the Dash Constructor.  Make sure adding "app = dash.Dash(__name__)" to dash init
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='Kings County Housing Data'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
