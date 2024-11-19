import {ref} from 'vue'

interface Header {
  key: string
  title: string
  align?: 'start' | 'center' | 'end'
  sortable?: boolean
  value?: string // 用于标识字段名称，可能替代 key
}

export const headers: Header[] = [
  {
    align: 'start',
    key: 'login',
    sortable: false,
    title: '中国开发者(前100名)',
  },
  {key: 'name', title: '网名'},
  {key: 'location', title: '位置信息'},
  {key: 'followers', title: '追随者数量'},
  {key: 'repositories', title: '仓库数量'},
  {key: 'score', title: '评分'},

];

interface Dessert {
  login: string
  name: string
  location: string
  followers: number
  repositories: number
  score: number

}

export const desserts = ref<Dessert[]>([
  {
    login: 'ruanyf',
    name: 'Ruan YiFeng',
    location: 'Shanghai, China',
    followers: 79335,
    repositories: 75,
    score: 206847.39
  },
  {
    login: 'vinta',
    name: 'Vinta Chen',
    location: 'Taiwan',
    followers: 7909,
    repositories: 23,
    score: 191788.47000000003
  },
  {
    login: 'justjavac',
    name: '迷渡',
    location: 'Tianjin, China',
    followers: 16931,
    repositories: 381,
    score: 168563.5299999992
  },
  {login: 'CyC2018', name: 'nan', location: 'Guangzhou, China', followers: 14577, repositories: 7, score: 161214.8},
  {
    login: 'jackfrued',
    name: '骆昊',
    location: 'Chengdu Sichuan, China',
    followers: 15627,
    repositories: 125,
    score: 152054.63999999998
  },
  {login: 'Snailclimb', name: 'Guide', location: 'Wuhan, Hubei', followers: 10440, repositories: 24, score: 149429.33},
  {
    login: 'jaywcjlove',
    name: '小弟调调',
    location: 'Suzhou, China',
    followers: 7928,
    repositories: 209,
    score: 141315.04
  },
  {
    login: 'appleboy',
    name: 'Bo-Yi Wu',
    location: 'Hsinchu, Taiwan',
    followers: 6803,
    repositories: 593,
    score: 118710.87000000024
  },
  {
    login: '521xueweihan',
    name: '削微寒',
    location: 'Beijing, China',
    followers: 9006,
    repositories: 150,
    score: 117286.8400000001
  },
  {login: 'macrozheng', name: 'macro', location: 'Wuxi,China', followers: 8952, repositories: 19, score: 107988.75},
  {
    login: 'PanJiaChen',
    name: '花裤衩',
    location: 'Shanghai, China',
    followers: 13081,
    repositories: 73,
    score: 105719.62
  },
  {login: 'peng-zhihui', name: '稚晖', location: 'Shanghai', followers: 80762, repositories: 61, score: 104709.4},
  {login: 'egoist', name: 'EGOIST', location: 'China', followers: 12315, repositories: 847, score: 90844.29000000002},
  {
    login: 'phodal',
    name: 'Fengda Huang',
    location: 'Shanghai / Hangzhou, China',
    followers: 20066,
    repositories: 495,
    score: 90509.64000000012
  },
  {login: 'krahets', name: 'Yudong Jin', location: 'Shanghai', followers: 5136, repositories: 11, score: 88742.7},
  {
    login: 'astaxie',
    name: 'astaxie',
    location: 'Shanghai, China',
    followers: 14997,
    repositories: 81,
    score: 84226.90000000004
  },
  {
    login: 'bailicangdu',
    name: 'cangdu',
    location: 'Shanghai, China',
    followers: 13694,
    repositories: 23,
    score: 82879.31
  },
  {
    login: 'sorrycc',
    name: 'chencheng (云谦)',
    location: 'HangZhou, China',
    followers: 14390,
    repositories: 253,
    score: 80683.86000000007
  },
  {
    login: 'easychen',
    name: 'Easy',
    location: 'Chongqing, China',
    followers: 9907,
    repositories: 225,
    score: 79527.71000000004
  },
  {
    login: 'fengdu78',
    name: 'Huang Haiguang',
    location: 'Qingdao,China',
    followers: 13256,
    repositories: 17,
    score: 78557.92000000001
  },
  {
    login: 'MisterBooo',
    name: '吴师兄学算法',
    location: 'Guangzhou, China',
    followers: 8745,
    repositories: 88,
    score: 72452.5
  },
  {login: 'Yidadaa', name: 'Yifei Zhang', location: 'China', followers: 5157, repositories: 61, score: 66883.77},
  {login: 'YunaiV', name: '芋道源码', location: 'Shanghai, China', followers: 11718, repositories: 86, score: 65967.74},
  {
    login: 'daimajia',
    name: '代码家',
    location: 'Beijing, China',
    followers: 24631,
    repositories: 90,
    score: 61797.24000000004
  },
  {
    login: 'PKUFlyingPig',
    name: 'Yinmin Zhong',
    location: 'Beijing, China',
    followers: 7424,
    repositories: 87,
    score: 60572.060000000005
  },
  {
    login: 'youngyangyang04',
    name: '程序员Carl',
    location: 'Shenzhen',
    followers: 7408,
    repositories: 48,
    score: 57037.92999999999
  },
  {
    login: 'halfrost',
    name: 'halfrost',
    location: '[California, Singapore, China]',
    followers: 17044,
    repositories: 81,
    score: 56700.28999999999
  },
  {
    login: 'xiaolai',
    name: 'xiaolai',
    location: 'beijing',
    followers: 19268,
    repositories: 56,
    score: 54688.12999999999
  },
  {login: 'amusi', name: 'Amusi', location: 'Shanghai, China', followers: 6779, repositories: 255, score: 54496.44},
  {
    login: 'michaelliao',
    name: 'Crypto Michael',
    location: 'Beijing, China',
    followers: 37262,
    repositories: 100,
    score: 54058.52000000001
  },
  {login: 'programthink', name: '编程随想', location: 'China', followers: 21390, repositories: 5, score: 52961.4},
  {
    login: 'azl397985856',
    name: 'lucifer',
    location: 'China',
    followers: 4620,
    repositories: 148,
    score: 51952.630000000034
  },
  {login: 'skywind3000', name: 'Linwei', location: 'PRC', followers: 6554, repositories: 152, score: 50686.81000000001},
  {
    login: 'oldratlee',
    name: '李鼎',
    location: 'Shanghai ⇌ Hangzhou Zhejiang, China',
    followers: 6976,
    repositories: 63,
    score: 50454.81000000001
  },
  {
    login: 'Trinea',
    name: 'Trinea',
    location: 'HangZhou',
    followers: 17004,
    repositories: 24,
    score: 49546.310000000005
  },
  {
    login: 'hongyangAndroid',
    name: '张鸿洋',
    location: 'Beijing,China',
    followers: 12988,
    repositories: 102,
    score: 48559.690000000046
  },
  {login: 'CarGuo', name: 'Shuyu Guo', location: 'China 广东 珠海', followers: 7632, repositories: 57, score: 48547.23},
  {
    login: 'ityouknow',
    name: '纯洁的微笑',
    location: 'beijing,china',
    followers: 8779,
    repositories: 30,
    score: 47180.2
  },
  {login: 'Blankj', name: 'Blankj', location: 'Hangzhou', followers: 4759, repositories: 44, score: 46730.99999999999},
  {
    login: 'miloyip',
    name: 'Milo Yip',
    location: 'Hong Kong, China',
    followers: 10589,
    repositories: 32,
    score: 46328.070000000014
  },
  {
    login: 'jinzhu',
    name: 'Jinzhu',
    location: 'HangZhou China',
    followers: 5375,
    repositories: 111,
    score: 46278.73000000004
  },
  {login: 'liyupi', name: '程序员鱼皮', location: 'China Shanghai', followers: 17417, repositories: 83, score: 45749.7},
  {login: 'cloudwu', name: '云风', location: 'China', followers: 20977, repositories: 135, score: 44038.32999999999},
  {
    login: 'JacksonTian',
    name: 'Jackson Tian',
    location: 'Hangzhou, China',
    followers: 21203,
    repositories: 285,
    score: 43867.83999999996
  },
  {login: 'haoel', name: 'Hao Chen', location: 'Beijing', followers: 12629, repositories: 29, score: 43058.37},
  {
    login: 'tw93',
    name: 'Tw93',
    location: 'HangZhou, China',
    followers: 5408,
    repositories: 30,
    score: 42703.180000000015
  },
  {
    login: 'huacnlee',
    name: 'Jason Lee',
    location: 'Chengdu, China',
    followers: 4955,
    repositories: 194,
    score: 42162.00000000003
  },
  {
    login: 'crossoverJie',
    name: 'crossoverJie',
    location: 'CHONGQING,CHINA',
    followers: 5603,
    repositories: 138,
    score: 40310.68000000002
  },
  {
    login: 'overtrue',
    name: '安正超',
    location: 'Shenzhen,China',
    followers: 7111,
    repositories: 110,
    score: 39679.91999999999
  },
  {login: 'lenve', name: '江南一点雨', location: 'China GuangZhou', followers: 4559, repositories: 90, score: 39476.4},
  {
    login: 'hehonghui',
    name: 'Mr.Simple',
    location: 'china',
    followers: 6944,
    repositories: 291,
    score: 38591.49999999999
  },
  {
    login: 'chokcoco',
    name: 'Coco',
    location: 'ShenZhen, China',
    followers: 8246,
    repositories: 67,
    score: 37916.69999999998
  },
  {
    login: 'yihong0618',
    name: 'yihong',
    location: 'China',
    followers: 5627,
    repositories: 109,
    score: 37759.11000000001
  },
  {
    login: 'mqyqingfeng',
    name: '冴羽',
    location: 'Hangzhou, China',
    followers: 11310,
    repositories: 33,
    score: 37611.00000000001
  },
  {
    login: 'QianMo',
    name: '浅墨（毛星云）',
    location: 'Shenzhen, China',
    followers: 11012,
    repositories: 37,
    score: 37349.50000000001
  },
  {
    login: 'YunYouJun',
    name: '云游君',
    location: 'Guangzhou, China',
    followers: 4569,
    repositories: 228,
    score: 37275.03999999999
  },
  {login: 'nihui', name: 'nan', location: 'Shanghai', followers: 7193, repositories: 185, score: 36355.54999999995},
  {
    login: 'chai2010',
    name: 'chai2010',
    location: 'Hangzhou, China',
    followers: 4852,
    repositories: 294,
    score: 35961.59999999999
  },
  {
    login: 'mercyblitz',
    name: 'Mercy Ma',
    location: 'Hangzhou, China',
    followers: 8065,
    repositories: 56,
    score: 35415.48999999999
  },
  {login: 'ustbhuangyi', name: 'HuangYi', location: 'HeFei,China', followers: 9631, repositories: 79, score: 33959.22},
  {login: 'fouber', name: '张云龙', location: 'China', followers: 11272, repositories: 182, score: 33557.21999999999},
  {
    login: 'xuxueli',
    name: '许雪里',
    location: 'Shanghai, China',
    followers: 5611,
    repositories: 12,
    score: 32598.200000000004
  },
  {
    login: 'Jack-Cherish',
    name: 'Jack Cui',
    location: 'China',
    followers: 9426,
    repositories: 18,
    score: 32159.680000000004
  },
  {
    login: 'CoderMJLee',
    name: 'M了个J',
    location: 'Guangzhou, China',
    followers: 9805,
    repositories: 16,
    score: 31706.6
  },
  {
    login: 'dyc87112',
    name: '程序猿DD',
    location: 'Shanghai, China',
    followers: 9079,
    repositories: 62,
    score: 31282.34
  },
  {
    login: 'fuzhengwei',
    name: '小傅哥',
    location: '北京市亦庄经济技术开发区',
    followers: 5860,
    repositories: 196,
    score: 30498.989999999965
  },
  {login: 'muan', name: 'Mu-An Chiou', location: 'Taipei', followers: 11232, repositories: 180, score: 29780.7},
  {
    login: 'i5ting',
    name: '狼叔',
    location: 'china beijing',
    followers: 9081,
    repositories: 951,
    score: 29300.449999999983
  },
  {
    login: 'skyzh',
    name: 'Alex Chi Z.',
    location: 'Pittsburgh, PA, USA ⇌ Shanghai, China',
    followers: 7257,
    repositories: 237,
    score: 29083.46999999999
  },
  {login: 'RubyLouvre', name: '司徒正美', location: 'China', followers: 14737, repositories: 131, score: 26526.52},
  {login: 'tiann', name: 'weishu', location: 'China', followers: 6912, repositories: 128, score: 26461.64},
  {
    login: 'atian25',
    name: 'TZ | 天猪',
    location: 'GuangZhou, China',
    followers: 4832,
    repositories: 124,
    score: 26227.469999999983
  },
  {
    login: 'jindongwang',
    name: 'Jindong Wang',
    location: 'Beijing, China',
    followers: 5016,
    repositories: 68,
    score: 25862.5
  },
  {
    login: 'smallnest',
    name: 'smallnest',
    location: 'China',
    followers: 4703,
    repositories: 230,
    score: 24203.469999999983
  },
  {login: 'liaohuqiu', name: 'Huqiu Liao', location: 'Hangzhou', followers: 8308, repositories: 125, score: 24143.81},
  {
    login: 'liuhuanyong',
    name: 'liuhuanyong',
    location: 'Beijing, China',
    followers: 5863,
    repositories: 73,
    score: 23484.200000000008
  },
  {login: 'guolindev', name: 'Lin Guo', location: 'Suzhou, China', followers: 5876, repositories: 17, score: 23364.84},
  {
    login: 'Ovilia',
    name: 'Wenli Zhang',
    location: 'Shanghai, China',
    followers: 15567,
    repositories: 79,
    score: 22886.47
  },
  {login: 'julycoding', name: 'July', location: 'Beijing, China', followers: 5109, repositories: 7, score: 22617.54},
  {
    login: 'singwhatiwanna',
    name: 'singwhatiwanna',
    location: 'Beijing, China',
    followers: 7344,
    repositories: 27,
    score: 21600.76
  },
  {
    login: 'stormzhang',
    name: 'stormzhang',
    location: 'Shanghai, China',
    followers: 15879,
    repositories: 5,
    score: 21497.94
  },
  {
    login: 'gaoxiang12',
    name: 'Xiang Gao',
    location: 'zhiyuan-robotics.com, Beijing',
    followers: 6155,
    repositories: 51,
    score: 21251.12
  },
  {
    login: 'alsotang',
    name: 'alsotang',
    location: 'ShenZhen, China',
    followers: 5228,
    repositories: 214,
    score: 21234.459999999985
  },
  {
    login: 'huangzworks',
    name: '宏图书社 | 黄健宏',
    location: 'China',
    followers: 5120,
    repositories: 48,
    score: 21092.230000000003
  },
  {login: 'sofish', name: '小鱼', location: 'Shanghai China', followers: 10485, repositories: 42, score: 20914.55},
  {
    login: 'hellokaton',
    name: '見える',
    location: 'ShangHai, China',
    followers: 4877,
    repositories: 96,
    score: 19909.37
  },
  {
    login: 'wx-chevalier',
    name: '王下邀月熊',
    location: 'Shanghai',
    followers: 5220,
    repositories: 157,
    score: 19507.800000000003
  },
  {
    login: 'fengmk2',
    name: 'fengmk2',
    location: 'Hangzhou, China',
    followers: 8120,
    repositories: 243,
    score: 19144.56999999998
  },
  {login: 'teddysun', name: 'Teddysun', location: 'Shanghai', followers: 4909, repositories: 8, score: 18467.0},
  {login: 'draveness', name: 'Draven', location: 'Beijing, China', followers: 13012, repositories: 90, score: 17910.93},
  {
    login: 'wizardforcel',
    name: '布客飞龙',
    location: 'Beijing, China',
    followers: 9612,
    repositories: 772,
    score: 17785.880000000012
  },
  {
    login: 'afc163',
    name: 'afc163',
    location: 'Hangzhou, China',
    followers: 7064,
    repositories: 277,
    score: 17713.659999999978
  },
  {
    login: 'rengwuxian',
    name: 'Kai Zhu',
    location: 'Zhengzhou, China',
    followers: 7959,
    repositories: 65,
    score: 17262.299999999992
  },
  {
    login: 'TommyZihao',
    name: 'Tommy in Tongji',
    location: 'Shanghai',
    followers: 6298,
    repositories: 129,
    score: 16819.280000000006
  },
  {
    login: 'drakeet',
    name: 'Drakeet',
    location: 'Suzhou, China',
    followers: 7969,
    repositories: 25,
    score: 16692.969999999998
  },
  {login: 'audreyt', name: '唐鳳', location: 'Taiwan', followers: 8677, repositories: 390, score: 16584.140000000014},
  {
    login: 'bigtreetech',
    name: 'BIGTREETECH',
    location: 'Shenzhen, China',
    followers: 6667,
    repositories: 139,
    score: 16265.080000000004
  },
  {login: 'breakwa11', name: '破娃酱', location: '喵嗷污, China', followers: 13201, repositories: 8, score: 16172.6},
  {
    login: 'lifesinger',
    name: 'lifesinger',
    location: 'Hangzhou, China',
    followers: 15869,
    repositories: 3,
    score: 15875.0
  },
  {login: 'coderwhy', name: 'nan', location: 'guangzhou', followers: 6294, repositories: 33, score: 15472.520000000002},
].map(dessert =>({
  ...dessert,
  score: parseFloat(dessert.score.toFixed(2))
})));

export function navigateToProfile(login: string): void {
  const url = `https://github.com/${login}`;
  window.open(url, '_blank');  // 在新标签页中打开 GitHub 用户主页
}
