import requests  # 映入request，用户http接口请求
import json  # 引入接json，用于数据格式转换

class Test_taobao():
     # 登录接口
     def test_login(self):
          # 请求url
          url = "https://login.taobao.com/newlogin/login.do?appName=taobao&fromSite=0&_bx-v=2.0.31"
          payload = 'loginId=dongdhq&password2=040d53b1135f51df41f034083480931def95994d57561585ab2c419786de2e231a861f3a188fa279adc535ffebd3e95cce0a18c8e633ccd15f22e915b3d813ca66220a2839aabdfa99849ce87459b22606d9612fee02ff4a9d18ec7b5fd3ae305d94579b65911b371d640f976f467f076c94da51ad40ec13cc77d2b16627596b&keepLogin=false&ua=140%23eNXDMwWfzzFfrzo2LxoTCtSdvN4O2o4eM0XRFRxEnUolrfZ1lT%2FSoViW2CdTPWE7MUdBQzdftxT2euZYfZkNu69%2Fdv%2Fqlbzxg8eKGStczzrf3XK7U6OzzPzbVXlqlbrDrGD%2BocZyhhOi2X0%2BlpYazDrbV2tz8broSIKKw3E%2FszrVc1844WQoVI%2BVAeBuHQrocDcKQt5uzF3Y2kJOqZoPzYLLMZ2aMX2sIRuf5xU7KogdmJplrbEK9DKtdOIdQs5TfEkq4ZpiSxor2hksD6qRLFCPYOVHTJzviaKmZER%2BdxzmG%2BaNxWCmEXkLMBgTukA32a4pcUwIPVqd4NTZvJHvab%2BOrm%2FJIF%2BNMoEZxqeShVRzHyNMRBj4EJl5Uk3cPgJEcHFViK6V7zr3pyS%2FfyDGarFCJonQh%2Boep%2BOgG19fb5WftjYIZ9b427QdkZK%2FbgzbxmWd4Em%2BG9cZ1d1rEk7sRjqY6suOh9XdCzMhmEy6FYu5gLFOZgBCOPOaYWfmud48FsKR3oMvPCBmrCCjuj971gGkmYcEl2fqg3wMnZaK2prwKLImVV%2B4cv1wIixHaTGXD6vesP8wOtHbK7kHeghjpuGJr3g4i6qUZHa0YvXtKwY4tdkBqYF9GgyOjYePkQPC2Rih7sc3JGIO4vqQ6%2BwxaCYXxT0%2BR0Re8sSu4tuQgTMwjSFmGJFtdtXrZwULo4Zq7P3b44bc221sbxi8PQJU8VYW%2BlY%2FUARlL2P7YEHLw5qSxJ00OqY2mvgZ%2Bc24lpNW%2BoOkitWTyTkL9iN%2BOOPdc1H6ACfN8iWG5kMIuc5DcSxepedtS8Ygp41G9LzV6hbiu3Q%2F8XxAmMH7SMfAGyCYshe0N%2F9s8coizCNIPHt%2FhATJu8l1Nzvnwem%2F6yFOeBE7%2BTHCK7zCZAQEtEqaxOJt6HO3wwjxaahnasesQO1Ew6ICW1i54Tv9R4NKXvUmpbYOTTYhQvlK%2BG7vV6muixJlMIOEwpvkVbjzJ0AXr7%2Fg2TchKiW3hZJXNebgg21YkxU9KoZHTRpvHTpjBSS%2BwF7gS8vWgGrUB%2F%2BXvHDWKl9zjv2ThK7usnhd6wXLvHsDCVZuIDfE99B1JMnw5N9fBrfjtqL5PjU94eUs6bNL4Mo4aAhLuSkO1rGlsQjsiuE1MRJX4NV1O8s0F5EiFD08%2Bgfh2XHY68OqbyO1TTSTD6uasWy8tJXHSK%2BD7jcnie%2FqoGKjRO665xn0jTWoMFFzZF%3D%3D&umidGetStatusVal=255&screenPixel=1536x864&navlanguage=zh-CN&navUserAgent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F91.0.4472.101%20Safari%2F537.36&navPlatform=Win32&appName=taobao&appEntrance=taobao_pc&_csrf_token=RkNjkEHjK1AthUHTeidwF2&umidToken=77917116efcf01bdc8c96135c7c54f0f6b06805b&hsiz=143fc3b0864d15c6b737ffd8c5d1d9ee&bizParams=&style=default&appkey=00000000&from=tb&isMobile=false&lang=zh_CN&returnUrl=http%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da230r.1.754894437.3.6e025193Tcfy6k%26pm_id%3D1501036000a02c5c3739&fromSite=0&bx-ua=212u00218VWWZw57WWvPP%2FKFU%2Fh7EY0ITO4wWWW6E9hZvA9Tu6Lw%2FPUwv%2FlKl55IT9CAW%2FYYqXZ9MdeBOWL6X6d8xWEWEYiLTOOmHQ6av3IJZZJXghR5pmMgT%2BP9zrKpX%2F63jXIPsbl8UpLkUrgdeDXFvMSQV6m0EjQ2uYOJ65zUXaOAhKxRSJ1p6clknZkk%2FH1N1j6XX8QT2iUwv9zI8k3KQIa11jQYWxr09T1LE5QQ4azY40aSoZcpe5m2gyltAQai7AZ%2FDSuUtY4u2ztCAugSW9hgdSH8AaKwlbo2JxQe91XuKrVGPV2vw6OY6GBOaDIumx%2BqNuqjMfmYG%2FRFJAmTNIUg9DubgwXNxUgz0DkSudVNHa1qlrt8QPH0Vy57mPKEvU%2FUAxnZgyPYAjHznhsBTMTgfTjJmS7qmUrlGPAaw26MhG%2B45yBDY81xQkwXRl0vd%2FbANbCS3A3R1%2FTJxTJzHrH1GoQ5sq2VLjq7OOqiUVYq3BLhssSK%2FSS4pKYh54qDgo6feaVxkiLa6ofBmysjcGuE3EmEImT2PNheNm2Sos3LZMsE7l%2FDRs1z7EG5klV4iuHpz%2FYBCyXX15RQhH3AsVrjbkDaNHwOAuZnxGhQFW1iLnqjwe9s7ooAly%2FXwwmWEyjYdgrS4TzzWIg%2Btfk4XWhlmd49ffo2XC9bTztCyzqnzGokgn3qY%2BZeTSnzKW4oYR2CFkz2REfVXzV7Sypzgc2MXaM7ITg9UbHExKoBNps%2BucQqKvOFqgZW2PzoiWQXIIJrNQ0FBH%2FV0Lg28budGwvHlHAD9xKw5EZnsL%2For2uh1CCQbM7QeacfDpNwn%2FIXFX4dZDpt4lo2Uo6IMof1dVTI%2BMqH6%2Fg0jp0Joi2DAbcWi8PmTbaawSFNOY4eq7XYo37pl3T55AkTbNs3W5%2FpsfpBtTexXM0KBYrry8YQE1GpR2HTH8FkfbnK8mN0OzVfTs1fk92%2FLGSn%2B4%2BFUMnExI8o9EnrnarpfvnTK6dgL3qqShr4rdLwXRe%2FMGZb%2FW5xjuOv0xObpdtyo%2Buz9OpIDqqjReIYZAT53f7omeCUrQW4VHWIeU4wllDLDT94RavaXoeMSiegsYWPX29CTss5%2BVTOnKQhou5jRbqJeOG8jYW6TWvxQ8sg1RgXTXH1L%2B6Rcat3eKeLaHF%2BAbLgoZ8y%2FZ1AiObcGt80Q%2BxsOC75WXGYy%2Btvamg09Fzp%2BezqXPPJFG0Nlsq3Y2ONGrsww0pbQYh8sb6mlviugJwhbOgujj57HYNkQlnnyhd9JPKMGMzYqJ0Rzci5ijW0VeypEtlP6dTdXmPG7PNbGn2LI8AOF%2BgSKEoENLZxk6iVjogtsmr8lJqqCRzvYHisFpxfG6Un94LjXd2NShdeoM%2B%2BUyWBvGrlJxDB6CGzSuGT1uN9%2BV%2BnRZHVQH6GhAJY%2BaZkQUiar6hdnfvvb3bX%2B951hVH9SUCywPC87eMqIQArStLrWA8YrJWwLs52GtkLzLBpDpgr4IL8j5tr%2FUgZ6%2Fg8SFXxsdzm62gwdvYQRXFfzbQzfSSUsxWJM%2BnbWHpX5bYSlWScTk9P4JzuwYEGny0SCt7QwjJaob5V6AJwCrxlFPj8GqVhqnPuU3wiSe6m836F0UiBaQfsWuCw93eWWXPfnuGB7i36q6cRrd5XKJJgQ5yASBlOGJ67COs8OwDTy54CDlH1FiT2d0ozW%2F2Gq7EjIEm6ViYmVVbnhWj3uw24TtV59yY8WlSHSJN6vpP0gfxCYEdK56%2Fl%2FSsaQzb48IiAEPUQITOJr05fh0BSIt22guFW5%2FLBVJKAhtOEWH5zTg44iHKGLRkXHyn7Yd6wrUDLEfkXYSTUBLGjEtcIxJ69ZjtoeoUsHM9wJdeRU8ANFDzYTwq1%2Fu3b4pM4EVxA9AXYj5vLDSad6RjFPyI5%2FFsS2m%2FO2da%2BzGEXeVvE%2FlDtIQgiQa%2FMP6jRVssgYdunwtrNRs7OMfcEXuSk6FZXrNQON9xQTZoB7ss4NImEXE%2F6u%2BimoDzYtH6BV3FV7YEdj0wKZhFSLoiJ8Q9xN6iebeoFZ%2BFOekhtA8p%2Bcjond9Ec6EpgaOSN7jbOcBlgKjb%2B%2BWmz&bx-umidtoken=T2gAilJxOt5SLUOfT3dImyNjX84LZsORxyyC0SG5b5UXFGOM7oDHIDkP-BOHmBKqCQk%3D'
          headers = {
              'authority': 'login.taobao.com',
              'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
              'sec-ch-ua-mobile': '?0',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
              'content-type': 'application/x-www-form-urlencoded',
              'eagleeye-sessionid': 'hekaep38waXbe5l4F2dCmvg13Xgg',
              'accept': 'application/json, text/plain, */*',
              'eagleeye-pappname': 'gf3el0xc6g@256d85bbd150cf1',
              'eagleeye-traceid': '78d57f1e1623657247921100250cf1',
              'origin': 'https://login.taobao.com',
              'sec-fetch-site': 'same-origin',
              'sec-fetch-mode': 'cors',
              'sec-fetch-dest': 'empty',
              'referer': 'https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da230r.1.754894437.3.6e025193Tcfy6k%26pm_id%3D1501036000a02c5c3739',
              'accept-language': 'zh-CN,zh;q=0.9',
              'cookie': 't=8a3bb05b24f0b7fb8992af9f4906912b; _bl_uid=mek07pp4tz5ly1xOgkmplFd2zLte; thw=cn; enc=vJ7ge4LCfityKgZ1C8p153ZgFURjZxH5h1Xjs7ae40spyYwdUE7RJiT%2BXerFHa%2FGBrL8FtPXSPM5QdKRrrmSfw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; lLtC1_=1; xlly_s=1; _m_h5_tk=fcd6677f27c8472b26f2328ae46baa0f_1623657768168; _m_h5_tk_enc=8fe9c4c044808141df2b7a8851a8bb67; XSRF-TOKEN=787d0837-868d-4673-a58d-1e350de862ed; _samesite_flag_=true; cookie2=143fc3b0864d15c6b737ffd8c5d1d9ee; _tb_token_=5e64de331ea63; ctoken=gATs0qYQDGY4hYaHFK8Irhllor; mt=ci=0_0; tracknick=; uc1=cookie14=Uoe2zs8JAeKCBg%3D%3D; cna=41QuF3Tj+F0CAXWYkRHCoqbv; l=eBjhLhRejZQUW3H3BO5whurza77tnIOfGsPzaNbMiInca1oRtFGrKNCBZBB2Sdtjgt5UQd-yVFTGFRHHSR4U-x1Hrt7APlUOrtJ6Re1..; isg=BF9fYDLCQ9G2V0fOa8yC64N87rPpxLNmVQRv2PGt_I5UgHsC3pcjt2AWQhD-GIve; tfstk=cO3fBuYjWtXjNWtNujOPbmZMMgaNasJ7ZnwxGDbjoBWhSMGbesDG8JNPicXlykF5.'
          }
          # 请求接口
          response = requests.request("POST", url, headers=headers, data=payload)
          print(response.json())
         # 断言接口返回状态
          assert response.status_code==200
          print('登录接口请求成功！')
     # 校验cookie 正确性

      # 商品搜索
     def test_search(self):
        # 请求url
        get_url='https://s.taobao.com/search'
        # 请求参数
        get_data={
            "q":"test",
            "imgfile":"",
            "js":"1",
            "stats_click":{
                "search_radio_all":"1"
            },
            "initiative_id":"staobaoz_20210614",
            "ie":"staobaoz_20210614"
        }

        # 请求接口
        result=requests.get(get_url,get_data)
        # 断言请求状态
        assert result.status_code == 200
        print('搜索接口请求成功！')

     # 商品下单
     def test_order(self):
          # 请求url
        get_url = "https://gm.mmstat.com/search?gmkey=&gokey=lf_aclog%3D1-618792538241-48-all%7C-1-24.00%26direct_cat%3D%26lf_acfrom%3D0%26at_alitrackid%3D%26at_bucketid%3D4%26multi_bucket%3D12_4_12_0_0_0_0_0%26srppage%3D1%26nick%3Ddongdhq%26rn%3De764e47bcdb1f0b4a7e00926ccb894a2%26multivariate%3Dmain_alg%253A266%253Bsearchapp_xmatch%253A3044%253Bmain_fe_extend%253A4547%253Bpfourp_test%253A236%253Bpfourp_mbox%253A4753%253Bmain_fe%253A301%253Bpricefixbts%253A8921%26stats_click%3Dtopcatpredict_flag%253A1%253Bs%253Amainsearch%253Bsearch_radio_all%253A1%253Buser_group%253AClusterMergeInfo%253A%253Bmd_QueryIntentionType%253A%253Bs%253Amainsearch%253Bbandit%253AGongYingLianDists%25253ACN%252BCKG103%252BCKG105%252BHFE103%252BHZO101%252BNKG401%252BNNG401%252BNNG403%252BPEK403%252BSHA105%252BSHA109%252B420100%252BCAZ401%252BCKG102%252BCKG104%252BCKG106%252BCKG107%252BCKG108%252BCKG110%252BDGM407%252BFUG401%252BFUZ101%252BHAI401%252BHCH101%252BHFE102%252BHGH102%252BHZ%252BJYN401%252BMES101%252BNID401%252BNKG102%252BNKG402%252BNNG402%252BPEK103%252BPEK104%252BSHA104%252BSHA106%252BSHE105%252BSTORE_1228938%252BSXHD%252BSXHZ%252BSZV101%252BSZV103%252BSZV405%252BSZX101%252BSZX102%252BTAZ101%252BTNA102%252BWUH103%252BWUH223%252BZHZ401%252B0%253Bqinfo%253A1%252C10%252C25%252C30%252C43%252C50%252C62%252C65%252C83%252C89%252C103%252C110%252C120%252C130%252C149%252C177%252C205%252C220%252C230%252C240%252C250%252C1107%252C9112%252C9201%252C150014927%252C224696009%252C1000000000%253Bzf_sort%253A42%253Bapass%253A0%253Bhas_sku_pic%253A0%253Btab_type%253Aall%253Bsn_hide%253A0%253Blist_model%253Agrid%253B%253Bsp_seller_type%253A0%253Bisp4p%253A0%253Bnewitem%253Anull%253Bauction_pid%253A573488409%3Bitem_click_from%3A1%26s_query%3Dtest%26vers%3Dj%26list_model%3Dgrid%26recommend_nav%3D%26risk%3D%26uidaplus%3D841684647%26_hng%3DCN%25257Czh-CN%25257CCNY%25257C156%26aws%3D1%26jsver%3Daplus_std%26lver%3D8.15.6%26pver%3D0.7.11%26cache%3Da31e715%26page_cna%3D41QuF3Tj%2BF0CAXWYkRHCoqbv%26_slog%3D0&cna=41QuF3Tj%2BF0CAXWYkRHCoqbv&_p_url=https%3A%2F%2Fs.taobao.com%2Fsearch%3Fq%3Dtest%26imgfile%3D%26js%3D1%26stats_click%3Dsearch_radio_all%253A1%26initiative_id%3Dstaobaoz_20210614%26ie%3Dutf8&_gr_uid_=841684647&spm-cnt=a230r.1.0.0.87c75193KGsHMs&logtype=2"

        headers = {
          'authority': 'gm.mmstat.com',
          'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
          'sec-ch-ua-mobile': '?0',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
          'accept': 'image/avi,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
          'sec-fetch-site': 'cross-site',
          'sec-fetch-mode': 'no-cors',
          'sec-fetch-dest': 'image',
          'referer': 'https://s.taobao.com/',
          'accept-language': 'zh-CN,zh;q=0.9',
          'cookie': 'cna=41QuF3Tj+F0CAXWYkRHCoqbv; cdpid=W80p9SbkRfwg; cnaui=841684647; aui=841684647; sca=3823d4a6; tbsa=8253bb184187b994d220bd00_1623651394_17; atpsida=dceea8aedc7d41ff943f3f9e_1623651399_18; cmida=1401053355_20210614141645; aui=841684647; cmida=1401053355_20210614141948'
        }
        response = requests.request("GET", get_url, headers=headers)
        # 断言请求状态
        assert  response.status_code==200
        print('商品下单成功！')

     # 提交订单
     def test_sumbit(self):
          url = "https://buy.tmall.com/login/buy.do?from=itemDetail&var=login_indicator&id=618792538241&shop_id=59108823&cart_ids=&t=1623652218327"
          headers = {
              'authority': 'buy.tmall.com',
              'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
              'sec-ch-ua-mobile': '?0',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
              'accept': '*/*',
              'sec-fetch-site': 'same-site',
              'sec-fetch-mode': 'no-cors',
              'sec-fetch-dest': 'script',
              'referer': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.1.87c75193KGsHMs&id=618792538241&cm_id=140105335569ed55e27b&abbucket=4',
              'accept-language': 'zh-CN,zh;q=0.9',
              'cookie': 'hng=CN%7Czh-CN%7CCNY%7C156; cna=41QuF3Tj+F0CAXWYkRHCoqbv; ubn=p; ucn=center; miid=207482133674429253; dnk=dongdhq; uc1=pas=0&existShop=false&cookie21=UtASsssmeWzt&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie15=UtASsssmOIJ0bQ%3D%3D&cookie14=Uoe2zs8JBzbGBQ%3D%3D; uc3=vt3=F8dCuw1Xp%2FIzWHEv81g%3D&nk2=B02oKbh7sQ%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&id2=W80p9SbkRfwg; tracknick=dongdhq; uc4=id4=0%40We5i4mPZX4qsMv0s6PEbw0RsChc%3D&nk4=0%40BQ4%2F2C7cCsoNZLV1lg7YrpUB; _l_g_=Ug%3D%3D; unb=841684647; lgc=dongdhq; cookie1=U7U2W6mjCOSsAXKKgwjfRdnjX%2FUdXVcyVbU1qguW9ds%3D; login=true; cookie17=W80p9SbkRfwg; cookie2=143fc3b0864d15c6b737ffd8c5d1d9ee; _nk_=dongdhq; sgcookie=E100WQ4ol5uJIx2MLSZY85Nq8fl7zMgMIPPgTbAhYdXAWZOBtJZ5PPrmUeDuDQbZs1WPTlegqv3UCnmB7LQ25ByJ9g%3D%3D; t=8a3bb05b24f0b7fb8992af9f4906912b; sg=q79; csg=1d7d0c46; _tb_token_=5e64de331ea63; xlly_s=1; enc=AXoJNoSRq9XtAAAAANz5XJsBX279%2Ff1TXXYVL%2F39Y%2F0Bc6lDiMF0vf8chVj9VM%2Bhy0CLmfLOhWkkgHaVjxD%2BbfRK; tfstk=c2ZfBRsbXIAjpQ_w0-6y7rT-jemhZ55SEZGYhyxXE3d5VjyficxEOYJ0SQx-JY1..; l=eBjM_SfgjZQJ9n_DBOfZlurza779AIRAguPzaNbMiOCPOpfw5NPlW6OrlnYeCnGVh6MHR3-W5FXWBeYBqnjRCSBNa6Fy_Ckmn; isg=BGdnQ67my7hynk82pdLdRjhD9psx7DvODdxnwDnUoPYdKIfqQb7YHqcqTii2wBNG'
          }
          response = requests.request("GET", url, headers=headers)
          print(response.status_code)
          # 断言返回成功状态码
          assert response.status_code==200
          print("提交订单状态返回200！")

          print(response.headers['Content-Type'])
          # 断言返回响应类型 为 text 、js类型
          assert  response.headers['Content-Type']=='text/javascript;charset=GBK'
          print("提交订单状态类型为："+response.headers['Content-Type'])

     # 支付订单
     def test_pay(self):

          url = "https://buy.tmall.com/login/buy.do?from=itemDetail&var=login_indicator&id=618792538241&shop_id=59108823&cart_ids=&t=1623655774764"
          headers = {
              'authority': 'buy.tmall.com',
              'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
              'sec-ch-ua-mobile': '?0',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
              'accept': '*/*',
              'sec-fetch-site': 'same-site',
              'sec-fetch-mode': 'no-cors',
              'sec-fetch-dest': 'script',
              'referer': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.1.6e025193Tcfy6k&id=618792538241&cm_id=140105335569ed55e27b&abbucket=4',
              'accept-language': 'zh-CN,zh;q=0.9',
              'cookie': 'hng=CN%7Czh-CN%7CCNY%7C156; cna=41QuF3Tj+F0CAXWYkRHCoqbv; ubn=p; ucn=center; miid=207482133674429253; dnk=dongdhq; uc1=pas=0&existShop=false&cookie21=UtASsssmeWzt&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie15=UtASsssmOIJ0bQ%3D%3D&cookie14=Uoe2zs8JBzbGBQ%3D%3D; uc3=vt3=F8dCuw1Xp%2FIzWHEv81g%3D&nk2=B02oKbh7sQ%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&id2=W80p9SbkRfwg; tracknick=dongdhq; uc4=id4=0%40We5i4mPZX4qsMv0s6PEbw0RsChc%3D&nk4=0%40BQ4%2F2C7cCsoNZLV1lg7YrpUB; _l_g_=Ug%3D%3D; unb=841684647; lgc=dongdhq; cookie1=U7U2W6mjCOSsAXKKgwjfRdnjX%2FUdXVcyVbU1qguW9ds%3D; login=true; cookie17=W80p9SbkRfwg; cookie2=143fc3b0864d15c6b737ffd8c5d1d9ee; _nk_=dongdhq; sgcookie=E100WQ4ol5uJIx2MLSZY85Nq8fl7zMgMIPPgTbAhYdXAWZOBtJZ5PPrmUeDuDQbZs1WPTlegqv3UCnmB7LQ25ByJ9g%3D%3D; t=8a3bb05b24f0b7fb8992af9f4906912b; sg=q79; csg=1d7d0c46; _tb_token_=5e64de331ea63; xlly_s=1; enc=AXoJbOGrokcXAAAAANz5XJsBWj3r%2Ff1SSz79Cv3hAXMzGFKqXlvCFe7Ku6EtjrkKdbC0EXD5ghqnlBB7mg8gQw%3D%3D; tfstk=cbLRB_2-pxDlBsfv_3nmA4JqFKORaVNRK76LJb86XX3EnYaLRs0eSFK1j01UeZhA.; l=eBjM_SfgjZQJ99h2BOfZPurza77TxIRVguPzaNbMiOCP_kfJ5XtPW6OkgLYvCnGVH67DR3-W5FX7B-YOEyI4CPseu_BkdloZ3dC..; isg=BNzcZ3Q20Ci3sqR36hs2V2_qrfqOVYB_muVMwbbdpke5AX6L3mf8DyPzYWn5ibjX; ubn=p; ucn=center'
          }
          response = requests.request("GET", url, headers=headers)
          # 断言请求成功状态码返回200
          assert response.status_code==200
          print("请求状态码返回200！")

          print(response.headers)
          # 端元请求响应类型为：text、js类型
          assert response.headers['Content-Type']=='text/javascript;charset=GBK'

tbTest = Test_taobao();
tbTest.test_login()
tbTest.test_search()
tbTest.test_order()
tbTest.test_sumbit()
tbTest.test_pay()






