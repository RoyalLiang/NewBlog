from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from blog.models import BlogModel, LabelModel
from comments.models import ArticleCommentModel
from extra.base.views import BaseView, BaseGetView, BasePostView
from extra.decorate import catch_page


class CommonView(BaseGetView):

    def get(self, request, *args, **kwargs):
        return self.response()

    def post(self, request):
        return HttpResponse('SUCCESS')


class ConfigView(BaseGetView):

    def _process(self, request, *args, **kwargs):
        # r = {"forum":"RoyalLiang","admin_username":"RoyalLiang","public_key":"","authorize_url":""}
        return self.response()


class OptionView(BaseGetView):

    def _process(self, request, *args, **kwargs):
        r = {"_id":"589e01b75af07d59124234cd","title":"Surmon.me","sub_title":"来苏之望","description":"凡心所向，素履所往；生如逆旅，一苇以航。","site_url":"https://surmon.me","site_email":"i@surmon.me","keywords":["Surmon","苏尔蒙","surmon 前端技术博客","surmon.me blog"],"__v":128,"meta":{"likes":635},"update_at":"2022-03-01T10:28:14.312Z","ad_config":"{\"BACK_UP_LINKS\":{\"淘宝（N）\":\"https://ai.taobao.com?pid=mm_41374337_2187400162_111073050478&union_lens=lensId%3APUB%401608571488%400b0b4eb0_0e24_176865507bf_03e9%4001\",\"ECS 服务器\":\"https://s.click.taobao.com/t?e=m%3D2%26s%3DwQGNwGZHks8cQipKwQzePCperVdZeJviEViQ0P1Vf2kguMN8XjClAl9fhuiKqypCkpyF%2FKhpxf16yA%2BmzrwhsmISS9fD%2BpNs0m12%2FErQE8AYYA30%2Bp3IBBvsds8Rw%2FhBYMsSHLWchUVtQl8vLdysepHjKlMEkHC06du04PdR3Oc9XUfbPSJC%2F02QpUwcKVbRBsyo6kUwi%2Bcv%2FIct653eazL4Qf1nAUKDyxemGfaaDIVsOChAV2X4biGFCzYOOqAQ\",\"轻量应用服务器\":\"https://s.click.taobao.com/t?e=m%3D2%26s%3DJOsqTG8r0JEcQipKwQzePCperVdZeJviEViQ0P1Vf2kguMN8XjClAszNUAT7%2BTd7gP494rOBEK56yA%2BmzrwhsmISS9fD%2BpNs0m12%2FErQE8AYYA30%2Bp3IBBvsds8Rw%2FhBYMsSHLWchUVtQl8vLdysepHjKlMEkHC06du04PdR3Oc9XUfbPSJC%2F02QpUwcKVbRX7%2BliFBjeJfQWJeWE%2FFfPg%3D%3D\",\"阿里云 云大使（官方活动页）\":\"https://www.aliyun.com/activity?source=5176.11533457&userCode=pu7fghvl#promotionArea\",\"阿里云 云小站（领取优惠券固定）\":\"https://www.aliyun.com/minisite/goods?userCode=pu7fghvl\"},\"PC_CARROUSEL\":false,\"PC_NAV\":[{\"icon\":\"icon-aliyun\",\"color\":\"#ff6a00\",\"url\":\"https://www.aliyun.com/minisite/goods?userCode=pu7fghvl\",\"i18n\":{\"en\":\"Aliyun\",\"zh\":\"云上爆款\"}}],\"PC_ASIDE_SWIPER\":[{\"url\":\"https://cloud.tencent.com/act/cps/redirect?redirect=1077&cps_key=8a58019c32584cfa76de23f9986c17ed&from=console\",\"src\":\"https://static.surmon.me/assets/pc-aside-tencent.jpg\"},{\"url\":\"https://www.aliyun.com/minisite/goods?userCode=pu7fghvl\",\"src\":\"https://static.surmon.me/assets/pc-aside-1-aliyun.jpg\"}],\"PC_MERCH_PRODUCTS\":[{\"name\":\"DJI 大疆 御 Mavic air2 无人机\",\"description\":\"性价比高，皮实好用\",\"detail\":\"购置一年，累计飞行超过 200km，去过新疆和青藏高原，拍过不少大片，DJI 现在出新款了，但是定位都较贵，Air2 性价比依旧很高，推荐畅飞套装\",\"src\":\"https://static.surmon.me/merch/products/dji-mavic-air-2.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAM4JK1olXDYCVV9cCEgRC28JHVolGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloUXQUEXF5cDkoIWipURmt-JXNaHD49Yy5_SwthRj58Q3pSDB09BEcnAl8IGloVXwcFVlxVOHsXBF9edVsUXAcDVV1fDEonAl8IHFkcXQMLUVlZAU4SM2gIEmtOCGgGUg5cDB4WCm0LSQgXbTYyV25tOEsnAF9KdV1CVQBQUg0JD08QA2oKHwkdVQ5RV1wJXU0WU2kAGAxBbQQDVVpUOA\"},{\"name\":\"GoPro HERO10 Black\",\"description\":\"地表最强运动相机\",\"detail\":\"我和我的的狗7一起去过芽庄潜水，和摩托车一起穿越阿尔金山，从未掉过链子，当然既然已经有 10 了，那就不要买 7/8/9 了，无论是小屏还是 5k 都是很值得买的点\",\"src\":\"https://static.surmon.me/merch/products/gopro-9.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BANYJK1olXgEAXV5aCEgTB18IGloUXQQFU1taC08nRzBQRQQlBENHFRxWFlVPRjtUBABAQlRcCEBdCUoWA20PHF4SXgIdDRsBVXtudBV0fxhjNGRwKlkHcwpBAy9OY15TUQoyVW5dCUoXAW4PGVkdbTYCU24fZkgWAG9eRRpWAzYDZF5aCkIXBmYPGV4SXw4yU15UOBBCbWsOS1oRCAcLVl0PW0knM18LK2slXTYBZBwzXEwSVGZYHwwUXFRQUQ5dCkJAC28KS1IUDwRVVgteCU4nAW4JH1Il\"},{\"name\":\"SONY 索尼 α6400 微单相机\",\"description\":\"入门日用首选\",\"detail\":\"如果你关注过我在 Ins 或者朋友圈发的图，你就应该震撼于这台小小的 C 画幅机器的巨大创作能量。当然最值得关注的是：它足够便宜，它绝对是你入门摄影的最佳机器！\",\"src\":\"https://static.surmon.me/merch/products/sony-a6400.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAM4JK1olXDYCVV9cCUkWAGkOEl4lGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloUXAQDV1hbAU4IWipURmsLBVlAAggcCilEcRpUY1xsPXtbNjUtBEcnAl8IGloVXwcFVlxVOHsXBF9edVsUXAcDVV9VC0snAl8IHFkcXQMLXVZeDksSM2gIEmtOCGgGUg5cDB4WCm0LSQgXbTYyV25tOEsnAF9KdVwcDVIKXApVDEpFUWoNH18cXgIFAF1dDB9FVGYIE1pFbQQDVVpUOA\"},{\"name\":\"SIGMA 适马 30mm F1.4 镜头\",\"description\":\"王者三剑客\",\"detail\":\"你应该听过适马三剑客的声誉，C 画幅的机器 30mm 相当于 50 的全画幅，适合挂机扫街，我的那些人像静物作品都来源于这款镜头\",\"src\":\"https://static.surmon.me/merch/products/sigma-30-14.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAMQJK1olXDYBUFlcCkIQMytXQwVKbV9HER8fA1UJWypcR0ROCBlQCgJDC08QAm0BHERMGFpfZCYCcj9OAi9se10WFlYKMDotX1FRUw8EF2sUbQYDVV5fCUwVAWc4K1sSbVBsVF9cCUoWAW0NHGsUbQYFVlddDUMXBW0OE1klWgYLZAUIZk8RU24MTlocXwVQB1xtOHsUM184G2sWbURsVVoODUJFU2ddTAwTWAQBUlZfC08UAj1fGAwSCFYEAVptCkoWB2Y4\"},{\"name\":\"Microsoft 微软 Surface Pro 8\",\"description\":\"更好的体验和配置\",\"detail\":\"我自身使用的是 Surface Pro 6，也是家里的一台唯一的 Windows 机器，自从 Win11 支持安卓子系统后，基本上 Surface 可以同时当做一个安卓平板使用，当然不推荐你买和我一样的旧款，所以入 8，很合适！\",\"src\":\"https://static.surmon.me/merch/products/surfacepro7.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAM4JK1olXDYCVV9cC00SA2gOHV4lGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloUXgAHVFlbDk4IWipURmtiOhhQLEAKFilCBBhwcghVG3lrHAEbBEcnAl8IGloVXwcFVlxVOHsXBF9edVsUXAcDVV9fC0wnAl8IHFkcXQMKVlldAU8WM2gIEmtOCGgGUg5cDB4WCm0LSQgXbTYyV25tOEsnAF9KdVwRWwALAwxdXE0fBWpcTltFWwFRU1wPARhCAWwAHAsUbQQDVVpUOA\"},{\"name\":\"Microsoft Xbox Series 手柄\",\"description\":\"完美手感，全平台兼容\",\"detail\":\"我没有 Xbox，但是买了这款手柄，之前配家里的一台 Windows 玩地平线及古墓丽影之类的一些游戏，后来 M1 Mac 官方完美支持后，在 Mac 上打模拟器游戏，同时还能完美适配 Android 和 iOS，手感也比 PS 好，真的会提升很多幸福感\",\"src\":\"https://static.surmon.me/merch/products/xbox-series.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAM4JK1olXDYCVV9cCEwXBmYAGlIlGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloUXQECUVdVCUIIWipURmtKCGZjMF0aSS5ceQhcWCNOJVhEH0ALBEcnAl8IGloVXwcFVlxVOHsXBF9edVsUXAcDVV9fC0wnAl8IHFkcXQMKU1xeCEofM2gIEmtOCGgGUg5cDB4WCm0LSQgXbTYyV25tOEsnAF9KdVtAXgVRVllcCUJFUGoPGltGWAcLXFhdD0oXC2ddG1IcbQQDVVpUOA\"},{\"name\":\"SONY 索尼 WH-1000XM3 耳机\",\"description\":\"没啥说的，大法好\",\"detail\":\"已经出 WH-1000XM4 了，好像就是多了一个感应器功能，而且还没 WH-1000XM3 卖得好，不知道为啥；如果你还在纠结降噪耳机选哪款，就选大法，绝对不会后悔的\",\"src\":\"https://static.surmon.me/merch/products/sony-wh-1000xm4.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAM4JK1olXDYCVV9cCUofC2YAGFolGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloUXAcKXFdVC0oIWipURmtDJF1BCgwHYSsUR2xqHjlQNQF2NA49BEcnAl8IGloVXwcFVlxVOHsXBF9edVsUXAcDVV9VC0snAl8IHFkcXQMKXVhbDUgRM2gIEmtOCGgGUg5cDB4WCm0LSQgXbTYyV25tOEsnAF9KdQlBVQQGB1xdXB8WAGpdG1tGDgIGUQ1fDR9DUDgKHV4UbQQDVVpUOA\"},{\"name\":\"Amazon Kindle Paperwhite 5\",\"description\":\"屏幕变大，配置升级\",\"detail\":\"不知道为啥各个平台都一直缺货，10月份第一次预售我就抢到了，已经把用了5年的青春款换掉了，新款用了 USB-C 接口，多了夜灯，屏幕变大，边框变窄，分辨率也提高了，总体来说就是好好好，截止今天 11月底我几经读完5本书了\",\"src\":\"https://static.surmon.me/merch/products/kindle-paperwhite-5.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAM4JK1olXDYCVV9cCE4UAWcPHFslGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloUXQMBVlZaD0sIWipURmsdIGZEMABfdCtHdTB9aBhINEJXNQ0tBEcnAl8IGloVXwcFVlxVOHsXBF9edVsUXAcDVV1cD0gnAl8IHFkcXQIDVVdeCUwTM2gIEmtOCGgGUg5cDB4WCm0LSQgXbTYyV25tOEsnAF9KdQlHCgZXB18KWhkVC2oOEwscDgUKUFpYW0hFAmYPEl4VbQQDVVpUOA\"},{\"name\":\"DELL 戴尔 27英寸 4K 显示器\",\"description\":\"每个开发者必备\",\"detail\":\"刚刚好的物理尺寸和像素密度，U2718QM 好像现在升级为 U2720QM 了，加量不加价，需要就购置一台吧\",\"src\":\"https://static.surmon.me/merch/products/dell-U2718.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BANcJK1olXgMKXFdYDEkQAV8IGloUXQYAVFhcDUInRzBQRQQlBENHFRxWFlVPRjtUBABAQlRcCEBdCUoWA28KG10UWA8dDRsBVXsNdA5zR11QX2VFDAMAATRfBiR3YQRDUQoyVW5dCUoXAW4PGVkdbTYCU24fZh5DXjJUSQZHCAQyVW5dD0keA2sJGVMRXAMAZFldAXtMVgEMHQsUWVMDXVxeWhgVM184GGslbQYyV24fZk4TC2YLHlIXXg4GUVteWE1HBToAE1gQXg4LUVpbDh4XM20JGl8cbQ\"},{\"name\":\"Logitech 罗技 K380 蓝牙键盘\",\"description\":\"便宜好用\",\"detail\":\"这玩意没啥说的，就是便宜好用啊，特别是和 Mac 很搭！一键切设备太实用，我天天在 Surface 和 Mac 之间无缝转换靠的就是这家伙\",\"src\":\"https://static.surmon.me/merch/products/logitech-k380.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAMwJK1olVQ4FVV5UC08XM28AG14XXwUyEAEFVhQnWipNWhkeQxhaEQoBFxBCHD1WR0UVVQYHVlxeFxJSXzI4ZTNxXQNqXBg9DVF_SzpfGDxVFFRGJFJROEonA24JG1kUWgQAXG5tCEwnVQEIGloUXAcDV1tUOEonA2gKElsRXAILU1pcD3sQA2Y4QA57WQBSVVoICUIVAD1bGWslbQUyZG5dOEgnQQFcHQkUCAIBXFlZC00SVmcNEg5FWwABUwxaX0hEU25YGGsXXAcGXW4\"},{\"name\":\"Logitech 罗技 M336 蓝牙鼠标\",\"description\":\"好用，家里有三个\",\"detail\":\"1. 微动手感很好 2. 简约好看好握 3. 我真的买了三个\",\"src\":\"https://static.surmon.me/merch/products/logitech-m336.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAMwJK1olVQ4FVV5UC08XM28BGFoWWAYyEAEFVhQnWipNWhkeQxhaEQoBFxBCHD1WR0UVVAUDV1tdFxJSXzI4TgRUD0JbAC0-bwtDHQdjQAJuAVt2ElJROEonA24JG1kUWgQAXG5tCEwnVQEIGloUXAcDV1tUOEonA2gKElsRXAAFVVdaDnsQA2Y4QA57WQBSVVoICUIVAD1bGWslbQUyZG5dOEgnQQFdTg8QXwEKXVcKCR4SBWlaSw8TWw4BBFteDRgeVzhbT2sXXAcGXW4\"},{\"name\":\"Apple HomePod mini\",\"description\":\"苹果牛逼\",\"detail\":\"如果你家里有超过两个苹果设备，就可以入它了，AirPlay 很方便，事实上我还有一款 Boss 的支持 AirPlay 的多源音响在一起组的立体声，声效特别好\",\"src\":\"https://static.surmon.me/merch/products/apple-homepod-mini.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAM4JK1olXDYCVV9cCEwWBmgKHVIlGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloUXQEDUVlfDkIIWipURmsTD0JbFyk4UytreQ1-HiFBWl1JDyMLBEcnAl8IGloVXwcFVlxVOHsXBF9edVsUXAcDVV9dC00nAl8IHFkcXQIDXVZaDUkUM2gIEmtOCGgGUg5cDB4WCm0LSQgXbTYyV25tOEsnAF9KdVgVCFFVUAsOAB4WUGoNHglFVAYGA1sOAEMQATpYTl1FbQQDVVpUOA\"},{\"name\":\"绿联 氮化镓 GaN100W 充电器\",\"description\":\"出门一个一把梭\",\"detail\":\"好用在哪呢？100w 大功率，可以持续输出多设备，我出门就带这一个家伙，剩下的只是把线准备好就行\",\"src\":\"https://static.surmon.me/merch/products/ugreen-charger.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAM4JK1olXDYCVV9cCEsQBGoMGV0lGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloUXQYFU1tZCk0IWipURmteC3xyKisYTSlwYQcAZAtvJFsYNl0tBEcnAl8IGloVXwcFVlxVOHsXBF9edVsUXAcDVVhYCEInAl8IHFkcXQICVVpZC0wXM2gIEmtOCGgGUg5cDB4WCm0LSQgXbTYyV25tOEsnAF9KdV9GDwJRAAkNDEpDV2oKSAsdXAALVlwIDB8eBm0OHVMXbQQDVVpUOA\"},{\"name\":\"EPSON 爱普生 TW740 投影仪\",\"description\":\"让幸福感 +10000\",\"detail\":\"我之前有篇文章写过测评，写的很详细，市面各种 LED 的、激光的机器我都试过了，全退了没法看；事实上爱普生带系统的几个机器，系统也是无比拉胯，所以我是拿这款 1080p 的机器 + MiBoxs 海外版组的一套，非常非常皮实实用，很快就要达到豆瓣1000篇电影的目标了\",\"src\":\"https://static.surmon.me/merch/products/epson-tw740.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BANcJK1olXg8FVF9YCEkfB18IGloUXA8FVVZdC0snRzBQRQQlBENHFRxWFlVPRjtUBABAQlRcCEBdCUoWAmYPGlMVXgYdDRsBVXtUeC9zH1JUIWV4EAQfUT0RHTpAbEFTUQoyVW5dCUoXAW4PGVkdbTYCU24LZksWAm4JGloQXgIyVW5dD0keA2sIGF4WXAYGZFldAXtMVgEMHQsUWVMDXVxeWhgVM184GGslbQYyV24fZhgWAGcNS14QCAYBA1sOWEIfAmcOGlMTDlUEBFcPAE4SM20JGl8cbQ\"},{\"name\":\"米家 空气净化器\",\"description\":\"有用，好用\",\"detail\":\"我家里没甲醛，我用这玩意儿吸雾霾、狗味儿、偶尔抽烟的烟味，以及周末大扫除的那天给屋内做个清洁，感觉很实用\",\"src\":\"https://static.surmon.me/merch/products/mi-air-clear.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BAM4JK1olXDYCVV9cCEkTCmoOHFklGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloUXQQGXVtbD0kIWipURmtNDVRwCDUmYy5iYStfayxRBngYPUQtBEcnAl8IGloVXwcFVlxVOHsXBF9edVsUXAcDVVtdC0knAl8IHFkcXQICUVxdCE4UM2gIEmtOCGgGUg5cDB4WCm0LSQgXbTYyV25tOEsnAF9KdQsRClYKBFxbChkfA2pYGFJGDVMEAFtaCRkRBmlfEw5HbQQDVVpUOA\"},{\"name\":\"米家 踢脚线电暖气\",\"description\":\"热得快，不费电\",\"detail\":\"和米家生态整合的很好，去年冬天买的，热得很快，低功率模式下，甚至可以穿个袜子搭在上面，如果你住的地方没暖气，可以考虑入手一台\",\"src\":\"https://static.surmon.me/merch/products/mi-heating.jpg\",\"url\":\"https://union-click.jd.com/jdc?e=&p=JF8BANMJK1olXQEKU1peDE8WB18MH18XXAILV1ZbDntTXDdWRGtMGENDFlVDFhNSVzMXQA4KD1heSlpZDEkWB2YLE10TQl9HCANtEh5DRgRucit2K3BEU0RUEjJfXSx8a1cZbQcyVF9cCEkWBG0KE2slXQEyFTBdCUsWA2YAGmsUbQYFVlddDEsTBG0PH1IlWgYLZAUIZk8RU24MTlocXwVQB1xtOHsUM184G2sWbURsVVtYXBsQVjpYSFtFWA9XAw1dXRhEC2cJGVsUVQdSUlltCkoWB2Y4\"}],\"PC_MERCH_BROKERS\":[{\"name\":\"富途牛牛\",\"description\":\"腾讯旗下，业界第一\",\"detail\":\"虽然我去年在美股亏了小十万，但还是得说富途是所有港美股券商中做的最好的；体验优异、港美股融资打新均支持；自有港股暗盘；支持 eDDA 入金，用户庞大；富途是我的主交易账户\",\"src\":\"https://static.surmon.me/merch/brokers/futu.webp\",\"url\":\"https://growth.futuhainan.com/new-customer-2101?code=4a751a5c06d6be724b7a18dd6d271aa2\"},{\"name\":\"老虎证券\",\"description\":\"港美股交易均支持\",\"detail\":\"老虎从去年收购了香港一些本土券商之后有了新的牌照，也跻身全地域券商的行列了；App 体验优秀，出入金快，港股 IPO 手续费固定￥100，由于有美国牌照，老虎是少有的支持美股打新的券商，我主要用来打新\",\"src\":\"https://static.surmon.me/merch/brokers/tiger.webp\",\"url\":\"https://www-web.itiger.com/activity/forapp/invitation/*LNLOGI-signup.html?invite=LNLOGI#/\"},{\"name\":\"新浪华盛通\",\"description\":\"新浪旗下，稳定好用\",\"detail\":\"新浪旗下的老牌券商，运营多年的品牌；App 体验优秀，支持港美股交易，支持 eDDA 入金，港股 IPO 手续费比较实在，经常送券，是我用于打新的主力账户\",\"src\":\"https://static.surmon.me/merch/brokers/hst.webp\",\"url\":\"https://hd.hstong.com/invite/market/accept?invite=VREMT\"},{\"name\":\"雪盈证券\",\"description\":\"雪球 + 盈透 = 雪盈\",\"detail\":\"雪盈的港股业务主要是和盈透亚洲的合作，其开立的账户都和盈透后台的账户对应，简单可以理解为，雪盈就是盈透的一个客户端；整体体验很好，由于没有自己的牌照，所以打新也只能融资，但又要求有保证金，出入金有点不方便，首次需要到盈透后台人工做一些操作；我目前不太使用雪盈\",\"src\":\"https://static.surmon.me/merch/brokers/xy.webp\",\"url\":\"https://snowball-x.com\"},{\"name\":\"长桥证券\",\"description\":\"阿里系投资人 + 香港辉立\",\"detail\":\"长桥是杭州阿里系产品，底层对接的香港辉立证券，所以它的 FPS 收款能力一直没有开放，只能使用转账入金；不过这个团队迭代很快，产品几个版本已经发生了大的优化，客户经理对接也非常积极；长桥主要用于港股交易、IPO，现金打新手续费很便宜\",\"src\":\"https://static.surmon.me/merch/brokers/long-bridge.webp\",\"url\":\"https://activity.lbkrs.com/pipeline/2021newactivities/index.html?sac=lb&loginUrl=&lbFitsStatusBar=0&invite-code=528947&channel=HM000001\"},{\"name\":\"华泰国际 涨乐全球通\",\"description\":\"华泰旗下，体验优秀\",\"detail\":\"华泰证券旗下的港股子品牌，App 做得很好，支持港美股交易，支持 eDDA 入金，有自己的会员机制，购买会员后一年内融资打新免手续费；只是图形数据方面不太专业，且不支持碎股交易，我开通了会员用作主力打新账户\",\"src\":\"https://static.surmon.me/merch/brokers/ht.webp\",\"url\":\"https://m.zhangleglobal.com/views/to-introduce-c/index.htm?type=3&ciphertext=AD3F8DAC8BA00F75B3536B699B3D84F7A3A3BAA116A9F65F8E6B70270B8A2FAD\"},{\"name\":\"艾德证券\",\"description\":\"小而美的券商\",\"detail\":\"有资质的新兴小券商，客户经理跟进及时，主要业务在香港和深圳；现金打新手续费便宜，是我的主力打新账户\",\"src\":\"https://static.surmon.me/merch/brokers/ed.png\",\"url\":\"https://www.eddidyzt.com/app_landing/yqzsj2/?myyqm=10175254&is_share=true\"},{\"name\":\"盈立智投\",\"description\":\"香港 Fintech 公司\",\"detail\":\"香港本土的 Fintech 公司，看起来是想向量化方面发展业务；支持 eDDA 入金，资质全，出入金效率高，现金打新几乎不要手续费，是我的首选打新账户\",\"src\":\"https://static.surmon.me/merch/brokers/usmart.webp\",\"url\":\"https://m.usmart8.com/marketing/activity/newcomer-award.html?ICode=x7tq#\"},{\"name\":\"哈富证券\",\"description\":\"东方财富旗下的港美股券商\",\"detail\":\"东方财富收购原持牌券商后成为少有的 A 股互联网券商；后进军港美股业务，收费也还行，App 体验良好，业务支持完成度较高，支持 eDDA 入金，我用来做主力打新账户\",\"src\":\"https://static.surmon.me/merch/brokers/hafoo.webp\",\"url\":\"https://marketing.dfcfs.com/views/actfissionhafu/invite?inviteCode=d94d09a305a9cdfe13132de29f4b3f3d&openid=ohJTzjihdXypDuXZbKJDi5vzZQvk&headImg=http%3A%2F%2Fhy.eastmoney.com%2Femwx2019%2Fimg%2FohJTzjihdXypDuXZbKJDi5vzZQvk&nickName=Surmon&unionid=oHW6st5nhLS26ilxUKS4KyfxsrgA\"},{\"name\":\"辉立证券\",\"description\":\"香港第一，HK$38 套餐\",\"detail\":\"香港本地券商行业的龙头老大，可在百科查到历史，拥有香港最大的暗盘，实力雄厚；只是 App 万年不更新，还是大概 10 年前的 Flash 技术做的，辉立最出名的是 HK$38 套餐，即只需 HK$38 即可认购一定数量的新股，只需要保证账户内最少有一定保证金即可；辉立是我的必用打新账户\",\"src\":\"https://static.surmon.me/merch/brokers/poems.webp\",\"url\":\"http://www.poems.com.hk\"},{\"name\":\"耀才证券\",\"description\":\"香港第二，融资利率低\",\"detail\":\"香港本地第二老牌券商，支持港股和期权交易，支持 eDDA 入金，融资利率低、额度充足，可上甲乙组，现金打新免费，是我的必用账户之一\",\"src\":\"https://static.surmon.me/merch/brokers/yc.png\",\"url\":\"https://www.bsgroup.com.hk\"},{\"name\":\"佳投环球\",\"description\":\"佳兆业旗下，实力派\",\"detail\":\"佳兆业旗下金融业务，有很强的业务实力，App 也好用\",\"src\":\"https://static.surmon.me/merch/brokers/jzy.webp\",\"url\":\"https://www.kaisaglobal.com\"}]}","friend_links":[{"name":"吕立青的博客","value":"https://blog.jimmylv.info"},{"name":"nighca's log","value":"https://nighca.me"},{"name":"vzchn's Blog","value":"https://blog.vzchn.com"}],"statement":"站点声明"}
        return self.response(data=r)


