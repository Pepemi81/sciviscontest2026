import matplotlib.pyplot as plt
import task0_data

target_variable = "pr" 
target_timestep = 12000

print(f"Downloading data for '{target_variable}' at timestep {target_timestep}...")

climate_data = task0_data.get_data_by_timestep(target_variable, target_timestep)
real_date = task0_data.get_date_by_timestep(target_timestep)

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(climate_data, origin='lower', cmap='turbo')

ax.set_title(f"CMIP6 ACCESS-CM2 - {target_variable.upper()} (Timestep: {target_timestep} | Date: {real_date})")
plt.colorbar(im, ax=ax, label="Variable Units")
plt.show()