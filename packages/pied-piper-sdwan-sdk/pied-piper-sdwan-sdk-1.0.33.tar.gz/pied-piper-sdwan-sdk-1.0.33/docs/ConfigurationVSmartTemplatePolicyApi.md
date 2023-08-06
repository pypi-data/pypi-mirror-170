# openapi_client.ConfigurationVSmartTemplatePolicyApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_policy**](ConfigurationVSmartTemplatePolicyApi.md#activate_policy) | **POST** /template/policy/vsmart/activate/{policyId} | 
[**activate_policy_for_cloud_services**](ConfigurationVSmartTemplatePolicyApi.md#activate_policy_for_cloud_services) | **POST** /template/policy/vsmart/activate/central/{policyId} | 
[**check_v_smart_connectivity_status**](ConfigurationVSmartTemplatePolicyApi.md#check_v_smart_connectivity_status) | **GET** /template/policy/vsmart/connectivity/status | 
[**create_v_smart_template**](ConfigurationVSmartTemplatePolicyApi.md#create_v_smart_template) | **POST** /template/policy/vsmart | 
[**de_activate_policy**](ConfigurationVSmartTemplatePolicyApi.md#de_activate_policy) | **POST** /template/policy/vsmart/deactivate/{policyId} | 
[**delete_v_smart_template**](ConfigurationVSmartTemplatePolicyApi.md#delete_v_smart_template) | **DELETE** /template/policy/vsmart/{policyId} | 
[**edit_template_without_lock_checks**](ConfigurationVSmartTemplatePolicyApi.md#edit_template_without_lock_checks) | **PUT** /template/policy/vsmart/central/{policyId} | 
[**edit_v_smart_template**](ConfigurationVSmartTemplatePolicyApi.md#edit_v_smart_template) | **PUT** /template/policy/vsmart/{policyId} | 
[**generate_v_smart_policy_template_list**](ConfigurationVSmartTemplatePolicyApi.md#generate_v_smart_policy_template_list) | **GET** /template/policy/vsmart | 
[**get_template_by_policy_id**](ConfigurationVSmartTemplatePolicyApi.md#get_template_by_policy_id) | **GET** /template/policy/vsmart/definition/{policyId} | 
[**qosmos_nbar_migration_warning**](ConfigurationVSmartTemplatePolicyApi.md#qosmos_nbar_migration_warning) | **GET** /template/policy/vsmart/qosmos_nbar_migration_warning | 


# **activate_policy**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} activate_policy(policy_id)



Activate vsmart policy for a given policy id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_smart_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_smart_template_policy_api.ConfigurationVSmartTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template policy (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.activate_policy(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->activate_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.activate_policy(policy_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->activate_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Template policy | [optional]

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

# **activate_policy_for_cloud_services**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} activate_policy_for_cloud_services(policy_id)



Activate vsmart policy for a given policy id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_smart_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_smart_template_policy_api.ConfigurationVSmartTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template policy (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.activate_policy_for_cloud_services(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->activate_policy_for_cloud_services: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.activate_policy_for_cloud_services(policy_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->activate_policy_for_cloud_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Template policy | [optional]

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

# **check_v_smart_connectivity_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} check_v_smart_connectivity_status()



Check VSmart Connectivity Status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_smart_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_smart_template_policy_api.ConfigurationVSmartTemplatePolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.check_v_smart_connectivity_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->check_v_smart_connectivity_status: %s\n" % e)
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

# **create_v_smart_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_v_smart_template()



Create template for given policy

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_smart_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_smart_template_policy_api.ConfigurationVSmartTemplatePolicyApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template policy (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_v_smart_template(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->create_v_smart_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Template policy | [optional]

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

# **de_activate_policy**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} de_activate_policy(policy_id)



Deactivate vsmart policy for a given policy id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_smart_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_smart_template_policy_api.ConfigurationVSmartTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.de_activate_policy(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->de_activate_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |

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

# **delete_v_smart_template**
> delete_v_smart_template(policy_id)



Delete template for a given policy id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_smart_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_smart_template_policy_api.ConfigurationVSmartTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_v_smart_template(policy_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->delete_v_smart_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_template_without_lock_checks**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] edit_template_without_lock_checks(policy_id)



Edit template for given policy id to allow for multiple component edits

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_smart_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_smart_template_policy_api.ConfigurationVSmartTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template policy (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_template_without_lock_checks(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->edit_template_without_lock_checks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_template_without_lock_checks(policy_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->edit_template_without_lock_checks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Template policy | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **edit_v_smart_template**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] edit_v_smart_template(policy_id)



Edit template for given policy id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_smart_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_smart_template_policy_api.ConfigurationVSmartTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template policy (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_v_smart_template(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->edit_v_smart_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_v_smart_template(policy_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->edit_v_smart_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Template policy | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **generate_v_smart_policy_template_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_v_smart_policy_template_list()



Get all template vsmart policy list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_smart_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_smart_template_policy_api.ConfigurationVSmartTemplatePolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.generate_v_smart_policy_template_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->generate_v_smart_policy_template_list: %s\n" % e)
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

# **get_template_by_policy_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_template_by_policy_id(policy_id)



Get template policy definition by policy id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_smart_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_smart_template_policy_api.ConfigurationVSmartTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_template_by_policy_id(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->get_template_by_policy_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |

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

# **qosmos_nbar_migration_warning**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} qosmos_nbar_migration_warning()



Qosmos Nbar migration

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_smart_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_smart_template_policy_api.ConfigurationVSmartTemplatePolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.qosmos_nbar_migration_warning()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVSmartTemplatePolicyApi->qosmos_nbar_migration_warning: %s\n" % e)
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

