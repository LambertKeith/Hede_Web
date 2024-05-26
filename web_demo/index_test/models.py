from django.db import models

# Create your models here.

class TitleParam:
    """抬头的参数类
    """    
    def __init__(self, brand, index, more, contact) -> None:
        
        self.brand_str = brand
        self.index_str = index
        self.more_str = more
        self.contact_str = contact



class HeadParam:
    """head板块的参数类
    """    
    def __init__(self, name, welcome, slogan, main_img) -> None:
        self.name_str = name
        self.welcome_str = welcome
        self.slogan_str = slogan
        self.img_path = main_img
    


class IntroductionParam:
    """公司介绍参数类
    """    
    def __init__(self, img_path, info_dict) -> None:
        self.img_path = img_path
        self.info_dict  = info_dict



class CompetitiveEdgeParam:
    """竞争优势参数类
    """    
    def __init__(self, bg_img, bg_color, competitive_title, competitive_point1, 
                 competitive_point2) -> None:
        self.bg_img = bg_img
        self.bg_color = bg_color
        self.competitive_title = competitive_title
        self.competitive_point1 = competitive_point1
        self.competitive_point2 = competitive_point2



class ContactParam:
    def __init__(self, name, mail, phone, wechet_QR=None) -> None:
        self.name = name
        self.mail = mail
        self.phone = phone