class BlogListView(BaseGetView):

    @catch_page
    def _process(self, request, *args, **kwargs):
        articles = BlogModel.list({}, self.page, self.page_size)
        p = {'total': 1, 'current_page': 1, 'per_page': 1, 'total_page': 1}
        return self.response(data={'data': articles, 'pagination': p})


class HotBlogView(BaseGetView):
    pass


class BlogDetailView(BaseGetView):

    def get(self, request, pid):
        articles = BlogModel.list({'id': pid}, detail=True)
        if articles:
            article = articles[0]
        else:
            article = {}
        return self.response(data=article)


class BlogContextView(BaseGetView):

    def get(self, request, pid):
        r = dict(prev_article=None, next_article=None, related_articles=[])
        return self.response(data=r)


class CommentView(BaseGetView):

    def _process(self, request, *args, **kwargs):
        """
        {
                "_id":"621c3f63c22be1bb38e5c1db",
                "post_id":199,
                "pid":2366,
                "content":"“人性”",
                "agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
                "author":{
                    "name":"Surmon",
                    "site":"https://surmon.me",
                    "email_hash":null
                },
                "state":1,
                "likes":0,
                "dislikes":0,
                "ip_location":{
                    "country":"China",
                    "country_code":"CN",
                    "region":"Shanghai",
                    "region_code":"SH",
                    "city":"Pudong",
                    "zip":""
                },
                "extends":[
                    {
                        "name":"disqus-post-id",
                        "value":"5772253662"
                    },
                    {
                        "name":"disqus-thread-id",
                        "value":"9045419483"
                    },
                    {
                        "name":"disqus-author-id",
                        "value":"231849069"
                    },
                    {
                        "name":"disqus-author-username",
                        "value":"surmon"
                    }
                ],
                "update_at":"2022-02-28T03:20:03.004Z",
                "create_at":"2022-02-28T03:20:03.004Z",
                "id":2367,
                "__v":0
            }
        """
        p = {'total': 0, 'current_page': 1, 'per_page': 50, 'total_page': 1}
        comments = ArticleCommentModel.objects.all()
        r = [{
            'id': i.pk,
            'post_id': i.blog.pk,
            'content': i.content,
            'pid': i.pid,
            'agent': '',
            'create_at': str(i.create_time),
            'author': {
                'name': i.nickname,
                'email': i.email,
                'site': ''
            },
            "state": 1,
            "likes": 0,
            "dislikes": 0,
            "ip_location": {
                "country": "China",
                "country_code": "CN",
                "region": "Shanghai",
                "region_code": "SH",
                "city": "Pudong",
                "zip": ""
            },
            'extends': []


        } for i in comments]
        r = dict(data=r, pagination=p)
        return self.response(data=r)


