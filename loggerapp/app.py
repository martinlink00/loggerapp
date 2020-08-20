##############################################################################################
"""This is the main GUI app controlling the datalogging as well as a semi-life camviewer"""
##############################################################################################


import numpy as np

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_daq as daq
import signal

import plotly.graph_objects as go
import plotly.express as px

import datalogger.db_interface as db
import datalogger.gui_interface as im
import datalogger.datalogger as dat
import datalogger.iter as run
import datalogger.Thread
from datalogger.logsetup import log



##############################################################################################



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

##

guiint=im.Guiinterfacelogger(8.0)


#Keyboard interupt handling

def keyboardInterruptHandler(signal, frame):
    guiint.sensormngr.closeallcams()
    log.info("KeyboardInterrupt (ID: {}) has been caught. You can now close the Browser Tab".format(signal))
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)


#App layout

app.layout = html.Div([
    html.Div([
        html.H2('Cam View'),
        html.Div([
            html.H4('Select camera instance:'),
            dcc.Dropdown(
                    id='camview-selection',
                    options=[{'label': i, 'value': i} for i in guiint.sensormngr.getcameraliststring()],
                    value=guiint.sensormngr.getcameraliststring()[0]        
            ) 
        ],style={'backgroundColor':'rgb(250,250,250)'}),
        
        #Camera View Division
        
        html.Div([
            html.Div([
                html.Div([
                    html.H5('Full cam view:'),
                    dcc.Graph(
                    id='camview'
                    )  
                ], className='three columns'),
                html.Div([
                    html.H5('ROI view:'),
                    dcc.Graph(
                    id='roiview'
                    )  
                ], className='three columns'),
                html.Div([
                    html.H5('Fit visualisation:'),
                    dcc.Graph(
                    id='fitvis'
                    )
                ], className='three columns'),
                html.Div([
                    html.H5('Latest fit data:'),
                    html.Div([
                        html.Table([
                            html.Tr([html.Td([html.Span("Horizontal beam position:",style={'cursor':'pointer','textDecoration':'underline'})],id='hcenterhelp'), html.Td(id='hcenter')]),
                            html.Tr([html.Td([html.Span("Vertical beam position:",style={'cursor':'pointer','textDecoration': 'underline'})], id='vcenterhelp'), html.Td(id='vcenter')]),
                            html.Tr([html.Td([html.Span("Large waist:",style={'cursor':'pointer','textDecoration': 'underline'})],id='lwhelp'), html.Td(id='largewaist')]),
                            html.Tr([html.Td([html.Span("Small waist:",style={'cursor':'pointer','textDecoration': 'underline'})],id='swhelp'), html.Td(id='smallwaist')]),
                            html.Tr([html.Td([html.Span("Angle:",style={'cursor':'pointer','textDecoration': 'underline'})],id='anglehelp'), html.Td(id='angle')]),
                            html.Tr([html.Td([html.Span("ROI position:",style={'cursor':'pointer','textDecoration': 'underline'})],id='roiposhelp'), html.Td(id='roipos')]),
                            html.Tr([html.Td([html.Span("ROI width",style={'cursor':'pointer','textDecoration': 'underline'})],id='roiwhelp'), html.Td(id='roiwidth')]),
                            html.Tr([html.Td([html.Span("ROI height",style={'cursor':'pointer','textDecoration': 'underline'})],id='roihhelp'), html.Td(id='roiheight')]),
                            html.Tr([html.Td([html.Span("Pixel size",style={'cursor':'pointer','textDecoration': 'underline'})], id='pixelsizehelp'), html.Td(id='pixelsize')]),
                            dbc.Tooltip(
                                "Horizontal beam position (extracted from database), "
                                "Fitted from Y-Profile (blue lined plots)",
                                target="hcenterhelp",
                                placement="top",
                                style={'color':'white', 'backgroundColor':'black'}
                            ),
                            dbc.Tooltip(
                                "Vertical beam position (extracted from database), "
                                "Fitted from X-Profile (blue lined plots)",
                                target="vcenterhelp",
                                placement="top",
                                style={'color':'white', 'backgroundColor':'black'}
                            ),
                            dbc.Tooltip(
                                "Long beam waist (extracted from database), "
                                "Fitted from Axis-Profile (red lined plots)",
                                target="lwhelp",
                                placement="top",
                                style={'color':'white', 'backgroundColor':'black'}
                            ),
                            dbc.Tooltip(
                                "Short beam waist (extracted from database), "
                                "Fitted from Axis-Profile (red lined plots)",
                                target="swhelp",
                                placement="top",
                                style={'color':'white', 'backgroundColor':'black'}
                            ),
                            dbc.Tooltip(
                                "Beam angle (extracted from database), "
                                "Should be in (-90°,90°). 0° refers to horizontal long axis.",
                                target="anglehelp",
                                placement="top",
                                style={'color':'white', 'backgroundColor':'black'}
                            ),
                            dbc.Tooltip(
                                "ROI position (extracted from camera)",
                                target="roiposhelp",
                                placement="top",
                                style={'color':'white', 'backgroundColor':'black'}
                            ),
                            dbc.Tooltip(
                                "ROI width (extracted from camera)",
                                target="roiwhelp",
                                placement="top",
                                style={'color':'white', 'backgroundColor':'black'}
                            ),
                            dbc.Tooltip(
                                "ROI height (extracted from camera)",
                                "Fitted from Y-Profile (blue lined plots)",
                                target="roihhelp",
                                placement="top",
                                style={'color':'white', 'backgroundColor':'black'}
                            ),
                            dbc.Tooltip(
                                "Pixelsize (extracted from camera), "
                                "Non square pixels are not supported.",
                                target="pixelsizehelp",
                                placement="top",
                                style={'color':'white', 'backgroundColor':'black'}
                            )
                        ],style={'backgroundColor':'rgb(255, 255, 255)','width':'82.5%'})
                    ])
                ], className='three columns')
            ], className='row'),
            dcc.Interval(
            id='interval-cam',
    # this is the refresh rate of the page initially set to the rate of the threader. It does not change, when the slider is moved
            interval=guiint.getrate()*1000, 
            n_intervals=0
            )
        ],style={'columnCount':1}),
        
        #ROI input Division
        
        html.Div([
            html.H4('Manually reset ROI parameters:'),
            html.Div([
                html.Div([
                    dcc.Input(
                        id="roisetter-x",
                        type='number',
                        placeholder="New x-Position of ROI",
                        debounce=True,
                        style={'width': '100%'}),
                    dcc.Input(
                        id="roisetter-y",
                        type='number',
                        placeholder="New y-Position of ROI",
                        debounce=True,
                        style={'width': '100%'})
                ], className="six columns",style={'columnCount':2}),

                html.Div([
                    dcc.Input(
                        id="roisetter-w",
                        type='number',
                        placeholder="New width of ROI",
                        debounce=True,
                        style={'width': '100%'}),
                    dcc.Input(
                        id="roisetter-h",
                        type='number',
                        placeholder="New height of ROI",
                        debounce=True,
                        style={'width': '100%'})
                ], className="six columns",style={'columnCount':2})
            ], className='row'),
            html.Div(id="hidden-div", style={"display":"none"}),
            html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
            
        ], style={'backgroundColor':'rgb(250,250,250)'})
        
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)'
    }),
    html.Div([
        html.H2('Datalogger Control'),
        html.Div([
            html.Div([
                daq.PowerButton(
                    id='loggerbutton',
                    on=False,
                    size=50
                ),
                dcc.Slider(
                    id='rate-slider',
                    min=1,
                    max=20,
                    value=guiint.getrate(),
                    marks={
                            1: {'label': '1 s', 'style': {'color': '#77b0b1'}},
                            5: {'label': '5 s', 'style': {'color': '#77b0b1'}},
                            10: {'label': '10 s', 'style': {'color': '#77b0b1'}},
                            15: {'label': '15 s', 'style': {'color': '#77b0b1'}},
                            20: {'label': '20 s', 'style': {'color': '#77b0b1'}}
                        })
            

            ], className="six columns"),
            
            html.Div([
                html.Div(id='poweronoff')
            ], className="six columns")
            
            
        ], className="row")


        
        
        
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)'
    })
], style={'columnCount': 1}
)


