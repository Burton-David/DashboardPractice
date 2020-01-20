# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# This is the Dash Constructor.  Make sure adding "app = dash.Dash(__name__)" to dash init
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
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
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