class HotBlogListView(BaseGetView):

    def _process(self, request, *args, **kwargs):
        p = {'total': 0, 'current_page': 1, 'per_page': 1, 'total_page': 1}
        return self.response(data=[])


class CategoryListView(BaseGetView):

    def _process(self, request, *args, **kwargs):
        if self.page <= 0 or self.page_size <= 0:
            return self.response()
        cats = LabelModel.list(self.page, self.page_size, cat='CATEGORY')
        p = {'total': 1, 'current_page': 1, 'per_page': 1, 'total_page': 1}
        return self.response(data={'data': cats, 'pagination': p})


class TagListView(BaseGetView):

    def _process(self, request, *args, **kwargs):
        if self.page <= 0 or self.page_size <= 0:
            return self.response()
        tags = LabelModel.list(self.page, self.page_size, cat='TAG')
        return self.response(data=tags)


class CalendarView(BaseGetView):

    def _process(self, request, *args, **kwargs):
        resp = [{'count': 1, 'date': "2022-02-18"}]
        return self.response(data=resp, msg='Get article calendar succeed')


class AuthorView(BaseGetView):

    def _process(self, request, *args, **kwargs):
        r = {"slogan":"Engineer / Freelancer / Digital nomad / 前端表演技术家 / 伏特加战士 / 海底捞之王","name":"Surmon","__v":0,"avatar":"https://cdn.surmon.me/_proxy/default/https%3A%2F%2Fwww.gravatar.com%2Favatar%2Ffa6719aa3cb274e29e9bec58459e8425%3Fs%3D360"}
        return self.response(data=r)


class VoteBlogView(BasePostView):

    def _process(self, request, *args, **kwargs):
        blog = BlogModel.vote(self.req['article_id'], vote=self.req['vote'])
        r = blog.like
        return self.response(data=r)
