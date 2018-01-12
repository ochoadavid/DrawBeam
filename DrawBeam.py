# author: David Ochoa (ochoadavid at gmail.com)
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def showsave(name):
    '''Prints and saves images given a name.'''
    plt.axis('equal')
    plt.axis('off')
    #plt.tight_layout(pad=-1)
    if name is not None:
        plt.savefig(name, dpi=90, bbox_inches='tight')
    plt.show()

def rotate(vx, vy, angle):
    '''Helper function to rotate arrays.'''
    angle_rad = np.radians(angle)
    vrx = vx * np.cos(angle_rad) + vy * np.sin(angle_rad)
    vry = -vx * np.sin(angle_rad) + vy * np.cos(angle_rad)
    return vrx, vry

def rep_vector(x1, y1, x2, y2, lineformat='-', label='', shw_label=True, shw_mag=False, 
               shw_angle=False, shw_legend=True, aligned=False, arrow_scale = 0.02, offset = 1, fdict={}):
    '''Plot a vector (line with arrow). It can show a legend and magnitude and angle values.'''
    mag = np.sqrt((y2-y1)**2+(x2-x1)**2)
    angle = np.degrees(np.arctan2((y2-y1),(x2-x1)))
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    ux = (x2-x1) / mag
    uy = (y2-y1) / mag
    if arrow_scale == 0:
        x = [x1,x2]
        y = [y1,y2]
    else:
        awx = ux * mag * arrow_scale
        awy = uy * mag * arrow_scale
        x = [x1,x2,x2-awy*.45-awx,x2+awy*.45-awx,x2]
        y = [y1,y2,y2+awx*.45-awy,y2-awx*.45-awy,y2]
    if shw_legend:
        plt.plot(x,y,lineformat, label=label)
    else:
        plt.plot(x,y,lineformat)

    if aligned:
        text_angle = np.degrees(np.arctan((y2-y1)/(x2-x1)))
    else:
        text_angle = 0 
    ux = (x2-x1) / mag * np.sign(angle)
    uy = (y2-y1) / mag * np.sign(angle)
    try:
        if len(offset) == 2:
            uy, ux = offset
            ux = -ux
            offset = 1
    except:
        pass
    fd = fdict.copy()
    fd.update({'ha':'center', 'va':'center'})
    if shw_label:
        plt.text(cx + uy * offset, cy - ux * offset, label, fontdict=fd, rotation=text_angle)
    if shw_mag and shw_angle:
        plt.text(cx - uy * offset, cy + ux * offset, r'${:.2f} \angle {:.2f}^o$'.format(mag,angle), fontdict=fd, rotation=text_angle)
    elif shw_mag:
        plt.text(cx - uy * offset, cy + ux * offset, '{:.2f}'.format(mag), fontdict=fd, rotation=text_angle)
    elif shw_angle:
        plt.text(cx - uy * offset, cy + ux * offset, r'$\angle {:.2f}^o$'.format(angle), fontdict=fd, rotation=text_angle)

def rep_pinned(x, y, scale=1, label='', shw_label=False, rotation=0, lineformat='k-'):
    '''Plot a pinned support.'''
    x_triangle = np.array([0, -0.35, 0.35, 0])
    y_triangle = np.array([0, -0.6, -0.6, 0])
    x_strp = np.array([-0.35, -0.5, -0.35, -0.175, -0.325, -0.175, 0.0, -0.15, 0.0, 0.175, 0.025, 0.175, 0.35, 0.2, 0.35])
    y_strp = np.array([-0.6, -0.75, -0.6, -0.6, -0.75, -0.6, -0.6, -0.75, -0.6, -0.6, -0.75, -0.6, -0.6, -0.75, -0.6])
    x_triangle = x_triangle * scale
    y_triangle = y_triangle * scale
    x_strp = x_strp * scale
    y_strp = y_strp * scale
    plt.plot(x_triangle+x, y_triangle+y, lineformat, lw=1)
    plt.plot(x_strp+x, y_strp+y, lineformat, lw=0.5)
    if (shw_label == True) or (shw_label == 'right'):
        plt.text(0.4*scale + x, -0.8*scale + y, label)
    elif (shw_label == 'left'):
        plt.text(-0.45*scale + x, -0.8*scale + y, label)

