# %%
import papermill as pm

# %%
# Sample Population
nb_sample_population = pm.execute_notebook(
   'sample_population.ipynb',
   r'notebook-output\sample_population_output.ipynb',
   kernel_name='python',
   log_out=True
)

# %%
# Mann Whitney Test
nb_mann_whitnet_test = pm.execute_notebook(
   'mann_whitnet_test.ipynb',
   r'notebook-output\mann_whitnet_test_output.ipynb',
   kernel_name='python',
   log_out=True
)

# %%
# Preprocessing Regression
nb_preprocess_regression = pm.execute_notebook(
   'preprocess_regression.ipynb',
   r'notebook-output\preprocess_regression_output.ipynb',
   kernel_name='python',
   log_out=True
)

# %%
# Parametric Regression
nb_paraetric_regression = pm.execute_notebook(
   'parametric_regression.ipynb',
   r'notebook-output\parametric_regression_output.ipynb',
   kernel_name='python',
   log_out=True
)

# %%
# No Parametric Regression
# nb_no_paraetric_regression = pm.execute_notebook(
#    'no_parametric_regression.ipynb',
#    r'notebook-output\no_parametric_regression_output.ipynb',
#    kernel_name='python',
#    log_out=True
# )


