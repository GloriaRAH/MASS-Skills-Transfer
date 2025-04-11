# import numpy as np
# import pandas as pd
# import json

# # Set random seed for reproducibility
# np.random.seed(0)

# # Generate mock data
# n_points = 10000

# # Double Gaussian distribution
# x1 = np.random.normal(loc=0, scale=10, size=n_points//2)
# y1 = np.random.normal(loc=0, scale=10, size=n_points//2)
# x2 = np.random.normal(loc=20, scale=10, size=n_points//2)
# y2 = np.random.normal(loc=25, scale=10, size=n_points//2)

# x = np.concatenate([x1, x2])
# y = np.concatenate([y1, y2])

# # Categorical variable: galaxy type
# galaxy_types = np.random.choice(['Spiral', 'Elliptical', 'Irregular'], size=n_points)

# # Boolean variable: active galactic nucleus (AGN) presence
# agn_presence = np.random.choice(["True", "False"], size=n_points)

# # Create DataFrame
# data_dict = {
#     'x': list(x),
#     'y': list(y),
#     'galaxy_type': list(galaxy_types),
#     'has_agn': list(agn_presence)
# }
# data = pd.DataFrame(
#     data_dict,
#     columns=['x', 'y', 'galaxy_type', 'has_agn']
# )

# # Save to CSV
# data.to_csv('galaxy_data.csv', index=False)

# # Save data_dict to JSON
# with open('galaxy_data.json', 'w') as f:
#     json.dump(data_dict, f)

# print('Data saved to galaxy_data.csv and galaxy_data.json')




import numpy as np
import pandas as pd
import json

# Set random seed for reproducibility
np.random.seed(0)

# Generate mock data
n_points = 10000

# Double Gaussian distribution
x1 = np.random.normal(loc=0, scale=1, size=n_points//2)
y1 = np.random.normal(loc=0, scale=1, size=n_points//2)
x2 = np.random.normal(loc=5, scale=1.5, size=n_points//2)
y2 = np.random.normal(loc=5, scale=1.5, size=n_points//2)

x = np.concatenate([x1, x2])
y = np.concatenate([y1, y2])

# Determine if points are in the densest region
dense_region_mask = (np.abs(x) < 1) & (np.abs(y) < 1)

# Categorical variable: galaxy type
galaxy_types = np.where(dense_region_mask, 
                        np.random.choice(['Elliptical', 'Elliptical', 'Spiral', 'Irregular'], size=n_points),
                        np.random.choice(['Spiral', 'Elliptical', 'Irregular'], size=n_points))

# Boolean variable: active galactic nucleus (AGN) presence
agn_presence = np.random.choice(['True', 'False'], size=n_points)

# Mapping galaxy types to colors
color_mapping = {
    'Elliptical': 'red',
    'Spiral': 'blue',
    'Irregular': 'grey'
}
colors = [color_mapping[galaxy_type] for galaxy_type in galaxy_types]

# Mass variable: more massive in dense region
masses = np.where(dense_region_mask, np.random.normal(loc=11, scale=2, size=n_points), np.random.normal(loc=9, scale=2, size=n_points))

# Create DataFrame
data_dict = {
    'x': list(x),
    'y': list(y),
    'galaxy_type': list(galaxy_types),
    'color': list(colors),
    'has_agn': list(agn_presence),
    'log10_mass': list(masses)

}
data = pd.DataFrame(
    data_dict,
    columns=['x', 'y', 'galaxy_type', 'color', 'has_agn', 'log10_mass']
)

# Save to CSV
data.to_csv('galaxy_data.csv', index=False)

# Save to JSON
with open('galaxy_data.json', 'w') as f:
    json.dump(data_dict, f)

print('Data saved to galaxy_data.csv and galaxy_data.json')

