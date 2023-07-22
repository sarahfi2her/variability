#### imports ###################################################################

from library import scale_fn
from IPython import display
from matplotlib.animation import FuncAnimation, FFMpegWriter
import matplotlib.pyplot as plt
import numpy as np

#### class definition ##########################################################

class Histogram():
    def __init__(self, pop, bins, ylim=0, density=False, color='grey', title='', 
                 xlabel='', ylabel='', save=''):
        self.pop = pop
        self.bins = bins
        self.ylim = ylim
        self.density = density
        self.color = color
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.save = save

    def show(self):
        plt.hist(self.pop, bins=self.bins, density=self.density, 
                 color=self.color)
        if self.ylim != 0:
            plt.ylim(0, self.ylim)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        if self.save != '':
            plt.savefig(self.save, dpi=300,  bbox_inches='tight')
        plt.show()
        return
    
class HistogramAnimated():
    def __init__(self, pop_dict, elapsed_dict, bins, ylim, density=False, 
                 color='grey', xlabel='', ylabel='', title='', save=''):
        self.pop_dict = pop_dict
        self.timestep_list = sorted(self.pop_dict.keys())
        self.elapsed_dict = elapsed_dict
        self.bins = bins
        self.ylim = ylim
        self.density = density
        self.color = color
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.save = save

    def show(self):
        fig, ax = plt.subplots()
        pop = self.pop_dict[self.timestep_list[0]]
        _, _, bar_container = ax.hist(pop, self.bins, lw=1, 
                                      ec=self.color, fc=self.color)
        ax.set_ylim(top=self.ylim)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        title = ax.text(0.5, 1.05, '', transform=ax.transAxes, ha='center')

        def prepare_animation(bar_container):
            def animate(t):
                title.set_text(f'{self.title} ({int(self.elapsed_dict[t])} hr)')
                pop = self.pop_dict[t]
                n, _ = np.histogram(pop, self.bins)
                for count, rect in zip(n, bar_container.patches):
                    rect.set_height(count)
                return bar_container.patches, title
            return animate
        
        ani = FuncAnimation(fig, prepare_animation(bar_container), 
                            self.timestep_list, repeat=False, blit=True)
        if self.save != '':
            writervideo = FFMpegWriter(fps=10)
            ani.save(self.save, dpi=300, writer=writervideo)
        video = ani.to_html5_video()
        html = display.HTML(video)
        display.display(html)
        plt.close() 
        return
    
class HistogramMultiple():
    def __init__(self, pop_list, bins, ylim=0, density=False, label_list=[],
                 color_list=['grey'], alpha=0.5, title='', xlabel='', ylabel='', 
                 save=''):
        self.pop_list = pop_list
        self.bins = bins
        self.ylim = ylim
        self.density = density
        self.label_list = label_list
        self.color_list = color_list
        self.alpha = alpha
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.save = save

    def show(self):
        if self.label_list == []:
            if len(self.color_list) != len(self.pop_list):
                for p in self.pop_list:
                    plt.hist(p, bins=self.bins, density=self.density, 
                             color=self.color_list[0], alpha=self.alpha)
            else:
                for p, c in zip(self.pop_list, self.color_list):
                    plt.hist(p, bins=self.bins, density=self.density, color=c, 
                             alpha=self.alpha)
        else:
            if len(self.color_list) != len(self.pop_list):
                for p, l in zip(self.pop_list, self.label_list):
                    plt.hist(p, bins=self.bins, density=self.density,
                             color=self.color_list[0], alpha=self.alpha, 
                             label=l)
            else:
                for p, c, l in zip(self.pop_list, self.color_list, 
                                   self.label_list):
                    plt.hist(p, bins=self.bins, density=self.density, color=c, 
                             alpha=self.alpha, label=l)
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        if self.ylim != 0:
            plt.ylim(0, self.ylim)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        if self.save != '':
            plt.savefig(self.save, dpi=300,  bbox_inches='tight')
        plt.show()
        return
    
