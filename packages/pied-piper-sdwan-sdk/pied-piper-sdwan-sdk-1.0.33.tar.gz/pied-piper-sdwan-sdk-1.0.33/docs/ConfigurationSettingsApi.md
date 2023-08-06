# openapi_client.ConfigurationSettingsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_analytics_data_file**](ConfigurationSettingsApi.md#create_analytics_data_file) | **POST** /settings/configuration/analytics/dca | 
[**edit_cert_configuration**](ConfigurationSettingsApi.md#edit_cert_configuration) | **PUT** /settings/configuration/certificate/{settingType} | 
[**edit_configuration**](ConfigurationSettingsApi.md#edit_configuration) | **PUT** /settings/configuration/{settingType} | 
[**get_banner**](ConfigurationSettingsApi.md#get_banner) | **GET** /settings/banner | 
[**get_cert_configuration**](ConfigurationSettingsApi.md#get_cert_configuration) | **GET** /settings/configuration/certificate/{settingType} | 
[**get_configuration_by_setting_type**](ConfigurationSettingsApi.md#get_configuration_by_setting_type) | **GET** /settings/configuration/{settingType} | 
[**get_google_map_key**](ConfigurationSettingsApi.md#get_google_map_key) | **GET** /settings/configuration/googleMapKey | 
[**get_maintenance_window**](ConfigurationSettingsApi.md#get_maintenance_window) | **GET** /settings/configuration/maintenanceWindow | 
[**get_session_timout**](ConfigurationSettingsApi.md#get_session_timout) | **GET** /settings/clientSessionTimeout | 
[**new_cert_configuration**](ConfigurationSettingsApi.md#new_cert_configuration) | **POST** /settings/configuration/certificate/{settingType} | 
[**new_configuration**](ConfigurationSettingsApi.md#new_configuration) | **POST** /settings/configuration/{settingType} | 


# **create_analytics_data_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_analytics_data_file()



Create analytics data file

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_settings_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_settings_api.ConfigurationSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.create_analytics_data_file()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->create_analytics_data_file: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_cert_configuration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_cert_configuration(setting_type)



Update certificate configuration

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_settings_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_settings_api.ConfigurationSettingsApi(api_client)
    setting_type = "settingType_example" # str | Setting type
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Certificate config (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_cert_configuration(setting_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->edit_cert_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_cert_configuration(setting_type, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->edit_cert_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_type** | **str**| Setting type |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Certificate config | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_configuration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_configuration(setting_type)



Update configuration setting

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_settings_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_settings_api.ConfigurationSettingsApi(api_client)
    setting_type = "settingType_example" # str | Setting type
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Configuration setting (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_configuration(setting_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->edit_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_configuration(setting_type, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->edit_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_type** | **str**| Setting type |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Configuration setting | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_banner**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_banner()



Retrieve banner

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_settings_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_settings_api.ConfigurationSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_banner()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->get_banner: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cert_configuration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cert_configuration(setting_type)



Retrieve certificate configuration value by settingType

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_settings_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_settings_api.ConfigurationSettingsApi(api_client)
    setting_type = "settingType_example" # str | Setting type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cert_configuration(setting_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->get_cert_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_type** | **str**| Setting type |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_by_setting_type**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_configuration_by_setting_type(setting_type)



Retrieve configuration value by settingType

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_settings_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_settings_api.ConfigurationSettingsApi(api_client)
    setting_type = "settingType_example" # str | Setting type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_configuration_by_setting_type(setting_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->get_configuration_by_setting_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_type** | **str**| Setting type |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_google_map_key**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_google_map_key()



Retrieve Google map key

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_settings_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_settings_api.ConfigurationSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_google_map_key()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->get_google_map_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_window**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_maintenance_window()



Retrieve maintenance window

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_settings_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_settings_api.ConfigurationSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_maintenance_window()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->get_maintenance_window: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_timout**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_session_timout()



Get client session timeout

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_settings_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_settings_api.ConfigurationSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_session_timout()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->get_session_timout: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_cert_configuration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} new_cert_configuration(setting_type)



Add new certificate configuration

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_settings_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_settings_api.ConfigurationSettingsApi(api_client)
    setting_type = "settingType_example" # str | Setting type
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Certificate config (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.new_cert_configuration(setting_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->new_cert_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.new_cert_configuration(setting_type, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->new_cert_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_type** | **str**| Setting type |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Certificate config | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_configuration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} new_configuration(setting_type)



Add new configuration

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_settings_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_settings_api.ConfigurationSettingsApi(api_client)
    setting_type = "settingType_example" # str | Setting type
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Configuration setting (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.new_configuration(setting_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->new_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.new_configuration(setting_type, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSettingsApi->new_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_type** | **str**| Setting type |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Configuration setting | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

