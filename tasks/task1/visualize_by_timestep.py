import matplotlib.pyplot as plt
import task1_data

target_variable = "u" 
target_timestep = 10268
target_face = 5
target_z = [0, 2]  

print(f"Downloading data for '{target_variable}' at timestep {target_timestep}...")

climate_data = task1_data.get_data_by_timestep(target_variable, target_face, target_timestep, target_z)
real_date = task1_data.get_date_by_timestep(target_timestep)


fig, axes = plt.subplots(1, 1, figsize=(10, 8))

im = axes.imshow(climate_data[0, :, :], aspect='auto', origin='lower', cmap='viridis')
cbar = plt.colorbar(im, ax=axes)
cbar.set_label('East-west wind speed (m/s)')

axes.set_title(
    f"DYAMOND GEOS - {target_variable.upper()} "
    f"(Timestep: {target_timestep} | Date: {real_date})"
)

plt.show()
