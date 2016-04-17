#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Template
import sys

sys.path += ['.']

def generate_navit_config():
    from jinja2 import Environment, PackageLoader
    env = Environment(loader=PackageLoader('navit-templates','templates'))
    template = env.get_template('navit.xml')
    text_file = open("./build/navit.xml", "w")

    context = {
        'defaults': {
            'text': {
                'color': '#333333',
                'background': '#EEEEEE',
                'size': 15,
                'size_small': 10
            },
            'icon': {
                'size': 24,
                'size_small': 12,
                'size_medium': 18,

            }
        },
        'default_font': 'Liberation Sans',
        'default_language': 'es_UY.UTF-8',
        'navit': {
            'center': '-34.8833 -56.1667',
            'pitch': 15
        },
        'polygons': {
            'text': {
                'color': '#333333FF',
                'size': 7
            }
        },
        'water': {
            'color': '#acbdc8',
            'border': {
                'color': '#acbdc8',
                'size': 1
            }

        },
        'streets': {
            'color': '#FFFFFF',
            'border': {
                'color': '#D7D7D7'
            },
            'selected_line': {
                'color': '#BA00B8'
            },
            'service': {
                'color': '#FFFFFF',
                'border': {
                    'color': '#D7D7D7'
                }
            },
            'level2': {
                'color': '#FFFFFF',
                'border': {
                    'color': '#D7D7D7'
                }
            },
            'level3': {
                'color': '#FFFFFF',
                'border': {
                    'color': '#D7D7D7'
                }
            },
            'level4': {
                'color': '#FFFFFF',
                'border': {
                    'color': '#D7D7D7'
                }
            },
            'highway': {
                'color': '#FFFFFF',
                'border': {
                    'color': '#D7D7D7'
                }
            },
            'n_lanes': {
                'color': '#FFFFFF',
                'border': {
                    'color': '#D7D7D7'
                }
            },
            
            'pedestrian': {
                'color': '#FFFFFF',
                'border': {
                    'color': '#D7D7D7'
                }
            },
            'route': {
                'color': '#FFA500',
                'border': {
                    'color': '#FFA500'
                }
            },

        },
        'labels': {
            'text': {
                'color': '#222222',
                'size': 10
            },
            'radius': 3
        },
        'ground': {
            'recreation_ground': {
                'color': '#c4dbc8'
            }
        },
        'building': {
            'color': '#a8a390',
            'border' : {
                'width': 1,
                'color': '#a8a390'
            }
        },
        'car_parking': {
            'color': '#a8a390',
            'border' : {
                'width': 1,
                'color': '#a8a390'
            }
        },
        'footway': {
            'color': '#DEDEDE',
            'show': False
        },
        'cycleway': {
            'color': '#DEDEDE'
        }, 
        'rail': {
            'color': '#FFFFFF',
            'border': {
                'color': '#696969'
            }
        },
        'ramp': {
            'color': '#FFFFFF',
            'border': {
                'color': '#EEEEEE'
            }
        },
        'traffic_distortion': {
            'color': '#FF9000'
        }



    }

    text_file.write(template.render(context).encode('utf-8'))
    text_file.close()


if __name__ == '__main__':
    generate_navit_config()