from index_test import models as index_models


class GenerateTitleParamPackage:
    """组合抬头参数包
    """    
    def __init__(self):
        self.title_param = self.generate_title_param()


    def generate_title_param(self):
        # 获得数据
        # TODO

        # 生成参数包
        title_param = index_models.TitleParam("HEDE", "主页", '更多', 
                                              '商务联系')
        return title_param



class GenerateHeadParamPackage:
    def __init__(self, ):
        self.head_param = index_models.HeadParam(
            '赫德电商', '欢迎您', '致力于成为鞋服类电商企业领导品牌', 'img/demo/封面展示.jpg'
        )



class GenerateIntroductionParamPackage:
    def __init__(self) -> None:
        self.introduction_param_dict = {}
        introduction_kv1 = {
            "公司介绍": '''公司创始于2017年，总部坐落于鞋都浙江温州，是一家以鞋为主，集品牌运营、品牌投资、品牌孵化、品牌授权、产品研发、生产销售、电商运营、供应链管理、大数据分析等为一体的集团化公司。赫德鞋服有限公司基于对行业的热爱并深耕，凭借长期夯实的品牌运营经验，整合快速反应的供应链体系、优秀的设计创新能力、团队强大的电商运营能力和长远的品牌发展战略，公司现已拥有或签约数个家喻户晓的国际、国内知名品牌：如Trumppipe/名人烟斗，C.BANNER/千百度，EBLAN/伊伴，Smiley/法国笑脸，Next impulsive/下一个冲动等。我们的理念是坚持做好产品，为客户带来高价值品牌产品的同时，成为正如我们企业名字“赫德”般高尚有品德的企业，推动行业标准化和规范化，引领潮流趋势。'''
         }

        pic_list = [
            {
                "number": '0', 
                "path": "/img/demo/公司门口（电梯进）.jpg", 
                "class": "active", 
                "alt": "First slide"
            }, 
            {
                "number": '1', 
                "path": "/img/demo/鞋展柜.jpg", 
                "class": "", 
                "alt": "Second slide"                
            },
            {
                "number": '2', 
                "path": "/img/demo/阳台.jpg", 
                "class": "", 
                "alt": "Second slide"                
            },
            {
                "number": '3', 
                "path": "/img/demo/水池 晚上.jpg", 
                "class": "", 
                "alt": "Second slide"                
            },
            {
                "number": '4', 
                "path": "/img/demo/天幕.jpg", 
                "class": "", 
                "alt": "Second slide"                
            },
        ]

        self.introduction_param_dict["1"] = index_models.IntroductionParam(
                                                'img/demo/公司门头（已修）.jpg',
                                                introduction_kv1,
                                                gallery_list=pic_list, 
                                                business_culture=[
                                                    "强目标化管理：结果导向，高效率、可执行、可量化。",
                                                    "运营小组制：每个小组都是一个小型公司，充分放权，各组以老板思维去运营，对决定、结果负责。",
                                                    "老板思维：每个员工都有责任心和担当精神，充分发挥才能；公司是一个平台，为员工提供发挥潜力的机会。",
                                                    "技术拥抱与自我提升：鼓励员工拥抱新技术，并融入到工作中，提升自我能力，跟上新时代发展。"
                                                ]
                                            )
  



class GenerateCompetitiveEdgeParamPackage:
    def __init__(self) -> None:
        
        self.competitive_edge_param_list = []
        self.get_data()
        pass


    def get_data(self):
        
        self.competitive_edge_param_list.append(
            index_models.CompetitiveEdgeParam(
                "img/demo/鞋子设计工作图 - 副本.JPG", 'overlay-blue', 
                '强目标化管理+运营小组制', "以结果为导向，高效率、可执行、可量化", 
                "每个小组都具备老板思维，对决策和结果负责"
            )
        )

        self.competitive_edge_param_list.append(
            index_models.CompetitiveEdgeParam(
                "img/demo/奖杯.jpg", 'overlay-red', 
                '小组分红制', "利润透明化，激励员工创造力", 
                "契合现代年轻人追求自由、成长的追求"
            )
        )

        self.competitive_edge_param_list.append(
            index_models.CompetitiveEdgeParam(
                "img/demo/品牌背景.png", 'overlay-black', 
                '注重多品牌管理', "利润透明化，激励员工创造力", 
                "契合现代年轻人追求自由、成长的追求"
            )
        )

        self.competitive_edge_param_list.append(
            index_models.CompetitiveEdgeParam(
                "img/demo/老板办公室.jpg", 'overlay-blue', 
                '人才文化', "人人都要有老板思维", 
                "培养年轻人，鼓励拥抱新技术"
            )
        )

        self.competitive_edge_param_list.append(
            index_models.CompetitiveEdgeParam(
                "img/demo/AI制作设计鞋子背景.png", 'overlay-red', 
                '拥抱新技术', "运用AI技术提高产品展示效果", 
                "增强品牌形象和竞争力"
            )
        )

        self.competitive_edge_param_list.append(
            index_models.CompetitiveEdgeParam(
                "img/demo/渠道-两排堆砌.png", 'overlay-black', 
                '网络销售全渠道覆盖', "在电商平台和社交平台均有涉足", 
                "实现了行业前十的业绩"
            )
        )

        self.competitive_edge_param_list.append(
            index_models.CompetitiveEdgeParam(
                "img/demo/办公室1.jpg", 'overlay-blue', 
                '全面完善的内部数据分析系统', "精准分析各品牌和平台数据", 
                "制定有效的销售方案和策略"
            )
        )

        self.competitive_edge_param_list.append(
            index_models.CompetitiveEdgeParam(
                "img/demo/大厅工作照.jpg", 'overlay-red', 
                '强大精细的运营团队', "超过100名专业团队成员", 
                "杭州分公司将吸纳更多优秀人才"
            )
        )



class GenerateContactParamPackage:
    def __init__(self) -> None:
        self.param = index_models.ContactParam(
            '联系人：杨总', '邮箱：272228208@qq.com', '电话：13506668301', 
            address='地址：温州瓯海区广川大厦广城国际中心5楼502室', map_img_path='img/demo/地图.png'
        )
        
        try:

            self.param_dict = {
                "text_list": [
                    self.param.name,
                    self.param.mail,
                    self.param.phone,
                    self.param.address
                ],
                "img": self.param.map_img_path
            }
            print("param_dict", self.param_dict)
        except:
            print("param_dict error")
            pass
       