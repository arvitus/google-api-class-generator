# Google API Class Generator
Generates a python class containing all methods and resources of a google api from its discovery document.


This script generates a python class that resembles the specified google api structure. It was mainly created for the sheets and docs api, so there may be some issues with other apis. The generated class doesn't have any other use than type hinting by default but you can add code to it by using the "method_code" template. This script will create a file called "\<api name>_discovery.py" in the same directory as this script. The generated class inside this file will be called "\<api title>Discovery". The generated class can be used for example as type hint for the `GoogleAPI` object of the [`aiogoogle`](https://github.com/omarryhan/aiogoogle) library. For this to work your code editor or IDE needs to support type hints!

Please open an [issue](https://github.com/arvitus/google-api-class-generator/issues) if you encounter any bugs or errors.

*It's a small script for an even smaller target group.*

## Prerequisites
  - Python 3.9+ (tested on 3.11 but should work with 3.9+)
  - black -> `pip install black`

## Usage
  - download the `google_api_class_generator.py` file and open it
  - change the values in the config section to your linking and save the file
  - run the script (`python3 google_api_class_generator.py`)
  - import the generated class to use it in your code (see [Example](#example))

## Where can I find the discovery document URL?
  1. Go to the [API Explorer](https://developers.google.com/apis-explorer/) and search for your desired api
     ![grafik](https://user-images.githubusercontent.com/34866314/210437655-19b7b878-171e-4da0-b3fa-67e71d09cfe6.png)
  2. Click the name of the API you want to get the discovery document for
  3. Scroll down to the `Discovery document` section where you can find the url to the discovery document
     ![grafik](https://user-images.githubusercontent.com/34866314/210437753-6dad4e8e-0a0d-4eb6-a686-8af8dbd63f54.png)

## Example
  ```py
  from sheets_discovery import GoogleSheetsAPIDiscovery as SheetsTypeHints
  async with aiogoogle.Aiogoogle(service_account_creds=creds) as aiogoogle:
      sheets: SheetsTypeHints = await aiogoogle.discover("sheets", "v4")
      request = sheets.spreadsheets.values.get(
          spreadsheetId="13LCOmhNUulFdRC5802ATeIemQq7e2Uchpno-waxEMYE",
          range="MySheet!A:A",
      )
      result = await aiogoogle.as_service_account(request)
  ```


## Templates
  The class can be customised through the use of templates.
  You can edit the docstring layout of the methods and the code of each method. There are placeholders available for more cusomisation.
  By default the class is only usable for type hinting but with the "method_code" template and some manual changes you could create an api wrapper for example.

  ```py
  ###############################################################################
  # ++++++++++ TTTTT EEEEE MM MM PPPP  L      AAA  TTTTT EEEEE  SSSS ++++++++++ #
  # ++++++++++   T   E     M M M P   P L     A   A   T   E     S     ++++++++++ #
  # ++++++++++   T   EEEE  M   M PPPP  L     AAAAA   T   EEEE   SSS  ++++++++++ #
  # ++++++++++   T   E     M   M P     L     A   A   T   E         S ++++++++++ #
  # ++++++++++   T   EEEEE M   M P     LLLLL A   A   T   EEEEE  SSS  ++++++++++ #
  ###############################################################################
  # The templates are used to generate the code for the methods and their       #
  # docstring. You can use the following global placeholders in every template: #
  # {method_name} - The name of the method (e.g. "get" or "batchUpdate")        #
  # {method_description} - The description of the method.                       #
  # {method_docs} - The url to the official documentation of the method.        #
  #                 May not always be correct.                                  #
  # {method_http_method} - The http method of the method (e.g. "GET" or "POST") #
  # {method_id} - The id of the method (e.g. "sheets.spreadsheets.values.get")  #
  # {method_path} - The path of the method                                      #
  #                 (e.g. "/v4/spreadsheets/{spreadsheetId}/values/{range}")    #
  # {api_title} - The title of the api (e.g. "Google Sheets API")               #
  # {api_description} - The description of the api.                             #
  # {api_docs} - The url to the official documentation of the api.              #
  # {api_name} - The name of the api (e.g. "sheets" or "docs")                  #
  # {api_version} - The version of the api (e.g. "v4")                          #
  ###############################################################################

  # ARGUMENTS
  # They will be replaced with the {arguments} placeholder in the docstring
  # You can use all global and the following placeholders:
  # {name} - The name of the argument (e.g. "spreadsheetId" or "ranges")
  # {type} - The type of the argument (e.g. "str" or "List[str]")
  # {description} - The description of the argument.
  # {default} - The default value of the argument. (Only for keyword arguments)
  arg = "- `{name}: {type}` {description}"
  kwarg = arg + "\n\t- Defaults to: `{default}`"
  
  # SCOPES
  # They will be replaced with the {scopes} placeholder in the docstring
  # You can use all global and the following placeholders:
  # {scope_url} - The scope url (e.g. "https://www.googleapis.com/auth/drive")
  scope = "- {scope_url}"
  
  # DOCSTRING
  # Will be inserted as the docstring of every method
  # You can use all global and the following placeholders:
  # {arguments} - The arguments of the method.
  # {scopes} - The scopes of the method.
  docstring = """
  {method_description}
  
  #### More information about parameter values or the response structure can be found in the [official documentation]({method_docs}).
  
  ### Args
  {arguments}
  
  ### Scopes
  Requires one of the following
  [Oauth scopes](https://developers.google.com/identity/protocols/OAuth2):
  {scopes}
  """
  
  # METHOD CODE
  # Will be inserted as the code of every method
  # You can use valid python code, all global placeholders
  # and the following placeholders:
  # {defaults} - The default values of the keyword arguments as a dictionary.
  #              -> {<kwarg_name>: <default_value>, ..}
  # {arguments} - All arguments of the method and their values as a dictionary.
  #               -> {"<arg_name>": <arg_name>, "<kwarg_name>": <kwarg_name>, ..}
  method_code = """
  pass
  """
  ```

  
## Contributing
  Feel free to contribute anything! There are no rules but I'd appreciate it if you format your code with black.
