showsave(name)
    '''Prints and saves images given a name.'''

rotate(vx, vy, angle)
    '''Helper function to rotate arrays.'''

rep_vector(x1, y1, x2, y2, lineformat='-', label='', shw_label=True, shw_mag=False, 
               shw_angle=False, shw_legend=True, aligned=False, arrow_scale = 0.02, offset = 1, fdict={})
    '''Plot a vector (line with arrow). It can show a legend and magnitude and angle values.'''

rep_pinned(x, y, scale=1, label='', shw_label=False, rotation=0, lineformat='k-')
    '''Plot a pinned support.'''

rep_roller(x, y, scale=1, label='', shw_label=False, rotation=0, lineformat='k-')
    '''Plot a roller support.'''
        
rep_fix(x, y, scale=1, label='', shw_label=False, rotation=0, lineformat='k-')
    '''Plot a fixed support.'''
    
rep_none(x, y, scale=1, label='', shw_label=False, rotation=0, lineformat='k-')
    '''Plot a beam end without suppport, helper function to place labels.'''

rep_axis(x=0, y=0, scale=1, shw_label=True, lineformat='k-')
    '''Plots x,y axis lines.'''

rep_element(x1, x2, y1, y2, lineformat='k-', fill=True)
    '''Plots a beam or element (filled rectangle).'''
    x = np.array([x1, x1, x2, x2, x1])
    y = np.array([y1, y2, y2, y1, y1])
    if fill
        polygon = Polygon(np.vstack((x,y)).T, True)
        p = PatchCollection([polygon], alpha=0.2)
        ax = plt.gca()
        ax.add_collection(p)
    plt.plot(x, y, lineformat, lw=1.5)

rep_leng(x1, x2, y1, y2, lineformat='k-', offset=-1, label='', shw_label=True, label_offset=0.5, arrow_scale=0.015)
    '''Plots a aligned lenght measure.'''

rep_dist(x1, x2, y1, y2, lineformat='k-', arrows=3, function=(lambda x: 1),
          offset=-1, label='', shw_label=True, label_offset=0.5, arrow_scale=0.15)
    '''Plots a distributed load.'''

rep_pair(x, y, diameter, start_angle, end_angle, lineformat='k-', 
          label_angle=0, offset=-1, label='', shw_label=True, label_offset=0.5, arrow_scale=.6)
    '''Plots a couple force (moment).'''