def rep_roller(x, y, scale=1, label='', shw_label=False, rotation=0, lineformat='k-'):
    '''Plot a roller support.'''
    ang = np.linspace(0,2,18) * np.pi
    cx = 0.072 * np.cos(ang)
    cy = 0.072 * np.sin(ang)
    x_triangle = np.array([0, -0.35, 0.35, 0])
    y_triangle = np.array([0, -0.6, -0.6, 0])
    x_strp = np.array([-0.35, -0.5, -0.35, -0.175, -0.325, -0.175, 0.0, -0.15, 0.0, 0.175, 0.025, 0.175, 0.35, 0.2, 0.35])
    y_strp = np.array([-0.75, -0.9, -0.75, -0.75, -0.9, -0.75, -0.75, -0.9, -0.75, -0.75, -0.9, -0.75, -0.75, -0.9, -0.75])
    x_c1 = (cx - 0.25) * scale
    y_c1 = (cy - 0.675) * scale
    x_c2 = (cx - 0.0) * scale
    y_c2 = (cy - 0.675) * scale
    x_c3 = (cx + 0.25) * scale
    y_c3 = (cy - 0.675) * scale
    x_triangle = x_triangle * scale
    y_triangle = y_triangle * scale
    x_strp = x_strp * scale
    y_strp = y_strp * scale
    if (rotation != 0):
        x_triangle, y_triangle = rotate(x_triangle, y_triangle, rotation)
        x_strp, y_strp = rotate(x_strp, y_strp, rotation)
        x_c1, y_c1 = rotate(x_c1, y_c1, rotation)
        x_c2, y_c2 = rotate(x_c2, y_c2, rotation)
        x_c3, y_c3 = rotate(x_c3, y_c3, rotation)
    plt.plot(x_triangle+x, y_triangle+y, lineformat, lw=1)
    plt.plot(x_strp+x, y_strp+y, lineformat, lw=0.5)
    plt.plot(x_c1+x, y_c1+y, lineformat, lw=0.5)
    plt.plot(x_c2+x, y_c2+y, lineformat, lw=0.5)
    plt.plot(x_c3+x, y_c3+y, lineformat, lw=0.5)
    if (shw_label == True) or (shw_label == 'right'):
        plt.text(0.4*scale + x, -0.8*scale + y, label)
    elif (shw_label == 'left'):
        plt.text(-0.45*scale + x, -0.8*scale + y, label)
        
def rep_fix(x, y, scale=1, label='', shw_label=False, rotation=0, lineformat='k-'):
    '''Plot a fixed support.'''
    x_triangle = np.array([0, 0])
    y_triangle = np.array([-0.35, 0.35])
    x_strp = np.array([0.0, -0.15, 0.0, 0.0, -0.15, 0.0, 0.0, -0.15, 0.0, 0.0, -0.15, 0.0, 0.0, -0.15, 0.0])
    y_strp = np.array([-0.35, -0.5, -0.35, -0.175, -0.325, -0.175, 0.0, -0.15, 0.0, 0.175, 0.025, 0.175, 0.35, 0.2, 0.35])
    x_triangle = x_triangle * scale
    y_triangle = y_triangle * scale
    x_strp = x_strp * scale
    y_strp = y_strp * scale
    if (rotation != 0):
        x_triangle, y_triangle = rotate(x_triangle, y_triangle, rotation)
        x_strp, y_strp = rotate(x_strp, y_strp, rotation)
    plt.plot(x_triangle+x, y_triangle+y, lineformat, lw=1)
    plt.plot(x_strp+x, y_strp+y, lineformat, lw=0.5)
    if (shw_label == True) or (shw_label == 'right'):
        plt.text(0.05*scale + x, -0.8*scale + y, label)
    elif (shw_label == 'left'):
        plt.text(-0.4*scale + x, -0.6*scale + y, label)    
    
def rep_none(x, y, scale=1, label='', shw_label=False, rotation=0, lineformat='k-'):
    '''Plot a beam end without suppport, helper function to place labels.'''
    if (shw_label == True) or (shw_label == 'right'):
        plt.text(0.05*scale + x, -0.6*scale + y, label)
    elif (shw_label == 'left'):
        plt.text(-0.10*scale + x, -0.6*scale + y, label) 

