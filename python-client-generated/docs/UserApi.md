# swagger_client.UserApi

All URIs are relative to *https://www.yuque.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_api_v2_hello**](UserApi.md#user_api_v2_hello) | **GET** /api/v2/hello | 心跳
[**user_api_v2_user_info**](UserApi.md#user_api_v2_user_info) | **GET** /api/v2/user | 获取当前 Token 的用户详情

# **user_api_v2_hello**
> InlineResponse200 user_api_v2_hello()

心跳

心跳 GET /api/v2/hello

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # 心跳
    api_response = api_instance.user_api_v2_hello()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_api_v2_hello: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_api_v2_user_info**
> InlineResponse2001 user_api_v2_user_info()

获取当前 Token 的用户详情

获取当前 Token 的用户详情 GET /api/v2/user  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # 获取当前 Token 的用户详情
    api_response = api_instance.user_api_v2_user_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_api_v2_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

