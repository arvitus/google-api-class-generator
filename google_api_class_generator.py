###############################################################################
#                         Google API Class Generator                          #
#                         Copyright (c) 2023 3D_MAMA                          #
###############################################################################
# ++++++++++++++++  CCCC    OOO    N   N   FFFFF   I    GGGG ++++++++++++++++ #
# ++++++++++++++++ C       O   O   NN  N   F       I   G     ++++++++++++++++ #
# ++++++++++++++++ C       O   O   N N N   FFFF    I   G  GG ++++++++++++++++ #
# ++++++++++++++++ C       O   O   N  NN   F       I   G   G ++++++++++++++++ #
# ++++++++++++++++  CCCC    OOO    N   N   F       I    GGG  ++++++++++++++++ #
###############################################################################
# This script generates a python class that resembles the specified google    #
# api structure. It was mainly created for the sheets and docs api, so there  #
# may be some issues with other apis.                                         #
# The generated class doesn't have any other use than type hinting by default #
# but you can add code to it by using the "method_code" template.             #
# This script will create a file called "<api name>_discovery.py" in the same #
# directory as this script. The generated class inside this file will be      #
# called "<api title>Discovery". The generated class can be used for example  #
# as type hint for the GoogleAPI object of the aiogoogle library.             #
# For this to work your code editor or IDE needs to support type hints!       #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# from sheets_discovery import GoogleSheetsAPIDiscovery as SheetsTypeHints    #
# async with aiogoogle.Aiogoogle(service_account_creds=creds) as aiogoogle:   #
#     sheets: SheetsTypeHints = await aiogoogle.discover("sheets", "v4")      #
#     request = sheets.spreadsheets.values.get(                               #
#         spreadsheetId=<your spreadsheet id>,                                #
#         range=<your range>, # e.g. "A1:F3" or "Sheet1!A:A"                  #
#     )                                                                       #
#     result = await aiogoogle.as_service_account(request)                    #
###############################################################################

# The url to the discovery document of the api
# You can find available apis here: https://developers.google.com/apis-explorer/
discovery_document_url = (
    "https://sheets.googleapis.com/$discovery/rest?version=v4"
)

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

###############################################################################
#     CCCC    OOO    N   N   FFFFF   I    GGGG       EEEEE   N   N   DEEE     #
#    C       O   O   NN  N   F       I   G           E       NN  N   D   D    #
#    C       O   O   N N N   FFFF    I   G  GG       EEEE    N N N   D   D    #
#    C       O   O   N  NN   F       I   G   G       E       N  NN   D   D    #
#     CCCC    OOO    N   N   F       I    GGG        EEEEE   N   N   DEEE     #
###############################################################################


import json
import os
import re
import sys
from typing import Any
from urllib.request import urlopen

try:
    import black
except ImportError:
    raise ImportError(
        "Black could not be found but it must be installed to run this"
        " script.\nPlease install black with `pip install black`."
    )

assert sys.version_info >= (
    3,
    9,
), "Python 3.9 or higher is required to run this script"


def multiple_replacer(replace_dict: dict):
    replacement_function = lambda match: replace_dict[match.group(0)]
    pattern = re.compile(
        "|".join([re.escape(k) for k, v in replace_dict.items()]), re.M
    )
    return lambda string: pattern.sub(replacement_function, string)


def multiple_replace(string, replace_dict) -> str:
    return multiple_replacer(replace_dict)(string)


def indent(string: str) -> str:
    return string.replace("\n", "\n\t")


def get_discovery_document(url: str) -> dict[str, str | Any]:
    with urlopen(url) as response:
        body = response.read()
    discovery = json.loads(body)
    if not discovery["title"]:
        raise ValueError(
            "Invalid response. (Probably an error)\nCheck the URL and try"
            " again.\nFor a list of available APIs, see"
            " https://developers.google.com/apis-explorer\nTo find the"
            " discovery document URL, go to the API's documentation page and"
            " look for the 'Discovery document' link."
        )
    return discovery


