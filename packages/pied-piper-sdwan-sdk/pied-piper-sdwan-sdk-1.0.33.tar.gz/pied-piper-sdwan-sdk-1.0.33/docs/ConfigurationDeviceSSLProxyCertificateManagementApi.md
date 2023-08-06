# openapi_client.ConfigurationDeviceSSLProxyCertificateManagementApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_wan_edge**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#add_wan_edge) | **POST** /sslproxy/certificate/wanedge/{deviceId} | 
[**generate_ssl_proxy_csr**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#generate_ssl_proxy_csr) | **POST** /sslproxy/generate/csr/sslproxy | 
[**generate_ssl_proxy_csr_0**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#generate_ssl_proxy_csr_0) | **POST** /sslproxy/generate/vmanage/csr | 
[**get_all_device_certificates**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#get_all_device_certificates) | **POST** /sslproxy/devicecertificates | 
[**get_all_device_csr**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#get_all_device_csr) | **POST** /sslproxy/devicecsr | 
[**get_certificate_state**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#get_certificate_state) | **GET** /sslproxy/settings/certificate | 
[**get_enterprise_certificate**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#get_enterprise_certificate) | **GET** /sslproxy/settings/enterprise/certificate | 
[**get_proxy_cert_of_edge**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#get_proxy_cert_of_edge) | **GET** /sslproxy/certificate | 
[**get_self_signed_cert**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#get_self_signed_cert) | **GET** /certificate/vmanage/selfsignedcert | 
[**get_ssl_proxy_csr**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#get_ssl_proxy_csr) | **GET** /sslproxy/csr | 
[**get_ssl_proxy_list**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#get_ssl_proxy_list) | **GET** /sslproxy/list | 
[**get_v_manage_enterprise_root_certificate**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#get_v_manage_enterprise_root_certificate) | **GET** /sslproxy/settings/enterprise/rootca | 
[**getv_manage_certificate**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#getv_manage_certificate) | **GET** /sslproxy/settings/vmanage/certificate | 
[**getv_manage_csr**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#getv_manage_csr) | **GET** /sslproxy/settings/vmanage/csr | 
[**getv_manage_root_ca**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#getv_manage_root_ca) | **GET** /sslproxy/settings/vmanage/rootca | 
[**renew_certificate**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#renew_certificate) | **POST** /sslproxy/renew | 
[**revoke_certificate**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#revoke_certificate) | **POST** /sslproxy/revoke | 
[**revoke_renew_certificate**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#revoke_renew_certificate) | **POST** /sslproxy/revokerenew | 
[**set_enterprise_cert**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#set_enterprise_cert) | **POST** /sslproxy/settings/enterprise/certificate | 
[**set_enterprise_root_ca_cert**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#set_enterprise_root_ca_cert) | **POST** /sslproxy/settings/enterprise/rootca | 
[**setv_manage_root_ca**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#setv_manage_root_ca) | **POST** /sslproxy/settings/vmanage/rootca | 
[**setv_manageintermediate_cert**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#setv_manageintermediate_cert) | **POST** /sslproxy/settings/vmanage/certificate | 
[**update_certificate**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#update_certificate) | **PUT** /sslproxy/certificate | 
[**upload_certificiates**](ConfigurationDeviceSSLProxyCertificateManagementApi.md#upload_certificiates) | **POST** /sslproxy/certificates | 


# **add_wan_edge**
> add_wan_edge(device_id)



Add SSL proxy wan edge

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cert state (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.add_wan_edge(device_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->add_wan_edge: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.add_wan_edge(device_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->add_wan_edge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cert state | [optional]

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

# **generate_ssl_proxy_csr**
> generate_ssl_proxy_csr()



CSR request SSL proxy for edge

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CSR request for edge (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.generate_ssl_proxy_csr(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->generate_ssl_proxy_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CSR request for edge | [optional]

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

# **generate_ssl_proxy_csr_0**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_ssl_proxy_csr_0()



Generate CSR

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CSR request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_ssl_proxy_csr_0(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->generate_ssl_proxy_csr_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CSR request | [optional]

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

# **get_all_device_certificates**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_all_device_certificates()



Get certificate for all cEdges

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device list (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_device_certificates(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->get_all_device_certificates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device list | [optional]

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

# **get_all_device_csr**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_all_device_csr()



Get CSR for all cEdges

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device list (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_device_csr(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->get_all_device_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device list | [optional]

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

# **get_certificate_state**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_certificate_state()



Get certificate state

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_certificate_state()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->get_certificate_state: %s\n" % e)
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

# **get_enterprise_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_enterprise_certificate()



Get enterprise certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_enterprise_certificate()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->get_enterprise_certificate: %s\n" % e)
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

# **get_proxy_cert_of_edge**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_proxy_cert_of_edge(device_id)



Get edge proxy certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_proxy_cert_of_edge(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->get_proxy_cert_of_edge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

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

# **get_self_signed_cert**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_self_signed_cert()



get self signed certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_signed_cert()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->get_self_signed_cert: %s\n" % e)
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

# **get_ssl_proxy_csr**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ssl_proxy_csr(device_id)



Get SSL proxy CSR

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    device_id = "8d86d8b2-2239-402e-9fef-467f7bad3f2f" # str | device UUID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ssl_proxy_csr(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->get_ssl_proxy_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| device UUID |

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

# **get_ssl_proxy_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_ssl_proxy_list()



Get SSL proxy certificate list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_ssl_proxy_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->get_ssl_proxy_list: %s\n" % e)
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

# **get_v_manage_enterprise_root_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_v_manage_enterprise_root_certificate()



Get vManage enterprise root certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_v_manage_enterprise_root_certificate()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->get_v_manage_enterprise_root_certificate: %s\n" % e)
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

# **getv_manage_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} getv_manage_certificate()



Get vManage intermediate certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.getv_manage_certificate()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->getv_manage_certificate: %s\n" % e)
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

# **getv_manage_csr**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} getv_manage_csr()



Get vManage CSR

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.getv_manage_csr()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->getv_manage_csr: %s\n" % e)
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

# **getv_manage_root_ca**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} getv_manage_root_ca()



Get vManage root certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.getv_manage_root_ca()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->getv_manage_root_ca: %s\n" % e)
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

# **renew_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} renew_certificate()



Renew device certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Renew device certificate request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.renew_certificate(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->renew_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Renew device certificate request | [optional]

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

# **revoke_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revoke_certificate()



Revoke device certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Revoke device certificate request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.revoke_certificate(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->revoke_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Revoke device certificate request | [optional]

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

# **revoke_renew_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revoke_renew_certificate()



Revoke and renew device certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Revoke device certificate request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.revoke_renew_certificate(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->revoke_renew_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Revoke device certificate request | [optional]

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

# **set_enterprise_cert**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} set_enterprise_cert()



Configure enterprise certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Config enterprise certificate request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_enterprise_cert(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->set_enterprise_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Config enterprise certificate request | [optional]

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

# **set_enterprise_root_ca_cert**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} set_enterprise_root_ca_cert()



Set vManage enterprise root certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Set enterprise root CA request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_enterprise_root_ca_cert(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->set_enterprise_root_ca_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Set enterprise root CA request | [optional]

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

# **setv_manage_root_ca**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} setv_manage_root_ca()



Set vManage root certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Set vManage root CA request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.setv_manage_root_ca(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->setv_manage_root_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Set vManage root CA request | [optional]

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

# **setv_manageintermediate_cert**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} setv_manageintermediate_cert()



Set vManage root certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Set vManage intermediate CA request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.setv_manageintermediate_cert(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->setv_manageintermediate_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Set vManage intermediate CA request | [optional]

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

# **update_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_certificate()



Upload device certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Upload device certificate (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_certificate(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->update_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Upload device certificate | [optional]

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

# **upload_certificiates**
> upload_certificiates()



Upload device certificates

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_ssl_proxy_certificate_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_ssl_proxy_certificate_management_api.ConfigurationDeviceSSLProxyCertificateManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.upload_certificiates()
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSSLProxyCertificateManagementApi->upload_certificiates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**207** | Multi-status |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