class LorenzPlot():
    def __init__(self, unscaled_pop=[], scaled_pop=[], equal_color='grey', 
                 equal_label='', unscaled_color='grey', unscaled_label='', 
                 scaled_color='grey', scaled_label='', title='', xlabel='', 
                 ylabel='', save=''):
        self.unscaled_pop = unscaled_pop
        self.scaled_pop = scaled_pop
        self.equal_color = equal_color
        self.equal_label = equal_label
        self.unscaled_color = unscaled_color
        self.unscaled_label = unscaled_label
        self.scaled_color = scaled_color
        self.scaled_label = scaled_label
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.save = save

    def show(self):
        if self.equal_label == '':
            plt.plot([0,1], [0,1], linestyle='--', color=self.equal_color, 
                    alpha=0.5)
        else:
            plt.plot([0,1], [0,1], linestyle='--', color=self.equal_color, 
                    alpha=0.5, label=self.equal_label)
        if self.unscaled_pop != []:
            x = np.array(self.unscaled_pop).cumsum() / sum(self.unscaled_pop)
            x = np.insert(x, 0, 0) 
            x[0], x[-1]
            if self.unscaled_label == '':
                plt.plot(np.arange(x.size)/(x.size-1), x, 1, 
                        color=self.unscaled_color) 
            else:
                plt.plot(np.arange(x.size)/(x.size-1), x, 1, 
                         color=self.unscaled_color, label=self.unscaled_label)
        if self.scaled_pop != []:
            x = np.array(self.scaled_pop).cumsum() / sum(self.scaled_pop)
            x = np.insert(x, 0, 0) 
            x[0], x[-1]
            if self.scaled_label == '':
                plt.plot(np.arange(x.size)/(x.size-1), x, 1, 
                         color=self.scaled_color) 
            else:
                plt.plot(np.arange(x.size)/(x.size-1), x, 1, 
                         color=self.scaled_color, label=self.scaled_label)
        
        if (self.equal_label != '' or self.unscaled_label != '' or 
            self.scaled_label != ''):
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        if self.save != '':
            plt.savefig(self.save, dpi=300,  bbox_inches='tight')
        plt.show()
        return

class LorenzPlotAnimated():
    def __init__(self, gini_obj_list, elapsed_dict, equal_color='grey', 
                 equal_label='', unscaled=False, scaled=False, 
                 color_list=[], label_list=[], title='', xlabel='', 
                 ylabel='', save=''):
        self.gini_obj_list = gini_obj_list
        self.elapsed_dict = elapsed_dict
        self.timestep_list = gini_obj_list[0].timestep_list
        self.pop_dict_list = self.get_pop_dict_list(unscaled, scaled)
        self.gini_dict_list = self.get_gini_dict_list(unscaled, scaled)
        self.equal_color = equal_color
        self.equal_label = equal_label
        self.color_list = color_list
        self.label_list = label_list
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.save = save
    
    def get_pop_dict_list(self, unscaled, scaled):
        pop_dict_list = []
        if unscaled:
            pop_dict_list.extend([x.pop_dict for x in self.gini_obj_list])
        if scaled:
            pop_dict_list.extend([x.scaled_pop_dict 
                                  for x in self.gini_obj_list])
        return pop_dict_list
    
    def get_gini_dict_list(self, unscaled, scaled):
        gini_dict_list = []
        if unscaled:
            gini_dict_list.extend([x.gini_dict for x in self.gini_obj_list])
        if scaled:
            gini_dict_list.extend([x.scaled_gini_dict 
                                   for x in self.gini_obj_list])
        return gini_dict_list
    
    def show(self):
        fig, ax = plt.subplots()
        lines = []
        for i, pop_dict in enumerate(self.pop_dict_list):
            x = (np.array(pop_dict[self.timestep_list[0]]).cumsum() / 
                 sum(pop_dict[self.timestep_list[0]]))
            x = np.insert(x, 0, 0) 
            x[0], x[-1]
            if self.color_list == []:
                if self.label_list == []:
                    line, = ax.plot(np.arange(x.size)/(x.size-1), x)
                else:
                    line, = ax.plot(np.arange(x.size)/(x.size-1), x, 
                                    label=self.label_list[i])
            else:
                if self.label_list == []:
                    line, = ax.plot(np.arange(x.size)/(x.size-1), x, 
                                    color=self.color_list[i])
                else:
                    line, = ax.plot(np.arange(x.size)/(x.size-1), x, 
                                    label=self.label_list[i], 
                                    color=self.color_list[i])
            lines.append(line)
            
        if self.equal_label == '':
            plt.plot([0,1], [0,1], linestyle='--', color=self.equal_color, 
                     alpha=0.5)
        else:
            plt.plot([0,1], [0,1], linestyle='--', color=self.equal_color, 
                     alpha=0.5, label=self.equal_label)
        
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        title = ax.text(0.5, 1.05, '', transform=ax.transAxes, ha='center')
        if self.label_list != []:
            L = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        def animate(t):
            title.set_text(f'{self.title} ({int(self.elapsed_dict[t])} hr)')
            for i, pop_dict in enumerate(self.pop_dict_list):
                x = np.array(pop_dict[t]).cumsum() / sum(pop_dict[t])
                x = np.insert(x, 0, 0) 
                x[0], x[-1]
                lines[i].set_xdata(np.arange(x.size)/(x.size-1))
                lines[i].set_ydata(x)
                if self.label_list != []:
                    gini = round(self.gini_dict_list[i][t], 2)
                    label = (f'{self.label_list[i]} (Gini Index: '\
                             f'{str(gini).ljust(4, str(0))})')
                    L.get_texts()[i].set_text(label)
                    plt.tight_layout(rect=[0, 0, 1, 0.95]) 
            return lines

        ani = FuncAnimation(fig, animate, self.timestep_list, blit=True)
        
        if self.save != '':
            writervideo = FFMpegWriter(fps=10)
            ani.save(self.save, dpi=300, writer=writervideo)
        video = ani.to_html5_video()
        html = display.HTML(video)
        display.display(html)
        plt.close() 
        return
        
    
