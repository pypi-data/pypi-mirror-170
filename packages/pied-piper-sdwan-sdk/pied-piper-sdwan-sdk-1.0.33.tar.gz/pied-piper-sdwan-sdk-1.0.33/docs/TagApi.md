# openapi_client.TagApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_for_conflicts_when_tagging**](TagApi.md#check_for_conflicts_when_tagging) | **POST** /tag/conflictCheck | 
[**check_rules**](TagApi.md#check_rules) | **POST** /tag/checkRules | 
[**create_tag**](TagApi.md#create_tag) | **POST** /tag | 
[**create_tag_rule**](TagApi.md#create_tag_rule) | **POST** /tag/tagRules | 
[**delete_tag**](TagApi.md#delete_tag) | **POST** /tag/remove | 
[**delete_tag_rule**](TagApi.md#delete_tag_rule) | **DELETE** /tag/tagRules/{tagRuleId} | 
[**edit_tag_rule**](TagApi.md#edit_tag_rule) | **PUT** /tag/tagRules | 
[**get_tag**](TagApi.md#get_tag) | **GET** /tag | 
[**get_tag_rules**](TagApi.md#get_tag_rules) | **GET** /tag/tagRules/{configGroupId} | 
[**reindex_tag**](TagApi.md#reindex_tag) | **GET** /tag/reindex | 


# **check_for_conflicts_when_tagging**
> str check_for_conflicts_when_tagging()



Check for conflicts when tagging

### Example


```python
import time
import openapi_client
from openapi_client.api import tag_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_api.TagApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.check_for_conflicts_when_tagging(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TagApi->check_for_conflicts_when_tagging: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**str**

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

# **check_rules**
> str check_rules()



This API will check if a rule can be created or not

### Example


```python
import time
import openapi_client
from openapi_client.api import tag_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_api.TagApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.check_rules(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TagApi->check_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**str**

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

# **create_tag**
> str create_tag()



Create a tag

### Example


```python
import time
import openapi_client
from openapi_client.api import tag_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_api.TagApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_tag(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TagApi->create_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**str**

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

# **create_tag_rule**
> str create_tag_rule()



Create a tag rule

### Example


```python
import time
import openapi_client
from openapi_client.api import tag_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_api.TagApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_tag_rule(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TagApi->create_tag_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**str**

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

# **delete_tag**
> delete_tag()



Deletes multiple tags

### Example


```python
import time
import openapi_client
from openapi_client.api import tag_api
from openapi_client.model.get_o365_preferred_path_from_v_analytics_request import GetO365PreferredPathFromVAnalyticsRequest
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_api.TagApi(api_client)
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_tag(get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
    except openapi_client.ApiException as e:
        print("Exception when calling TagApi->delete_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_o365_preferred_path_from_v_analytics_request** | [**GetO365PreferredPathFromVAnalyticsRequest**](GetO365PreferredPathFromVAnalyticsRequest.md)|  | [optional]

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

# **delete_tag_rule**
> delete_tag_rule(tag_rule_id, config_group_id)



Delete a tag rule

### Example


```python
import time
import openapi_client
from openapi_client.api import tag_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_api.TagApi(api_client)
    tag_rule_id = "tagRuleId_example" # str | tagRule Id
    config_group_id = "configGroupId_example" # str | ConfigGroup Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_tag_rule(tag_rule_id, config_group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TagApi->delete_tag_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_tag_rule(tag_rule_id, config_group_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TagApi->delete_tag_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_rule_id** | **str**| tagRule Id |
 **config_group_id** | **str**| ConfigGroup Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **edit_tag_rule**
> edit_tag_rule()



Edit a tag rule

### Example


```python
import time
import openapi_client
from openapi_client.api import tag_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_api.TagApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edit_tag_rule(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TagApi->edit_tag_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **get_tag**
> [TagRestfulResource] get_tag()



Get all tags

### Example


```python
import time
import openapi_client
from openapi_client.api import tag_api
from openapi_client.model.tag_restful_resource import TagRestfulResource
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_api.TagApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_tag()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TagApi->get_tag: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[TagRestfulResource]**](TagRestfulResource.md)

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

# **get_tag_rules**
> get_tag_rules(config_group_id)



Get tag rules

### Example


```python
import time
import openapi_client
from openapi_client.api import tag_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_api.TagApi(api_client)
    config_group_id = "configGroupId_example" # str | ConfigGroup Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_tag_rules(config_group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TagApi->get_tag_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**| ConfigGroup Id |

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

# **reindex_tag**
> reindex_tag()



Re-index device tags for search. Only call this API very occasionally if tag search is not returning expected results.

### Example


```python
import time
import openapi_client
from openapi_client.api import tag_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_api.TagApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.reindex_tag()
    except openapi_client.ApiException as e:
        print("Exception when calling TagApi->reindex_tag: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

