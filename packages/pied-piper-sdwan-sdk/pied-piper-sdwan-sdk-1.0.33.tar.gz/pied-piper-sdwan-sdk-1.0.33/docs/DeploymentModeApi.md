# openapi_client.DeploymentModeApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_fedramp_mode**](DeploymentModeApi.md#config_fedramp_mode) | **POST** /fedramp/status | 
[**configure_dns_sec**](DeploymentModeApi.md#configure_dns_sec) | **POST** /fedramp/dnssec/config | 
[**configure_wazuh_client**](DeploymentModeApi.md#configure_wazuh_client) | **POST** /fedramp/wazuh/config | 
[**get_dns_sec_status**](DeploymentModeApi.md#get_dns_sec_status) | **GET** /fedramp/dnssec/status | 
[**get_wazuh_agent_status**](DeploymentModeApi.md#get_wazuh_agent_status) | **GET** /fedramp/wazuh/status | 
[**reques_dns_sec_actions**](DeploymentModeApi.md#reques_dns_sec_actions) | **GET** /fedramp/dnssec/actions | 
[**request_wazuh_actions**](DeploymentModeApi.md#request_wazuh_actions) | **GET** /fedramp/wazuh/actions | 


# **config_fedramp_mode**
> config_fedramp_mode()



Set network deployment mode

### Example


```python
import time
import openapi_client
from openapi_client.api import deployment_mode_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deployment_mode_api.DeploymentModeApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Network deployment mode (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.config_fedramp_mode(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling DeploymentModeApi->config_fedramp_mode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Network deployment mode | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_dns_sec**
> configure_dns_sec()



Configure DNS-Sec

### Example


```python
import time
import openapi_client
from openapi_client.api import deployment_mode_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deployment_mode_api.DeploymentModeApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | DNS sec config request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.configure_dns_sec(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling DeploymentModeApi->configure_dns_sec: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| DNS sec config request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_wazuh_client**
> configure_wazuh_client()



Configure Wazuh agent

### Example


```python
import time
import openapi_client
from openapi_client.api import deployment_mode_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deployment_mode_api.DeploymentModeApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Wazhuh configuration (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.configure_wazuh_client(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling DeploymentModeApi->configure_wazuh_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Wazhuh configuration | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_sec_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dns_sec_status()



Get DNS-Sec status

### Example


```python
import time
import openapi_client
from openapi_client.api import deployment_mode_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deployment_mode_api.DeploymentModeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_dns_sec_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeploymentModeApi->get_dns_sec_status: %s\n" % e)
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

# **get_wazuh_agent_status**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_wazuh_agent_status()



Get Wazuh agent status

### Example


```python
import time
import openapi_client
from openapi_client.api import deployment_mode_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deployment_mode_api.DeploymentModeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_wazuh_agent_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeploymentModeApi->get_wazuh_agent_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **reques_dns_sec_actions**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} reques_dns_sec_actions(action)



Request DNS-Sec actions

### Example


```python
import time
import openapi_client
from openapi_client.api import deployment_mode_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deployment_mode_api.DeploymentModeApi(api_client)
    action = "action_example" # str | DNS-Sec action

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.reques_dns_sec_actions(action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeploymentModeApi->reques_dns_sec_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| DNS-Sec action |

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

# **request_wazuh_actions**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] request_wazuh_actions()



Wazuh agent action

### Example


```python
import time
import openapi_client
from openapi_client.api import deployment_mode_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deployment_mode_api.DeploymentModeApi(api_client)
    action = "action_example" # str | Wazhuh Action (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.request_wazuh_actions(action=action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeploymentModeApi->request_wazuh_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Wazhuh Action | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

