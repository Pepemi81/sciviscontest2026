import numpy as np
import OpenVisus as ov
from datetime import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

print("--------------------------------------- \n")

try:
    dataset_url="https://atlantis.sci.utah.edu/mod_visus?dataset=nex-gddp-cmip6"
    db=ov.LoadDataset(dataset_url)
except:
    dataset_url="https://us-east-1.gw.future-tech-holdings.com/nasa-t0/nex-gddp-cmip6/nex-gddp-cmip6.idx"


model     = "ACCESS-CM2"
variable  = "pr" #pr: precipitacion tas: temp
scenario  = "historical"
timestamp = '2010-04-20' #aaaa-mm-dd

field = f"{variable}_day_{model}_{scenario}_r1i1p1f1_gn"

def calculate_day_of_year(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    start_of_year = datetime(date.year, 1, 1)
    day_of_year = (date - start_of_year).days
    return day_of_year

def get_timestep(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    day_of_year = calculate_day_of_year(date_str)
    total_days = 365 + (1 if (date.year % 4 == 0 and date.year % 100 != 0) or (date.year % 400 == 0) else 0)
    return f"{date.year*total_days+day_of_year}"

timestep_index=int(get_timestep(timestamp))
#print(timestep_index)

db=ov.LoadDataset(dataset_url)
print(f'Dimensions: {db.getLogicBox()[1][0]}*{db.getLogicBox()[1][1]}')
print(f'Total Timesteps: {len(db.getTimesteps())}')


#print(f'Field: {field}')
#print('Data Type: float32')
data=db.read(time=timestep_index,quality=0,field=field)
data.shape


#visualizacion


def test_visualization():
    
    y_max, x_max = data.shape
    xlabels = [str(x) for x in range(0, 360, 50)]
    ylabels = [str(y) for y in range(-60, 90, 20)]
    xticks = np.linspace(0, x_max, len(xlabels))
    yticks = np.linspace(0, y_max, len(ylabels))

    # Create the plot
    fig, axes = plt.subplots(1, 1,figsize=(10, 8))
    axes.set_xticks(xticks)
    axes.set_xticklabels(xlabels)
    axes.set_yticks(yticks)
    axes.set_yticklabels(ylabels)

    # Plot the data
    im = axes.imshow(data[:, :], origin='lower', cmap='turbo')

    divider = make_axes_locatable(axes)
    cax = divider.append_axes("right", size="5%", pad=0.1)  # Adjust size and pad as needed

    # Add the colorbar
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_label('Precipitation (kg m-2 s-1)')

    # Show the plot
    plt.show()


test_visualization()


print("---------------------------------------")