def get_type(parameter: dict[str], ignore_optional: bool = True) -> str:
    if parameter.get("enum"):
        type = 'Literal["' + '", "'.join(parameter["enum"]) + '"]'
    else:
        type = multiple_replace(
            parameter["type"],
            {
                "string": "str",
                "integer": "int",
                "boolean": "bool",
                "number": "float",
                "float": "float",
                "object": "dict",
                "array": "list",
                "null": "None",
            },
        )
    if parameter.get("repeated"):
        type = f"list[{type}]"
    if not ignore_optional and not parameter.get("required"):
        type = f"Optional[{type}]"
    return type


def get_parameters(method: dict) -> list[dict]:
    parameters = method.get("parameters", {})
    new_parameters = []
    for param_name in method.get("parameterOrder", {}):
        try:
            new_parameters.append(
                parameters.pop(param_name) | {"name": param_name}
            )
        except KeyError:
            raise KeyError(
                f"Required parameter '{param_name}' not found in parameter"
                " definition."
            )
    if method.get("request"):
        new_parameters.append(
            {
                "name": "body",
                "type": "dict",
                "required": True,
                "description": (
                    "The request body containing more data. A detailed"
                    " description of its structure and possible values can"
                    " be found in the [official"
                    f" documentation]({build_method_docs_url(method)}#request-body)."
                ),
            }
        )
    for param_name in parameters:
        new_parameters.append(parameters[param_name] | {"name": param_name})
    return new_parameters


def build_parameter(parameter: dict[str], kwarg_default: Any = None) -> str:
    type = get_type(parameter)
    if parameter.get("required"):
        return f"{parameter['name']}: {type}"
    else:
        return f"{parameter['name']}: {type} = {kwarg_default}"


def build_argument_string(
    parameter: dict[str],
    global_placeholders: dict[str, str | Any],
    kwarg_default: Any = None,
) -> str:
    type = get_type(parameter, ignore_optional=False)
    if parameter.get("required"):
        return templates["arg"].format(
            **global_placeholders,
            name=parameter["name"],
            type=type,
            description=parameter["description"],
        )
    else:
        return templates["kwarg"].format(
            **global_placeholders,
            name=parameter["name"],
            type=type,
            description=parameter["description"],
            default=kwarg_default,
        )


def build_method_docs_url(method: dict[str, str]) -> str:
    path_parts = method["id"].split(".")
    path = f'{".".join(path_parts[1:-1])}/{method["name"]}'

    api_name = path_parts[0]
    api_version = method["path"].split("/")[0]
    url_base = f"https://developers.google.com/{api_name}/reference/rest/{api_version}/"

    url = url_base + path
    return url


def build_method(method: dict[str], is_function: bool = False) -> str:
    parameters = get_parameters(method)
    method_placeholders = {
        "method_name": method["name"],
        "method_description": method["description"],
        "method_docs": build_method_docs_url(method),
        "method_http_method": method["httpMethod"],
        "method_id": method["id"],
        "method_path": method["path"],
    }
    global_placeholders = api_placeholders | method_placeholders
    kwarg_default = None
    method_string = (
        f'def {method["name"]}('
        + ("self, " if not is_function else "")
        + ", ".join(
            [
                build_parameter(parameter, kwarg_default)
                for parameter in parameters
            ]
        )
        + "):\n\t\t"
        + templates["docstring"]
        .strip()
        .format(
            **global_placeholders,
            arguments="\n".join(
                [
                    build_argument_string(
                        parameter, global_placeholders, kwarg_default
                    )
                    for parameter in parameters
                ]
            ),
            scopes="\n".join(
                [
                    templates["scope"].format(
                        **global_placeholders, scope_url=scope
                    )
                    for scope in method.get("scopes", [])
                ]
            ),
        )
        + "\n\t\t"
        + "\n\t\t".join(
            templates["method_code"]
            .format(
                **global_placeholders,
                defaults={
                    param["name"]: kwarg_default
                    for param in parameters
                    if not param.get("required")
                },
                arguments="{"
                + ", ".join(
                    [
                        f'"{param["name"]}": {param["name"]}'
                        for param in parameters
                    ]
                )
                + "}",
            )
            .strip()
            .split("\n")
        )
    )
    return method_string


