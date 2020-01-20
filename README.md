# DashboardPractice
Dash refresher that will attempt to familiarize myself with Dash and toy with its capabilities.

# The Assets Folder
## Customizing the style sheets? 
[Adding CSS & JS and Overriding the Page-Load Template](https://dash.plot.ly/external-resources) <br>
Adding Your Own CSS and JavaScript to Dash Apps
- > Optional but useful! : Turn off hot-reloading app.run_server by setting (dev_tools_hot_reload=False)
- create an assets directory within root of app directory(directly within project folder).
- You can store assets directory externally and reference it via assets_external_path='http://your-external-assets-folder-url'
- > External css/js files are loaded before the assets.
- include images within assets directory
- modify the image displayed in the browser tab by adding favicon.ico

```
- app.py
- assets/
    |-- image.png
    |-- favicon.ico

```