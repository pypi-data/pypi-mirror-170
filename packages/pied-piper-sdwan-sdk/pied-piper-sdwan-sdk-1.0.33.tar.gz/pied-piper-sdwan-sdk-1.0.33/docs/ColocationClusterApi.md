# openapi_client.ColocationClusterApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acitvate_cloud_dock_cluster**](ColocationClusterApi.md#acitvate_cloud_dock_cluster) | **POST** /colocation/cluster/activate | 
[**cloud_dock_cluster_preview**](ColocationClusterApi.md#cloud_dock_cluster_preview) | **GET** /colocation/cluster/config | 
[**create_cloud_dock_cluster**](ColocationClusterApi.md#create_cloud_dock_cluster) | **POST** /colocation/cluster | 
[**de_acitvate_cloud_dock_cluster**](ColocationClusterApi.md#de_acitvate_cloud_dock_cluster) | **POST** /colocation/cluster/deactivate | 
[**delete_cloud_dock_cluster_by_name**](ColocationClusterApi.md#delete_cloud_dock_cluster_by_name) | **DELETE** /colocation/cluster/{clustername} | 
[**dummyccm**](ColocationClusterApi.md#dummyccm) | **GET** /colocation/cluster/activateClusterDummy | 
[**dummycsp_state**](ColocationClusterApi.md#dummycsp_state) | **GET** /colocation/cluster/activateClusterDummyState | 
[**get_cloud_dock_cluster_detail**](ColocationClusterApi.md#get_cloud_dock_cluster_detail) | **GET** /colocation/cluster | 
[**get_cloud_dock_cluster_detail_by_id**](ColocationClusterApi.md#get_cloud_dock_cluster_detail_by_id) | **GET** /colocation/cluster/id | 
[**rma_cloud_dock_csp**](ColocationClusterApi.md#rma_cloud_dock_csp) | **POST** /colocation/cluster/rma | 
[**update_cloud_dock_cluster**](ColocationClusterApi.md#update_cloud_dock_cluster) | **PUT** /colocation/cluster | 
[**update_csp_to_cluster**](ColocationClusterApi.md#update_csp_to_cluster) | **PUT** /colocation/cluster/attached/csp | 


# **acitvate_cloud_dock_cluster**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} acitvate_cloud_dock_cluster(cluster_name)



Activate a cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    cluster_name = "clusterName_example" # str | Cluster name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.acitvate_cloud_dock_cluster(cluster_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->acitvate_cloud_dock_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name |

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

# **cloud_dock_cluster_preview**
> str cloud_dock_cluster_preview(serial_number)



Clouddock cluster preview

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    serial_number = "serialNumber_example" # str | Serial number

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cloud_dock_cluster_preview(serial_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->cloud_dock_cluster_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**| Serial number |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_dock_cluster**
> create_cloud_dock_cluster()



Add a new cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cluster config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_cloud_dock_cluster(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->create_cloud_dock_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cluster config | [optional]

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

# **de_acitvate_cloud_dock_cluster**
> de_acitvate_cloud_dock_cluster(cluster_id)



Deactivate clouddock cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.de_acitvate_cloud_dock_cluster(cluster_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->de_acitvate_cloud_dock_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id |

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

# **delete_cloud_dock_cluster_by_name**
> delete_cloud_dock_cluster_by_name(clustername)



Delete cluster by name

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    clustername = "clustername_example" # str | Cluster name

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_cloud_dock_cluster_by_name(clustername)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->delete_cloud_dock_cluster_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustername** | **str**| Cluster name |

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

# **dummyccm**
> dummyccm(cluster_name)



Activate dummp cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    cluster_name = "clusterName_example" # str | Cluster name

    # example passing only required values which don't have defaults set
    try:
        api_instance.dummyccm(cluster_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->dummyccm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name |

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

# **dummycsp_state**
> dummycsp_state(cluster_name, state)



Activate cluster in a state

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    cluster_name = "clusterName_example" # str | Cluster name
    state = "state_example" # str | Cluster state

    # example passing only required values which don't have defaults set
    try:
        api_instance.dummycsp_state(cluster_name, state)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->dummycsp_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name |
 **state** | **str**| Cluster state |

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

# **get_cloud_dock_cluster_detail**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_dock_cluster_detail(cluster_name)



Get details of all existing Clusters

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    cluster_name = "clusterName_example" # str | Cluster name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_dock_cluster_detail(cluster_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->get_cloud_dock_cluster_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name |

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

# **get_cloud_dock_cluster_detail_by_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_dock_cluster_detail_by_id(cluster_id)



Get cluster by Id

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_dock_cluster_detail_by_id(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->get_cloud_dock_cluster_detail_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id |

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

# **rma_cloud_dock_csp**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} rma_cloud_dock_csp(cluster_name)



RMA operation for CSP device

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    cluster_name = "clusterName_example" # str | Cluster name
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.rma_cloud_dock_csp(cluster_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->rma_cloud_dock_csp: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.rma_cloud_dock_csp(cluster_name, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->rma_cloud_dock_csp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name |
 **body** | **str**|  | [optional]

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

# **update_cloud_dock_cluster**
> update_cloud_dock_cluster()



Update a existing cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cluster config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_cloud_dock_cluster(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->update_cloud_dock_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cluster config | [optional]

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

# **update_csp_to_cluster**
> update_csp_to_cluster()



Update attached csp to cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_cluster_api.ColocationClusterApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CSP config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_csp_to_cluster(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationClusterApi->update_csp_to_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CSP config | [optional]

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

