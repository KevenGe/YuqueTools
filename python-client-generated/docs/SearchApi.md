# swagger_client.SearchApi

All URIs are relative to *https://www.yuque.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_api_v2_search**](SearchApi.md#search_api_v2_search) | **GET** /api/v2/search | 通用搜索

# **search_api_v2_search**
> InlineResponse2002 search_api_v2_search(q, type, scope=scope, page=page, offset=offset, strict=strict, related=related, creator_id=creator_id, creator=creator)

通用搜索

通用搜索 GET /api/v2/search   - 支持分页, PageSize 固定为 20  

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | 搜索关键词
type = 'type_example' # str | 搜索类型 (doc:文档, repo:知识库)
scope = 'scope_example' # str | 搜索范围, 不填默认为搜索当前用户/团队   [例子] ``` - 假设:   - 团队 URL = https://yuque_domain/group_a   - 知识库 URL = https://yuque_domain/group_a/book_x - 则:   - 搜索团队里的文档: { type: 'doc', scope: 'group_a' }   - 搜索团队里的知识库: { type: 'repo', scope: 'group_a' }   - 搜索知识库里的文档: { type: 'doc', scope: 'group_a/book_x' } ``` (optional)
page = 56 # int | 页码 [分页参数] (optional)
offset = 56 # int | 页码, 非偏移量 [分页参数] (optional)
strict = true # bool | 关键词精确匹配, 不分词 (optional)
related = true # bool | 仅搜索与我相关 [筛选条件] (optional)
creator_id = 56 # int | 仅搜索指定作者 ID [筛选条件] (optional)
creator = 'creator_example' # str | 仅搜索指定作者 login [筛选条件] (optional)

try:
    # 通用搜索
    api_response = api_instance.search_api_v2_search(q, type, scope=scope, page=page, offset=offset, strict=strict, related=related, creator_id=creator_id, creator=creator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_api_v2_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| 搜索关键词 | 
 **type** | **str**| 搜索类型 (doc:文档, repo:知识库) | 
 **scope** | **str**| 搜索范围, 不填默认为搜索当前用户/团队   [例子] &#x60;&#x60;&#x60; - 假设:   - 团队 URL &#x3D; https://yuque_domain/group_a   - 知识库 URL &#x3D; https://yuque_domain/group_a/book_x - 则:   - 搜索团队里的文档: { type: &#x27;doc&#x27;, scope: &#x27;group_a&#x27; }   - 搜索团队里的知识库: { type: &#x27;repo&#x27;, scope: &#x27;group_a&#x27; }   - 搜索知识库里的文档: { type: &#x27;doc&#x27;, scope: &#x27;group_a/book_x&#x27; } &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| 页码 [分页参数] | [optional] 
 **offset** | **int**| 页码, 非偏移量 [分页参数] | [optional] 
 **strict** | **bool**| 关键词精确匹配, 不分词 | [optional] 
 **related** | **bool**| 仅搜索与我相关 [筛选条件] | [optional] 
 **creator_id** | **int**| 仅搜索指定作者 ID [筛选条件] | [optional] 
 **creator** | **str**| 仅搜索指定作者 login [筛选条件] | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