def build_init(resource: dict) -> str:
    resource_names: list[str] = resource.get("resources", {}).keys()
    init_string = f"def __init__(self) -> None:\n\t\t" + (
        "\n\t\t".join(
            [
                f"self.{resource_name} = self._{resource_name.capitalize()}()"
                for resource_name in resource_names
            ]
        )
        or "pass"
    )
    return init_string


def build_resource(resource: dict[str, str | Any]) -> str:
    methods = resource.get("methods", {})
    methods = {k: v | {"name": k} for k, v in methods.items()}
    resources = resource.get("resources", {})
    resources = {k: v | {"name": k} for k, v in resources.items()}

    resource_string = (
        f'class _{resource["name"].capitalize()}:\n\t'
        + f"{build_init(resource)}\n\t"
        + indent(
            "\n".join(
                [
                    build_resource(nested_resource)
                    for nested_resource in resources.values()
                ]
            )
        )
        + "\n\t"
        + "\n\t".join([build_method(method) for method in methods.values()])
    )
    return resource_string


def build_class(discovery: dict[str, str | Any]) -> str:
    resources = {k: v | {"name": k} for k, v in discovery["resources"].items()}
    class_name = re.sub(r"[^a-zA-Z_][^a-zA-Z0-9_]*", "", discovery["title"])

    class_string = (
        f"class {class_name}Discovery:\n\t"
        + f"{build_init(discovery)}\n\t\tself.url ="
        f' "{discovery["baseUrl"]}$discovery/{discovery["protocol"]}?version={discovery["version"]}"\n\t'
        + indent(
            "\n".join(
                [
                    build_resource(nested_resource)
                    for nested_resource in resources.values()
                ]
            )
        )
    )
    return class_string


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    templates = {
        "arg": arg.strip(),
        "kwarg": kwarg.strip(),
        "scope": scope.strip(),
        "docstring": f'"""{docstring.strip()}\n\t\t"""',
        "method_code": method_code,
    }

    necessary_imports = ["from typing import Literal"]
    imports_string = "\n".join(necessary_imports) + "\n"

    discovery = get_discovery_document(discovery_document_url)
    api_placeholders = {
        "api_name": discovery["name"],
        "api_version": discovery["version"],
        "api_title": discovery["title"],
        "api_description": discovery["description"],
        "api_docs": discovery["documentationLink"],
    }
    api_class_string = build_class(discovery)

    output_file = f'{discovery["name"]}_discovery.py'
    output_string = imports_string + api_class_string
    # replace each tab (\t) with 4 spaces
    output_string = output_string.expandtabs(4)

    # format with black to clean up the mess
    try:
        output_string = black.format_str(
            output_string,
            mode=black.FileMode(
                line_length=80,
                string_normalization=True,
                preview=True,
            ),
        )
    except:
        # if black fails, write the raw output for debugging
        output_file = f"raw_{output_file}"

    with open(output_file, "w") as f:
        f.write(output_string)

    if output_file.startswith("raw_"):
        print(
            "black failed to format the output, please check the config and"
            " try again\nYou can find the unformatted output in the file"
            f" '{output_file}'"
        )
    else:
        class_name = re.sub(r"[^a-zA-Z_][^a-zA-Z0-9_]*", "", discovery["title"])
        print(
            f"Successfully created the class '{class_name}Discovery' in"
            f" '{output_file}'.\nFor usage help, see the config at the top of"
            " this script."
        )
        if os.path.exists(f"raw_{output_file}"):
            os.remove(f"raw_{output_file}")
