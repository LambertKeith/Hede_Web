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
        introduction_kv1 = {"公司介绍": '''公司创始于2017年，总部坐落于鞋都浙江温州，是一家以鞋为主，集品牌运营、品牌投资、品牌孵化、品牌授权、产品研发、生产销售、电商运营、供应链管理、大数据分析等为一体的集团化公司。赫德鞋服有限公司基于对行业的热爱并深耕，凭借长期夯实的品牌运营经验，整合快速反应的供应链体系、优秀的设计创新能力、团队强大的电商运营能力和长远的品牌发展战略，公司现已拥有或签约数个家喻户晓的国际、国内知名品牌：如Trumppipe/名人烟斗，C.BANNER/千百度，EBLAN/伊伴，Smiley/法国笑脸，Next impulsive/下一个冲动等。我们的理念是坚持做好产品，为客户带来高价值品牌产品的同时，成为正如我们企业名字“赫德”般高尚有品德的企业，推动行业标准化和规范化，引领潮流趋势。'''}
        introduction_kv2 = {
            "管理模型": [
                "强目标化管理：产品小组为模型，以结果为导向，高效率、可执行、可量化",
                "运营小组制：每个小组都是一个小型公司，以老板思维去运营，要对决定负责，更要对结果负责（放权）",
                "小组分红制：使利润透明化，契合现代年轻人对自由、成长的追求，（分钱）",
                "注重多品牌管理：围绕“人、货、场、运营”展开。特别强调人才，因为人是所有生意和事业的本质。"
            ]
        }
        introduction_kv3 = {
            "人才文化": [
                "“人人都要有老板思维”，即每个员工都要有责任心和担当精神，我们相信公司是一个平台，是为员工提供发挥潜力的机会。",
                "注重培养和吸收，特别是年轻人，因为他们代表未来。",
                "强调中层干部要做好榜样，以身作则，知行合一，责任担当。",
                "鼓励员工拥抱新技术，并融入到工作中，提升自我能力，跟上新时代发展。"
            ]
        }
        self.introduction_param_dict["1"] = index_models.IntroductionParam(
                                                'img/demo/test.png',
                                                introduction_kv1
                                            )
        self.introduction_param_dict["2"] = index_models.IntroductionParam(
                                                "img/demo/管理模型.jpg",
                                                introduction_kv2
                                            )
        self.introduction_param_dict["3"] = index_models.IntroductionParam(
                                                "img/demo/人才文化.jpg",
                                                introduction_kv3
                                            )        



class GenerateCompetitiveEdgeParamPackage:
    def __init__(self) -> None:
        
        self.competitive_edge_param_list = []
        self.get_data()
        pass


    def get_data(self):
        
        self.competitive_edge_param_list.append(
            index_models.CompetitiveEdgeParam(
                "img/demo/鞋子设计工作图.JPG", 'overlay-blue', 
                '强目标化管理和运营小组制', "以结果为导向，高效率、可执行、可量化", 
                "每个小组都具备老板思维，对决策和结果负责"
            )
        )

        self.competitive_edge_param_list.append(
            index_models.CompetitiveEdgeParam(
                "img/demo/23年年会.JPG", 'overlay-red', 
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
                "img/demo/ai鞋子设计.png", 'overlay-red', 
                '拥抱新技术', "运用AI技术提高产品展示效果", 
                "增强品牌形象和竞争力"
            )
        )

        self.competitive_edge_param_list.append(
            index_models.CompetitiveEdgeParam(
                "img/demo/渠道-两排堆砌.png", 'overlay-black', 
                '覆盖全渠道的网络销售途径', "在电商平台和社交平台均有涉足", 
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
                "img/demo/开会.JPG", 'overlay-red', 
                '强大精细的运营团队', "超过100名专业团队成员", 
                "杭州分公司将吸纳更多优秀人才"
            )
        )



class GenerateContactParamPackage:
    def __init__(self) -> None:
        self.param = index_models.ContactParam('杨先生', '272228208@qq.com', '13506668301', address='温州瓯海区广川大厦广城国际中心5楼502室', map_img_path='img/demo/地图.png')