def rep_axis(x=0, y=0, scale=1, shw_label=True, lineformat='k-'):
    '''Plots x,y axis lines.'''
    x_x = np.array([-1, 1])
    x_y = np.array([0, 0])
    y_x = np.array([0, 0])
    y_y = np.array([-1, 1])
    x_x = x_x * scale
    x_y = x_y * scale
    y_x = y_x * scale
    y_y = y_y * scale
    plt.plot(x_x + x, x_y + y, lineformat, lw=0.5)
    plt.plot(y_x + x, y_y + y, lineformat, lw=0.5)
    if shw_label:
        plt.text(x_x[1]*1.1, -.25*scale, 'x')
        plt.text(-0.25*scale, y_y[1]*1.1, 'y')

def rep_element(x1, x2, y1, y2, lineformat='k-', fill=True):
    '''Plots a beam or element (filled rectangle).'''
    x = np.array([x1, x1, x2, x2, x1])
    y = np.array([y1, y2, y2, y1, y1])
    if fill:
        polygon = Polygon(np.vstack((x,y)).T, True)
        p = PatchCollection([polygon], alpha=0.2)
        ax = plt.gca()
        ax.add_collection(p)
    plt.plot(x, y, lineformat, lw=1.5)

def rep_leng(x1, x2, y1, y2, lineformat='k-', offset=-1, label='', shw_label=True, label_offset=0.5, arrow_scale=0.015):
    '''Plots a aligned lenght measure.'''
    mag = np.sqrt((y2-y1)**2+(x2-x1)**2)
    angle = np.degrees(np.arctan2((y2-y1),(x2-x1)))
    ux = (x2-x1) / mag * offset
    uy = (y2-y1) / mag * offset
    rep_vector(x1-uy, y1+ux, x2-uy, y2+ux, aligned=False, lineformat='k-', 
               label=label, shw_label=True, arrow_scale=arrow_scale, offset=label_offset)
    rep_vector(x2-uy, y2+ux, x1-uy, y1+ux, aligned=False, lineformat='k-', 
               label='', shw_label=False, arrow_scale=arrow_scale)
    plt.plot([x1, x1-uy*1.2],[y1, y1+ux*1.2],lineformat, lw=0.5)
    plt.plot([x2, x2-uy*1.2],[y2, y2+ux*1.2],lineformat, lw=0.5)

def rep_dist(x1, x2, y1, y2, lineformat='k-', arrows=3, function=(lambda x: 1),
          offset=-1, label='', shw_label=True, label_offset=0.5, arrow_scale=0.15):
    '''Plots a distributed load.'''
    mag = np.sqrt((y2-y1)**2+(x2-x1)**2)
    angle = np.degrees(np.arctan2((y2-y1),(x2-x1)))
    ux = (x2-x1) / mag
    uy = (y2-y1) / mag
    for i in range (arrows):
        t = i / (arrows - 1)
        px = x1 * (1-t) + x2 * t
        py = y1 * (1-t) + y2 * t
        rep_vector(px-uy*function(t), py+ux*function(t), px, py, lineformat=lineformat, 
                   shw_label=False, arrow_scale=arrow_scale)
    rep_vector(x1-uy*function(0), y1+ux*function(0), x2-uy*function(1), y2+ux*function(1), lineformat=lineformat, 
                   shw_label=shw_label, label=label, arrow_scale=0, offset=label_offset)

def rep_pair(x, y, diameter, start_angle, end_angle, lineformat='k-', 
          label_angle=0, offset=-1, label='', shw_label=True, label_offset=0.5, arrow_scale=.6):
    '''Plots a couple force (moment).'''
    s_ang = np.deg2rad(start_angle)
    e_ang = np.deg2rad(end_angle)
    ang = np.linspace(s_ang,e_ang,50)
    cx = diameter * np.cos(ang)
    cy = diameter * np.sin(ang)
    plt.plot(cx+x,cy+y,lineformat)
    rep_vector(cx[-10]+x, cy[-10]+y, cx[-1]+x, cy[-1]+y, lineformat=lineformat, 
                   shw_label=shw_label, label=label, arrow_scale=arrow_scale, offset=label_offset)
    rep_axis(x=x, y=y, scale=diameter/4, shw_label=False, lineformat=lineformat)
