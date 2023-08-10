## YAML to Python Translator ##

import yaml
from googletran import Translator


def translate_yaml(input_file, output_file, target_lang):
    ## load the YAML file
    with open(input_file, 'r') as f:
        data = yaml.safe_load(f)

    translator = Translator()

    ## Translate values in the data
def translate(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = translator.translate(value, dest=target_lang).text
            elif isinstance(value, dict) or isinstance(value, list):
                translate(value)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, str):
                data[i] = translator.translate(item, dest=target_lang).text
            elif isinstance(item, dict) or isinstance(item, list):
                translate(item)

translate(data)

## writes to a YAML file
   with open(output_file, 'w') as f:
      yaml.dump(data, f)
if __name__ == "__main__"
   input_file = "input.yaml" ## put your input YAML file
   output_file = "output_yaml" ## put your output YAML file
   target_lang = "fr"  ## Replace with your target code

   translate_yaml(input_file, output_file, target_lang)