class Matrix():
    def __init__(self, matrix, cmap=plt.cm.Greens, clim=(0,1), xticklabels=[],
                 xticks=[], yticklabels=[], yticks=[], title='', cbar_label='',
                 xlabel='', ylabel='', save=''):
        self.matrix = matrix
        self.cmap = cmap
        self.clim = clim 
        self.xticklabels = xticklabels
        self.xticks = xticks
        self.yticklabels = yticklabels
        self.yticks = yticks
        self.title = title
        self.cbar_label = cbar_label
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.save = save

    def show(self):
        fig, ax = plt.subplots(1,1)
        img = ax.imshow(self.matrix, cmap=self.cmap, clim=self.clim) 
        ax.set_xticks(self.xticks)
        ax.set_xticklabels(self.xticklabels)
        ax.set_yticks(self.yticks)
        ax.set_yticklabels(self.yticklabels)
        fig.colorbar(img, cbar_label='',)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        if self.save != '':
            plt.savefig(self.save, dpi=300,  bbox_inches='tight')
        plt.show()
        return
        
class MatrixAnimated():
    def __init__(self, matrix_dict, elapsed_dict, cmap=plt.cm.Greens, clim=(0,1), 
                 xticklabels=[], xticks=[], yticklabels=[], yticks=[], 
                 cbar_label='', xlabel='', ylabel='', title='', save=''):
        self.matrix_dict = matrix_dict
        self.elapsed_dict = elapsed_dict
        self.timestep_list = sorted(matrix_dict.keys())
        self.cmap = cmap
        self.clim = clim 
        self.xticklabels = xticklabels
        self.xticks = xticks
        self.yticklabels = yticklabels
        self.yticks = yticks
        self.title = title
        self.cbar_label =cbar_label
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.save = save
    
    def show(self):
        fig, ax = plt.subplots(1, 1)
        im = ax.imshow(self.matrix_dict[self.timestep_list[0]], 
                       cmap=self.cmap, animated=True)
        plt.yticks(self.yticks, self.yticklabels)
        plt.xticks(self.xticks, self.xticklabels)
        im.set_clim(vmin=self.clim[0], vmax=self.clim[1])
        plt.colorbar(im, label=self.cbar_label)

        def update(t):
            im.set_array(self.matrix_dict[t])
            ax.set_title(f'{self.title} ({int(self.elapsed_dict[t])} hr)')
            return im

        ani = FuncAnimation(fig, update, frames=self.timestep_list)
        
        if self.save != '':
            writervideo = FFMpegWriter(fps=10)
            ani.save(self.save, dpi=300, writer=writervideo)
        video = ani.to_html5_video()
        html = display.HTML(video)
        display.display(html)
        plt.close() 
        return


