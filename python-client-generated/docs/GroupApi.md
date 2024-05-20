# swagger_client.GroupApi

All URIs are relative to *https://www.yuque.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_api_v2_group_member_destroy**](GroupApi.md#group_api_v2_group_member_destroy) | **DELETE** /api/v2/groups/{login}/users/{id} | 删除成员
[**group_api_v2_group_member_list**](GroupApi.md#group_api_v2_group_member_list) | **GET** /api/v2/groups/{login}/users | 获取团队的成员
[**group_api_v2_group_member_update**](GroupApi.md#group_api_v2_group_member_update) | **PUT** /api/v2/groups/{login}/users/{id} | 变更成员
[**group_api_v2_user_group_list**](GroupApi.md#group_api_v2_user_group_list) | **GET** /api/v2/users/{id}/groups | 获取用户的团队

# **group_api_v2_group_member_destroy**
> InlineResponse2006 group_api_v2_group_member_destroy(login, id)

删除成员

删除成员 DELETE /api/v2/groups/:login/users/:id

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | 团队 Login or ID
id = 'id_example' # str | 用户 Login or ID

try:
    # 删除成员
    api_response = api_instance.group_api_v2_group_member_destroy(login, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_api_v2_group_member_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| 团队 Login or ID | 
 **id** | **str**| 用户 Login or ID | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_api_v2_group_member_list**
> InlineResponse2004 group_api_v2_group_member_list(login, role=role, offset=offset)

获取团队的成员

获取团队的成员 GET /api/v2/groups/:login/users   - 支持分页, PageSize 固定为 100  

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | 团队 Login or ID
role = 'role_example' # str | 角色 [筛选条件] (0:管理员, 1:成员, 2:只读成员) (optional)
offset = 0 # int | 偏移量 [分页条件] (optional) (default to 0)

try:
    # 获取团队的成员
    api_response = api_instance.group_api_v2_group_member_list(login, role=role, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_api_v2_group_member_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| 团队 Login or ID | 
 **role** | **str**| 角色 [筛选条件] (0:管理员, 1:成员, 2:只读成员) | [optional] 
 **offset** | **int**| 偏移量 [分页条件] | [optional] [default to 0]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_api_v2_group_member_update**
> InlineResponse2005 group_api_v2_group_member_update(login, id, body=body)

变更成员

变更成员 PUT /api/v2/groups/:login/users/:id  

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | 团队 Login or ID
id = 'id_example' # str | 用户 Login or ID
body = NULL # object |  (optional)

try:
    # 变更成员
    api_response = api_instance.group_api_v2_group_member_update(login, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_api_v2_group_member_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| 团队 Login or ID | 
 **id** | **str**| 用户 Login or ID | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_api_v2_user_group_list**
> InlineResponse2003 group_api_v2_user_group_list(id, role=role, offset=offset)

获取用户的团队

获取用户的团队 GET /api/v2/users/:id/groups   - 支持分页, PageSize 固定为 100  

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 用户 login 或 ID
role = 'role_example' # str | 角色 [过滤条件] (0:管理员, 1:成员) (optional)
offset = 0 # int | 偏移量 [分页条件] (optional) (default to 0)

try:
    # 获取用户的团队
    api_response = api_instance.group_api_v2_user_group_list(id, role=role, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_api_v2_user_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 用户 login 或 ID | 
 **role** | **str**| 角色 [过滤条件] (0:管理员, 1:成员) | [optional] 
 **offset** | **int**| 偏移量 [分页条件] | [optional] [default to 0]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

