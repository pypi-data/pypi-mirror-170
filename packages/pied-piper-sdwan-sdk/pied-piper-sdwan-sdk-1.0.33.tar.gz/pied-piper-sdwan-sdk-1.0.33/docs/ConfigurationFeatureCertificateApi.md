# openapi_client.ConfigurationFeatureCertificateApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gen_device_csr**](ConfigurationFeatureCertificateApi.md#gen_device_csr) | **PUT** /featurecertificate/devicecsr | 
[**get_device_certificate**](ConfigurationFeatureCertificateApi.md#get_device_certificate) | **GET** /featurecertificate/certificate | 
[**get_device_csr**](ConfigurationFeatureCertificateApi.md#get_device_csr) | **GET** /featurecertificate/devicecsr | 
[**get_feature_ca_state**](ConfigurationFeatureCertificateApi.md#get_feature_ca_state) | **GET** /featurecertificate/syslogconfig | 
[**install_feature_certificate**](ConfigurationFeatureCertificateApi.md#install_feature_certificate) | **PUT** /featurecertificate/certificate | 
[**revoke_feature_certificate**](ConfigurationFeatureCertificateApi.md#revoke_feature_certificate) | **PUT** /featurecertificate/revoke | 


# **gen_device_csr**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} gen_device_csr()



Create CSR for cEdge device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_certificate_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_certificate_api.ConfigurationFeatureCertificateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CSR request for cEdge (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.gen_device_csr(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureCertificateApi->gen_device_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CSR request for cEdge | [optional]

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

# **get_device_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_certificate(device_id)



Get feature cert from cEdge device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_certificate_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_certificate_api.ConfigurationFeatureCertificateApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_certificate(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureCertificateApi->get_device_certificate: %s\n" % e)
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

# **get_device_csr**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_csr(device_id)



Get CSR from cEdge device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_certificate_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_certificate_api.ConfigurationFeatureCertificateApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_csr(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureCertificateApi->get_device_csr: %s\n" % e)
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

# **get_feature_ca_state**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_feature_ca_state()



Get Feature CA state<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_certificate_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_certificate_api.ConfigurationFeatureCertificateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_feature_ca_state()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureCertificateApi->get_feature_ca_state: %s\n" % e)
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

# **install_feature_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} install_feature_certificate()



Upload feature cert for cEdge device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_certificate_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_certificate_api.ConfigurationFeatureCertificateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Install feature cert request for cEdge (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.install_feature_certificate(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureCertificateApi->install_feature_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Install feature cert request for cEdge | [optional]

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

# **revoke_feature_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revoke_feature_certificate()



Revoke feature cert from cEdge device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_certificate_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_certificate_api.ConfigurationFeatureCertificateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Revoking feature cert request for cEdge (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.revoke_feature_certificate(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureCertificateApi->revoke_feature_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Revoking feature cert request for cEdge | [optional]

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

