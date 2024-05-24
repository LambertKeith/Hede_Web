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
            '赫德鞋服', '欢迎您', '致力于成为鞋服类电商领导品牌', 'img/demo/test.png'
        )



class GenerateIntroductionParamPackage:
    def __init__(self) -> None:
        self.introduction_param_dict = {}
        introduction_kv1 = {"公司介绍": '''公司创始于2017年，总部坐落于鞋都浙江温州，系一家以鞋为主，集品牌运营、品牌投资、品牌孵化、品牌授权、产品研发、生产销售、电商运营、供应链管理、大数据分析等为一体的集团化公司。赫德鞋服有限公司基于对行业的热爱并深耕，凭借长期夯实的品牌运营经验，整合快速反应的供应链体系、优秀的设计创新能力、团队强大的电商运营能力和长远的品牌发展战略，公司现已拥有或签约数个家喻户晓的国际、国内知名品牌：如Trumppipe/名人烟斗，C.BANNER/千百度，EBLAN/伊伴，Smiley/法国笑脸，Next impulsive/下一个冲动等。我们的理念是坚持做好产品，为客户带来高价值品牌产品的同时，成为正如我们企业名字“赫德”般高尚有品德的企业，推动行业标准化和规范化，引领潮流趋势。'''}
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
                                                "img/demo/公司门头2.jpg",
                                                introduction_kv1
                                            )
        self.introduction_param_dict["2"] = index_models.IntroductionParam(
                                                "img/demo/天幕.jpg",
                                                introduction_kv2
                                            )
        self.introduction_param_dict["3"] = index_models.IntroductionParam(
                                                "img/demo/水池 晚上.jpg",
                                                introduction_kv3
                                            )        



