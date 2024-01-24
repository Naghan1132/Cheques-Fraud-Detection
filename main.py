# lancer tout avec ce script
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat

def execute_notebook(notebook_path):
    # Charger le notebook
    with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
        notebook_content = nbformat.read(notebook_file, as_version=4)

    # Configurer le preprocesseur pour exécuter le code dans le notebook
    execute_preprocessor = ExecutePreprocessor(timeout=600, kernel_name='python3')

    # Exécuter le code du notebook
    execute_preprocessor.preprocess(notebook_content, {'metadata': {'path': '.'}})

if __name__ == '__main__':
    # Spécifiez le chemin du notebook à exécuter
    notebook_path = 'preprocessing/preprocessing.ipynb'

    # Spécifiez le chemin où vous souhaitez enregistrer le résultat
    #output_path = 'rapport.html'

    # Exécutez les notebooks et enregistrez le résultat
    execute_notebook('preprocessing/preprocessing.ipynb')
    execute_notebook('preprocessing/smote.ipynb')
    execute_notebook('preprocessing/undersampling.ipynb')
    execute_notebook('preprocessing/simple.ipynb')
    execute_notebook('classification/classification.ipynb')




# 1 : preprocess 
# 2 : split train test
# 3 : smote / undersampling 
# 4 : classification