# %%
import papermill as pm

# %%
# Sample Population
nb_sample_population = pm.execute_notebook(
   'sample_population.ipynb',
   'sample_population.ipynb',
   kernel_name='python',
   log_out=True
)

# %%
# Mann Whitney Test
nb_mann_whitnet_test = pm.execute_notebook(
   'mann_whitnet_test.ipynb',
   'mann_whitnet_test.ipynb',
   kernel_name='python',
   log_out=True
)

# %%
# Preprocessing Regression
nb_preprocess_regression = pm.execute_notebook(
   'preprocess_regression.ipynb',
   'preprocess_regression.ipynb',
   kernel_name='python',
   log_out=True
)

# %%
# Regression
nb_regression = pm.execute_notebook(
   'regression.ipynb',
   'regression.ipynb',
   kernel_name='python',
   log_out=True
)
