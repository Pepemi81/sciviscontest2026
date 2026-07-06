import matplotlib.pyplot as plt
import task0_data

target_variable = "tas" 
target_date = "2017-06-30"
target_scenario = "ssp126"
       
print(f"Downloading data for '{target_variable}' on date {target_date} in scenario {target_scenario}...")

climate_data = task0_data.get_data_by_date(target_variable, target_date, target_scenario)

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(climate_data, origin='lower', cmap='turbo')
ax.set_title(f"CMIP6 ACCESS-CM2 - {target_variable.upper()} ({target_date}) - {target_scenario}")
plt.colorbar(im, ax=ax, label="Variable Units")
plt.show()