class PlotLine():
    def __init__(self, x_list, y_list, avg=1, label_list=[], color_list=[], 
                 axv_x_list=[], axv_label_list=[], axv_color_list=['grey'], 
                 temp_x=[], temp_y=[], temp_avg=1, temp_label='', 
                 temp_color='grey', title='', xlabel='', ylabel='', save=''):
        self.x_list, self.y_list = self.get_xy_avg(x_list, y_list, avg)
        self.label_list = label_list
        self.color_list = color_list
        self.axv_x_list = axv_x_list
        self.axv_label_list = axv_label_list
        self.axv_color_list = axv_color_list
        self.temp_x, self.temp_y = self.get_xy_avg([temp_x], 
                                                   [scale_fn(temp_y, 
                                                             self.get_y_lims())]
                                                             , temp_avg)
        self.temp_avg = temp_avg
        self.temp_label = temp_label
        self.temp_color = temp_color
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.save = save

    def get_xy_avg(self, x_list, y_list, avg):
        x_res = []
        y_res = []
        for x, y in zip(x_list, y_list):
            x_temp = [x[i:i+avg] for i in range(len(x)-avg+1)]
            x_res.append([np.array(x).mean() for x in x_temp])
            y_temp = [y[i:i+avg] for i in range(len(y)-avg+1)]
            y_res.append([np.array(y).mean() for y in y_temp])
        return x_res, y_res
    
    def get_y_lims(self):
        lo = min([min(l) for l in self.y_list])
        hi = max([max(l) for l in self.y_list])
        return [lo, hi]
    
    def show(self):
        if self.label_list == []:
            if self.color_list == []:
                for x, y in zip(self.x_list, self.y_list):
                    plt.plot(x, y)
            else:
                for x, y, c in zip(self.x_list, self.y_list, self.color_list):
                    plt.plot(x, y, color=c)
        else:
            if self.color_list == []:
                for x, y, l in zip(self.x_list, self.y_list, self.label_list):
                    plt.plot(x, y, label=l)
            else: 
                for x, y, l, c in zip(self.x_list, self.y_list, self.label_list, 
                                      self.color_list):
                    plt.plot(x, y, color=c, label=l)

        if self.axv_x_list != []:
            if self.axv_label_list == []:
                if len(self.axv_color_list) != len(self.axv_x_list):
                    for x in self.axv_x_list:
                        plt.axvline(x, color=self.axv_color_list[0], 
                                    linestyle='--')
                else:
                    for x, c in zip(self.axv_x_list, self.axv_color_list):
                        plt.axvline(x, color=c, linestyle='--')
            else:
                if len(self.axv_color_list) != len(self.axv_x_list):
                    for x, l in zip(self.axv_x_list, self.axv_label_list):
                        plt.axvline(x, color=self.axv_color_list[0], 
                                    linestyle='--', label=l)
                else:
                    for x, c, l in zip(self.axv_x_list, self.axv_color_list, 
                                       self.axv_label_list):
                        plt.axvline(x, color=c, linestyle='--', label=l)

        if self.temp_x != []:
            if self.temp_label == '':
                plt.plot(self.temp_x[0], self.temp_y[0], color=self.temp_color)
            else:
                plt.plot(self.temp_x[0], self.temp_y[0], color=self.temp_color, 
                         label=self.temp_label)
                
        if (self.label_list != [] or self.axv_label_list != [] or 
            self.temp_label != ''):
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        if self.save != '':
            plt.savefig(self.save, dpi=300,  bbox_inches='tight')
        plt.show()
        return
    
################################################################################