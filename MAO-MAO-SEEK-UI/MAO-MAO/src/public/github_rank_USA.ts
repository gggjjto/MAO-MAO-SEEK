import {ref} from "vue";


interface Header {
  key: string
  title: string
  align?: 'start' | 'center' | 'end'
  sortable?: boolean
  value?: string // 用于标识字段名称，可能替代 key
}

export const USA_headers: Header[] = [
  {
    align: 'start',
    key: 'login',
    sortable: false,
    title: '美国开发者(前100名)',
  },
  { key: 'name', title: '网名' },
  { key: 'location', title: '位置信息' },
  { key: 'followers', title: '追随者数量' },
  { key: 'repositories', title: '仓库数量' },
  { key: 'score', title: '评分' },
];

interface Dessert {
  login: string
  name: string
  location: string
  followers: number
  repositories: number
  score: number
}

export const USA_desserts = ref<Dessert[]>([
  { login: 'JakeWharton', name: 'Jake Wharton', location: 'Pittsburgh, PA, USA', followers: 67641, repositories: 206, score: 363453.4799999998 },
  { login: 'donnemartin', name: 'Donne Martin', location: 'Washington, D.C.', followers: 21093, repositories: 29, score: 333373.54000000004 },
  { login: 'torvalds', name: 'Linus Torvalds', location: 'Portland, OR', followers: 219610, repositories: 31, score: 318117.78 },
  { login: 'jwasham', name: 'John Washam', location: 'United States', followers: 23676, repositories: 30, score: 280124.47000000003 },
  { login: 'karpathy', name: 'Andrej', location: 'Stanford', followers: 91536, repositories: 59, score: 274072.21 },
  { login: 'getify', name: 'Kyle Simpson', location: 'Austin, TX', followers: 43936, repositories: 71, score: 212737.41 },
  { login: 'bradtraversy', name: 'Brad Traversy', location: 'Massachusetts', followers: 72334, repositories: 290, score: 204485.24999999997 },
  { login: 'acdlite', name: 'Andrew Clark', location: 'New York', followers: 14235, repositories: 87, score: 200565.94 },
  { login: 'sebmarkbage', name: 'Sebastian Markbåge', location: 'New York City', followers: 8822, repositories: 83, score: 197317.55999999988 },
  { login: 'jaredpalmer', name: 'Jared Palmer', location: 'New York, NY', followers: 9459, repositories: 216, score: 176299.10000000006 },
  { login: 'lucidrains', name: 'Phil Wang', location: 'San Francisco', followers: 41421, repositories: 315, score: 171514.97000000003 },
  { login: 'DanWahlin', name: 'Dan Wahlin', location: 'Arizona', followers: 4959, repositories: 147, score: 167717.77 },
  { login: 'addyosmani', name: 'Addy Osmani', location: 'Mountain View, California', followers: 43081, repositories: 374, score: 167172.84999999998 },
  { login: 'kentcdodds', name: 'Kent C. Dodds', location: 'Salt Lake City, Utah, USA', followers: 33315, repositories: 790, score: 142445.88999999972 },
  { login: 'kelseyhightower', name: 'Kelsey Hightower', location: 'Portland, OR', followers: 22346, repositories: 241, score: 138441.15999999997 },
  { login: 'rasbt', name: 'Sebastian Raschka', location: 'Madison, WI', followers: 24766, repositories: 159, score: 130497.02000000002 },
  { login: 'tpope', name: 'Tim Pope', location: 'Brooklyn, NY', followers: 21657, repositories: 90, score: 111509.61000000002 },
  { login: 'mgechev', name: 'Minko Gechev', location: 'California', followers: 9888, repositories: 404, score: 97324.63000000008 },
  { login: 'jakevdp', name: 'Jake Vanderplas', location: 'Oakland CA', followers: 17753, repositories: 286, score: 95740.35000000008 },
  { login: 'robbyrussell', name: 'Robby Russell', location: 'Portland, Oregon USA', followers: 4717, repositories: 71, score: 93963.57999999991 },
  { login: 'spf13', name: 'Steve Francia', location: 'NYC', followers: 15318, repositories: 113, score: 91913.99000000003 },
  { login: 'hadley', name: 'Hadley Wickham', location: 'Houston, TX', followers: 25840, repositories: 357, score: 78966.80000000005 },
  { login: 'swyxio', name: 'swyx.io', location: 'San Francisco', followers: 6720, repositories: 722, score: 76040.16000000024 },
  { login: 'leerob', name: 'Lee Robinson', location: 'Des Moines, IA', followers: 12689, repositories: 89, score: 70914.28000000001 },
  { login: 'geerlingguy', name: 'Jeff Geerling', location: 'St. Louis, MO', followers: 21284, repositories: 297, score: 70525.56000000003 },
  { login: 'ardalis', name: 'Steve Smith', location: 'Ohio', followers: 8712, repositories: 294, score: 69533.90000000004 },
  { login: 'junyanz', name: 'Jun-Yan Zhu', location: 'Pittsburgh, PA', followers: 6744, repositories: 64, score: 69422.01000000001 },
  { login: 'alex', name: 'Alex Gaynor', location: 'Washington D.C.', followers: 9960, repositories: 497, score: 69093.81000000035 },
  { login: 'bvaughn', name: 'Brian Vaughn', location: 'Brooklyn, NY', followers: 11179, repositories: 183, score: 68378.74999999999 },
  { login: 'jxnblk', name: 'Brent Jackson', location: 'New York City', followers: 6024, repositories: 289, score: 57685.96 },
  { login: 'dtolnay', name: 'David Tolnay', location: 'Redwood City, California', followers: 8021, repositories: 123, score: 56802.16 },
  { login: 'dabit3', name: 'Nader Dabit', location: 'Madison, Mississippi', followers: 7257, repositories: 458, score: 55859.40000000008 },
  { login: 'isaacs', name: 'isaacs', location: 'Oakland CA', followers: 15169, repositories: 507, score: 55817.35000000004 },
  { login: 'kdn251', name: 'Kevin Naughton Jr.', location: 'New York, New York', followers: 4548, repositories: 23, score: 54980.3 },
  { login: 'creationix', name: 'Tim Caswell', location: 'Mountainburg, AR, USA', followers: 5139, repositories: 534, score: 54933.89000000005 },
  { login: 'zenorocha', name: 'Zeno Rocha', location: 'San Francisco, California', followers: 10974, repositories: 188, score: 54798.570000000014 },
  { login: 'poteto', name: 'lauren', location: 'nyc', followers: 5700, repositories: 96, score: 54576.67000000003 },
  { login: 'andrewrk', name: 'Andrew Kelley', location: 'Portland, Oregon', followers: 7603, repositories: 269, score: 54358.79999999999 },
  { login: 'benawad', name: 'Ben Awad', location: 'Austin, TX', followers: 29014, repositories: 264, score: 53870.73999999999 },
  { login: 'jashkenas', name: 'Jeremy Ashkenas', location: 'Berkeley', followers: 13244, repositories: 26, score: 53325.15 },
  { login: 'Rich-Harris', name: 'Rich Harris', location: 'NYC', followers: 19234, repositories: 403, score: 53134.27999999996 },
  { login: 'WebDevSimplified', name: 'nan', location: 'Nebraska', followers: 30334, repositories: 207, score: 49841.19 },
  { login: 'soumith', name: 'Soumith Chintala', location: 'New York, USA', followers: 12200, repositories: 212, score: 48936.53 },
  { login: 'lattner', name: 'Chris Lattner', location: 'Bay Area, California, USA', followers: 10288, repositories: 17, score: 47930.73 },
  { login: 'wycats', name: 'Yehuda Katz', location: 'Portland, OR', followers: 10228, repositories: 397, score: 46931.470000000016 },
  { login: 'markerikson', name: 'Mark Erikson', location: 'OH, USA', followers: 5710, repositories: 97, score: 46245.280000000006 },
  { login: 'jhaddix', name: 'Jason Haddix', location: 'United States', followers: 10246, repositories: 72, score: 45501.52999999998 },
  { login: 'gvanrossum', name: 'Guido van Rossum', location: 'San Francisco Bay Area', followers: 23293, repositories: 54, score: 44955.12000000001 },
  { login: 'leebyron', name: 'Lee Byron', location: 'San Francisco', followers: 5211, repositories: 120, score: 44949.02 },
  { login: 'mattt', name: 'Mattt', location: 'Portland, OR', followers: 18023, repositories: 103, score: 44867.86 },
  { login: 'mjackson', name: 'Michael Jackson', location: 'Carlsbad, California', followers: 7089, repositories: 205, score: 44191.56999999999 },
  { login: 'minimaxir', name: 'Max Woolf', location: 'San Francisco', followers: 4650, repositories: 144, score: 44101.47999999998 },
  { login: 'evanw', name: 'Evan Wallace', location: 'San Francisco', followers: 12526, repositories: 129, score: 43340.92999999999 },
  { login: 'chiphuyen', name: 'Chip Huyen', location: 'San Francisco', followers: 15331, repositories: 36, score: 42510.73 },
  { login: 'wesm', name: 'Wes McKinney', location: 'Nashville, TN', followers: 14758, repositories: 147, score: 42322.40999999997 },
  { login: 'ahejlsberg', name: 'Anders Hejlsberg', location: 'Redmond, WA, USA', followers: 14302, repositories: 7, score: 41486.07 },
  { login: 'rsms', name: 'Rasmus', location: 'San Francisco', followers: 7224, repositories: 182, score: 40572.36 },
  { login: 'norvig', name: 'Peter Norvig', location: 'Palo Alto, CA, USA', followers: 9284, repositories: 6, score: 39857.58 },
  { login: 'rauchg', name: 'Guillermo Rauch', location: 'SF', followers: 14939, repositories: 181, score: 39613.04 },
  { login: 'calebporzio', name: 'Caleb Porzio', location: 'Buffalo NY', followers: 5106, repositories: 97, score: 39501.64999999999 },
  { login: 'mojombo', name: 'Tom Preston-Werner', location: 'San Francisco', followers: 24054, repositories: 88, score: 38630.24 },
  { login: 'chenglou', name: 'Cheng Lou', location: 'California', followers: 5867, repositories: 208, score: 37917.76 },
  { login: 'romainguy', name: 'Romain Guy', location: 'California', followers: 10095, repositories: 21, score: 37631.350000000006 },
  { login: 'rs', name: 'Olivier Poitrey', location: 'Silicon Valley, California, USA', followers: 4694, repositories: 122, score: 36433.60999999998 },
  { login: 'charliermarsh', name: 'Charlie Marsh', location: 'Brooklyn, NY', followers: 5075, repositories: 65, score: 36093.41999999999 },
  { login: 'shanselman', name: 'Scott Hanselman', location: 'Portland, OR', followers: 11315, repositories: 240, score: 36010.04000000001 },
  { login: 'ry', name: 'Ryan Dahl', location: 'New York City', followers: 31863, repositories: 69, score: 35112.340000000004 },
  { login: 'buckyroberts', name: 'Bucky Roberts', location: 'New York, NY', followers: 27286, repositories: 61, score: 35096.130000000005 },
  { login: 'nat', name: 'Nat Friedman', location: 'San Francisco', followers: 6741, repositories: 20, score: 34754.6 },
  { login: 'douglascrockford', name: 'Douglas Crockford', location: 'Anaheim', followers: 21739, repositories: 18, score: 34524.29 },
  { login: 'afollestad', name: 'Aidan Follestad', location: 'St. Paul, Minnesota', followers: 5426, repositories: 34, score: 33971.6 },
  { login: 'fogleman', name: 'Michael Fogleman', location: 'Cary, NC', followers: 5477, repositories: 144, score: 33754.69 },
  { login: 'felixrieseberg', name: 'Felix Rieseberg', location: 'San Francisco', followers: 4687, repositories: 269, score: 32754.22 },
  { login: 'shiffman', name: 'Daniel Shiffman', location: 'New York, NY', followers: 19266, repositories: 255, score: 32668.93 },
  { login: 'kenwheeler', name: 'Ken Wheeler', location: 'Jersey Shore', followers: 5226, repositories: 123, score: 32371.259999999984 },
  { login: 'octocat', name: 'The Octocat', location: 'San Francisco', followers: 15563, repositories: 203, score: 31533.45 },
  { login: 'dmalan', name: 'David J. Malan', location: 'Cambridge, MA, USA', followers: 30623, repositories: 31, score: 31103.46 },
  { login: 'igrigorik', name: 'Ilya Grigorik', location: 'Portland, OR', followers: 8766, repositories: 95, score: 30904.469999999998 },
  { login: 'ChrisTitusTech', name: 'Chris Titus', location: 'Dallas, TX', followers: 10300, repositories: 58, score: 29770.980000000003 },
  { login: 'codingforentrepreneurs', name: 'Coding For Entrepreneurs', location: 'Boise, Idaho', followers: 16381, repositories: 206, score: 29546.800000000003 },
  { login: 'tenderlove', name: 'Aaron Patterson', location: 'Seattle', followers: 9448, repositories: 413, score: 29508.079999999994 },
  { login: 'steven-tey', name: 'Steven Tey', location: 'SF', followers: 5254, repositories: 105, score: 28708.83 },
  { login: 'bradfitz', name: 'Brad Fitzpatrick', location: 'Seattle', followers: 12109, repositories: 166, score: 28341.94000000001 },
  { login: 'loiane', name: 'Loiane Groner', location: 'Florida, US', followers: 18420, repositories: 358, score: 28332.76000000001 },
  { login: 'jbogard', name: 'Jimmy Bogard', location: 'Austin, TX', followers: 5945, repositories: 141, score: 28265.40999999999 },
  { login: 'ryanb', name: 'Ryan Bates', location: 'Southern Oregon', followers: 7717, repositories: 80, score: 28109.34 },
  { login: 'AllenDowney', name: 'Allen Downey', location: 'Needham, MA, USA', followers: 9814, repositories: 369, score: 27756.249999999964 },
  { login: 'jeresig', name: 'John Resig', location: 'Hudson Valley, NY', followers: 18744, repositories: 119, score: 27660.56 },
  { login: 'vczh', name: 'nan', location: 'Seattle, WA, USA', followers: 17513, repositories: 19, score: 27658.38 },
  { login: 'gamemann', name: 'Christian Deacon', location: 'Mullica Hill, New Jersey, US', followers: 24663, repositories: 161, score: 27168.34 },
  { login: 'Nutlope', name: 'Hassan El Mghari', location: 'New York City, NY', followers: 4958, repositories: 77, score: 27017.400000000005 },
  { login: 'samyk', name: 'samy kamkar', location: 'los angeles', followers: 11020, repositories: 185, score: 26814.22 },
  { login: 'cassidoo', name: 'Cassidy Williams', location: 'Chicago, IL', followers: 13385, repositories: 188, score: 26079.61 },
  { login: 'eliben', name: 'Eli Bendersky', location: 'California', followers: 5511, repositories: 78, score: 25269.04 },
  { login: 'mxcl', name: 'Max Howell', location: 'Apex, NC, USA', followers: 7365, repositories: 64, score: 24403.489999999994 },
  { login: 'holman', name: 'Zach Holman', location: 'San Francisco', followers: 6382, repositories: 68, score: 23864.56 },
  { login: 'btholt', name: 'Brian Holt', location: 'MSP 🔜 SNA 🔜 SLC 🔜 SMF', followers: 12488, repositories: 167, score: 23855.36000000001 },
  { login: 'anvaka', name: 'Andrei Kashcha', location: 'Seattle ', followers: 4798, repositories: 320, score: 23615.76000000001 },
  { login: 'amueller', name: 'Andreas Mueller', location: 'Los Gatos', followers: 10731, repositories: 217, score: 23438.550000000017 },
  { login: 'jamesmontemagno', name: 'James Montemagno', location: 'Pacific Northwest', followers: 8075, repositories: 405, score: 23380.389999999985 },
].map(dessert => ({
  ...dessert,
  score: parseFloat(dessert.score.toFixed(2))
})));
