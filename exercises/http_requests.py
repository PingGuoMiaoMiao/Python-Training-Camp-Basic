import requests

def get_website_content(url):
    """
    发送GET请求获取网页内容
    
    参数:
    - url: 目标网站URL
    
    返回:
    - 包含响应信息的字典: 
      {
        'status_code': HTTP状态码,
        'content': 响应内容文本,
        'headers': 响应头部信息
      }
    """
    try:
        response = requests.get(url)
        return {
            'status_code': response.status_code,
            'content': response.text,
            'headers': response.headers
        }
    except requests.RequestException as e:
        return {'status_code': None, 'content': str(e), 'headers': None}

def post_data(url, data):
    """
    发送POST请求提交数据
    
    参数:
    - url: 目标网站URL
    - data: 要提交的数据字典
    
    返回:
    - 包含响应信息的字典:
      {
        'status_code': HTTP状态码,
        'response_json': 响应的JSON数据(如果有),
        'success': 请求是否成功(状态码为2xx)
      }
    """
    try:
        response = requests.post(url, json=data)
        return {
            'status_code': response.status_code,
            'response_json': response.json() if response.headers.get('Content-Type') == 'application/json' else None,
            'success': response.ok
        }
    except requests.RequestException as e:
        return {'status_code': None, 'response_json': None, 'success': False}