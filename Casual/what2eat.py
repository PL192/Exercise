seas = input('weather:\n1. hot\n2. cool\n')
if seas == '1':
    s_mod = '1'
else:
    s_mod = '2'
    
home = input('at home?\nyes(y) no(n)\n')
if home == 'y':
    h_mod = '1' 
else:
    h_mod = '0'
    
time = input('hour now:')
t = int(time)
if t >= 18:
    if h_mod == '0':
        print('==== VEGEYABLE ====', '\n黄瓜', '\n西红柿')
        print('==== FRUIT ====', '\n小柿子', '\n樱桃', '\n蓝莓', '\n桃', '\n苹果')
        if s_mod == '2':
            print('草莓')
    else:
        print('随便少吃点得了\n')
elif t <= 12:
    print('==== FOOD ====')
    if h_mod == '1':
        print('【course】', '\n西红柿炒鸡蛋', '\n蒜茄子拌蛋黄', '\n苏子茄子拌蛋黄', '\n白菜炖(冻)豆腐', '\n甜辣黄豆芽', '\n醋番茄酱')
    if h_mod == '0':
        print('鸡蛋', '\n豆干', '\n东食堂豆腐脑')
    print('==== VEGEYABLE ====')
    if h_mod == '1':
        print('绿豆芽', '\n菠菜', '\n茼蒿', '\n生菜', '\n微波茄子')
    else:
        print('黄瓜', '\n西红柿')
    print('==== FRUIT ====')
    print('小柿子', '\n樱桃', '\n蓝莓', '\n桃', '\n苹果')
    if s_mod == '2':
        print('草莓')
    print('==== HOT DRINK ====')
    ms = input('thick drink?\nyes(y) no(n)\n')
    if ms == 'y':
        print('牛奶', '\n豆乳', '\n豆浆', )
else:
    print('==== VEGEYABLE ====')
    if h_mod == '1':
        print('绿豆芽', '\n菠菜', '\n茼蒿', '\n生菜', '\n微波茄子')
    else:
        print('黄瓜', '\n西红柿')
    print('==== FRUIT ====')
    print('小柿子', '\n樱桃', '\n蓝莓', '\n桃', '\n苹果')
    if s_mod == '2':
        print('草莓')
print('==== DRINK ====')    
tea = input('tea?\nyes(y) no(n)')
if tea == 'y':
    print('气泡橘皮乌龙', '\n气泡茉莉', '\n玉米须茶', )
cafe = input('coffee?\nyes(y) no(n)')
if cafe =='y':
    print('\n拿铁', '\n椰拿铁', '\n奶油冰棍拿铁', '\n榛拿铁', '\n豆乳拿铁')