@app.callback(
    [dash.dependencies.Output('camview', 'figure'),
    dash.dependencies.Output('roiview', 'figure'),
    dash.dependencies.Output('fitvis', 'figure'),
    dash.dependencies.Output('hcenter','children'),
    dash.dependencies.Output('vcenter','children'),
    dash.dependencies.Output('largewaist','children'),
    dash.dependencies.Output('smallwaist','children'),
    dash.dependencies.Output('angle','children'),
    dash.dependencies.Output('roipos','children'),
    dash.dependencies.Output('roiwidth','children'),
    dash.dependencies.Output('roiheight','children'),
    dash.dependencies.Output('pixelsize','children')],
    [dash.dependencies.Input('camview-selection', 'value'),
    dash.dependencies.Input('loggerbutton', 'on'),
    dash.dependencies.Input('interval-cam','n_intervals')])


def update_image(beamselection,on,n):
    guiint.selectcam(beamselection)
    if on:
        return guiint.fitvis()
    else:
        blackimg=px.imshow(np.zeros((200,200)))
        blackimg.update_layout(coloraxis_showscale=False)
        return blackimg, blackimg, blackimg, 0, 0, 0, 0, 0, 0, 0, 0, 0

    
@app.callback(
    dash.dependencies.Output('hidden-div','children'),
    [dash.dependencies.Input('submit-button-state', 'n_clicks')],
    [dash.dependencies.State('roisetter-x', 'value'),
     dash.dependencies.State('roisetter-y', 'value'),
     dash.dependencies.State('roisetter-w', 'value'),
     dash.dependencies.State('roisetter-h', 'value')]
)
    

def manuallysetroi(n_clicks,roiinputx,roiinputy,roiinputw,roiinputh):
    if roiinputx is not None:
        guiint.camviewer.getselectedcam().IA.setroi(posx=roiinputx)
        log.info("ROI x-Coordinate was changed to %f" % (roiinputx))

    if roiinputy is not None:
        guiint.camviewer.getselectedcam().IA.setroi(posy=roiinputy)
        log.info("ROI y-Coordinate was changed to %f" % (roiinputy))

    if roiinputw is not None:
        guiint.camviewer.getselectedcam().IA.setroi(width=roiinputw)
        log.info("ROI width was changed to %f" % (roiinputw))

    if roiinputh is not None:
        guiint.camviewer.getselectedcam().IA.setroi(height=roiinputh)
        log.info("ROI height was changed to %f" % (roiinputh))
    

    
@app.callback(
    dash.dependencies.Output('poweronoff', 'children'),
    [dash.dependencies.Input('loggerbutton', 'on'),
    dash.dependencies.Input('rate-slider', 'value')])

def update_output(on,rate):

    if on:
        guiint.thread.start()
        guiint.setrate(rate)
        log.info("Data is being logged every %f seconds" % (guiint.getrate()))
        return 'The datalogger is turned on and exporting every %f seconds' % (guiint.getrate())
    else:
        guiint.thread.stop()
        log.info("Data is not being logged at the moment")
        return 'The datalogger is turned off'




if __name__ == '__main__':
    app.run_server(debug=False)
