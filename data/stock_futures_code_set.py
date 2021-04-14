code_pair_list = [
    # 현물코드, 선물코드, 시장, 이름
    ['005930', '111', 'KOSPI', '삼성전자'],
    ['017670', '112', 'KOSPI', 'SK텔레콤'],
    ['005490', '113', 'KOSPI', 'POSCO'],
    ['030200', '114', 'KOSPI', 'KT'],
    ['015760', '115', 'KOSPI', '한국전력'],
    ['005380', '116', 'KOSPI', '현대차'],
    ['016360', '117', 'KOSPI', '삼성증권'],
    ['055550', '118', 'KOSPI', '신한지주'],
    ['000270', '119', 'KOSPI', '기아차'],
    ['012330', '120', 'KOSPI', '현대모비스'],
    ['006400', '122', 'KOSPI', '삼성SDI'],
    ['009150', '123', 'KOSPI', '삼성전기'],
    ['066570', '124', 'KOSPI', 'LG전자'],
    ['036460', '128', 'KOSPI', '한국가스공사'],
    ['004020', '132', 'KOSPI', '현대제철'],
    ['003550', '134', 'KOSPI', 'LG'],
    ['078930', '135', 'KOSPI', 'GS'],
    ['033780', '136', 'KOSPI', 'KT&G'],
    ['009540', '139', 'KOSPI', '한국조선해양'],
    ['086790', '140', 'KOSPI', '하나금융지주'],
    ['096770', '141', 'KOSPI', 'SK이노베이션'],
    ['001040', '142', 'KOSPI', 'CJ'],
    ['034220', '145', 'KOSPI', 'LG디스플레이'],
    ['105560', '146', 'KOSPI', 'KB금융'],
    ['051910', '147', 'KOSPI', 'LG화학'],
    ['006800', '148', 'KOSPI', '미래에셋대우'],
    ['042670', '149', 'KOSPI', '두산인프라코어'],
    ['000660', '150', 'KOSPI', 'SK하이닉스'],
    ['006360', '151', 'KOSPI', 'GS건설'],
    ['139480', '154', 'KOSPI', '이마트'],
    ['161390', '155', 'KOSPI', '한국타이어앤테크놀로지'],
    ['035420', '156', 'KOSPI', 'NAVER'],
    ['003490', '157', 'KOSPI', '대한항공'],
    ['032640', '1B0', 'KOSPI', 'LG유플러스'],
    ['010950', '1B2', 'KOSPI', 'S-Oil'],
    ['010130', '1B3', 'KOSPI', '고려아연'],
    ['024110', '1B4', 'KOSPI', '기업은행'],
    ['001680', '1B6', 'KOSPI', '대상'],
    ['047050', '1B7', 'KOSPI', '포스코인터내셔널'],
    ['034020', '1B9', 'KOSPI', '두산중공업'],
    ['023530', '1BA', 'KOSPI', '롯데쇼핑'],
    ['011170', '1BB', 'KOSPI', '롯데케미칼'],
    ['032830', '1BD', 'KOSPI', '삼성생명'],
    ['010140', '1BF', 'KOSPI', '삼성중공업'],
    ['029780', '1BG', 'KOSPI', '삼성카드'],
    ['012450', '1BH', 'KOSPI', '한화에어로스페이스'],
    ['036570', '1BJ', 'KOSPI', '엔씨소프트'],
    ['000080', '1BK', 'KOSPI', '하이트진로'],
    ['071050', '1BL', 'KOSPI', '한국금융지주'],
    ['047810', '1BM', 'KOSPI', '한국항공우주'],
    ['000720', '1BN', 'KOSPI', '현대건설'],
    ['011210', '1BP', 'KOSPI', '현대위아'],
    ['008770', '1BQ', 'KOSPI', '호텔신라'],
    ['035250', '1BS', 'KOSPI', '강원랜드'],
    ['138930', '1BT', 'KOSPI', 'BNK금융지주'],
    ['139130', '1BV', 'KOSPI', 'DGB금융지주'],
    ['114090', '1BW', 'KOSPI', 'GKL'],
    ['001120', '1BX', 'KOSPI', 'LG상사'],
    ['011070', '1BY', 'KOSPI', 'LG이노텍'],
    ['005940', '1BZ', 'KOSPI', 'NH투자증권'],
    ['010060', '1C0', 'KOSPI', 'OCI'],
    ['034730', '1C1', 'KOSPI', 'SK'],
    ['001740', '1C2', 'KOSPI', 'SK네트웍스'],
    ['011780', '1C3', 'KOSPI', '금호석유'],
    ['002350', '1C4', 'KOSPI', '넥센타이어'],
    ['018260', '1C5', 'KOSPI', '삼성에스디에스'],
    ['090430', '1C6', 'KOSPI', '아모레퍼시픽'],
    ['030000', '1C7', 'KOSPI', '제일기획'],
    ['028260', '1C8', 'KOSPI', '삼성물산'],
    ['000880', '1C9', 'KOSPI', '한화'],
    ['088350', '1CA', 'KOSPI', '한화생명'],
    ['009830', '1CB', 'KOSPI', '한화솔루션'],
    ['086280', '1CC', 'KOSPI', '현대글로비스'],
    ['010620', '1CD', 'KOSPI', '현대미포조선'],
    ['001450', '1CE', 'KOSPI', '현대해상'],
    ['035720', '1CF', 'KOSPI', '카카오'],
    ['034230', '1CG', 'KOSDAQ', '파라다이스'],
    ['046890', '1CJ', 'KOSDAQ', '서울반도체'],
    ['069080', '1CK', 'KOSDAQ', '웹젠'],
    ['096530', '1CL', 'KOSDAQ', '씨젠'],
    ['022100', '1CN', 'KOSDAQ', '포스코 ICT'],
    ['068270', '1CP', 'KOSPI', '셀트리온'],
    ['122870', '1CQ', 'KOSDAQ', '와이지엔터테인먼트'],
    ['051900', '1CR', 'KOSPI', 'LG생활건강'],
    ['002790', '1CS', 'KOSPI', '아모레G'],
    ['000810', '1CT', 'KOSPI', '삼성화재'],
    ['008930', '1CV', 'KOSPI', '한미사이언스'],
    ['021240', '1CW', 'KOSPI', '코웨이'],
    ['128940', '1CX', 'KOSPI', '한미약품'],
    ['018880', '1CY', 'KOSPI', '한온시스템'],
    ['027410', '1CZ', 'KOSPI', 'BGF'],
    ['005830', '1D0', 'KOSPI', 'DB손해보험'],
    ['097950', '1D1', 'KOSPI', 'CJ제일제당'],
    ['009240', '1D2', 'KOSPI', '한샘'],
    ['002380', '1D3', 'KOSPI', 'KCC'],
    ['007070', '1D4', 'KOSPI', 'GS리테일'],
    ['012750', '1D5', 'KOSPI', '에스원'],
    ['000100', '1D6', 'KOSPI', '유한양행'],
    ['051600', '1D7', 'KOSPI', '한전KPS'],
    ['069960', '1D8', 'KOSPI', '현대백화점'],
    ['079160', '1D9', 'KOSPI', 'CJ CGV'],
    ['004370', '1DA', 'KOSPI', '농심'],
    ['079550', '1DB', 'KOSPI', 'LIG넥스원'],
    ['204320', '1DC', 'KOSPI', '만도'],
    ['004170', '1DD', 'KOSPI', '신세계'],
    ['161890', '1DE', 'KOSPI', '한국콜마'],
    ['111770', '1DG', 'KOSPI', '영원무역'],
    ['008560', '1DH', 'KOSPI', '메리츠증권'],
    ['006650', '1DJ', 'KOSPI', '대한유화'],
    ['192820', '1DK', 'KOSPI', '코스맥스'],
    ['108670', '1DL', 'KOSPI', 'LG하우시스'],
    ['023590', '1DM', 'KOSPI', '다우기술'],
    ['039130', '1DN', 'KOSPI', '하나투어'],
    ['086900', '1DP', 'KOSDAQ', '메디톡스'],
    ['078340', '1DR', 'KOSDAQ', '컴투스'],
    ['036490', '1DS', 'KOSDAQ', 'SK머티리얼즈'],
    ['035760', '1DT', 'KOSDAQ', 'CJ ENM'],
    ['056190', '1DV', 'KOSDAQ', '에스에프에이'],
    ['241560', '1DW', 'KOSPI', '두산밥캣'],
    ['017800', '1DY', 'KOSPI', '현대엘리베이'],
    ['105630', '1DZ', 'KOSPI', '한세실업'],
    ['240810', '1E0', 'KOSDAQ', '원익IPS'],
    ['001060', '1E1', 'KOSPI', 'JW중외제약'],
    ['053800', '1E2', 'KOSDAQ', '안랩'],
    ['091700', '1E3', 'KOSDAQ', '파트론'],
    ['041510', '1E4', 'KOSDAQ', '에스엠'],
    ['251270', '1E5', 'KOSPI', '넷마블'],
    ['091990', '1E6', 'KOSDAQ', '셀트리온헬스케어'],
    ['003670', '1E8', 'KOSPI', '포스코케미칼'],
    ['003520', '1E9', 'KOSPI', '영진약품'],
    ['178920', '1EA', 'KOSDAQ', 'PI첨단소재'],
    ['316140', '1EB', 'KOSPI', '우리금융지주'],
    ['294870', '1EC', 'KOSPI', 'HDC현대산업개발'],
    ['020150', '1ED', 'KOSPI', '일진머티리얼즈'],
    ['009420', '1EE', 'KOSPI', '한올바이오파마'],
    ['035900', '1EF', 'KOSDAQ', 'JYP Ent.'],
    ['003410', '1EG', 'KOSPI', '쌍용양회'],
    ['028670', '1EH', 'KOSPI', '팬오션'],
    ['011790', '1EJ', 'KOSPI', 'SKC'],
    ['000990', '1EK', 'KOSPI', 'DB하이텍'],
    ['093370', '1EL', 'KOSPI', '후성'],
    ['218410', '1EM', 'KOSDAQ', 'RFHIC'],
    ['005290', '1EN', 'KOSDAQ', '동진쎄미켐'],
    ['033640', '1EP', 'KOSDAQ', '네패스'],
    ['090460', '1EQ', 'KOSDAQ', '비에이치'],
    ['375500', '1ER', 'KOSPI', 'DL이앤씨'],
    # ['102780', '1M0', 'KOSPI', 'KODEX 삼성그룹'],  # 모의투자 종목코드 없음
    # ['143860', '1M1', 'KOSPI', 'TIGER 헬스케어'],  # 모의투자 종목코드 없음
    # ['161510', '1M2', 'KOSPI', 'ARIRANG 고배당주'],  # 모의투자 종목코드 없음
    # ['192090', '1M3', 'KOSPI', 'TIGER 차이나CSI300'],  # 모의투자 종목코드 없음
    # ['315930', '1M4', 'KOSPI', 'KODEX Top5PlusTR'],  # 모의투자 종목코드 없음
]
