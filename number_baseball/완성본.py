from tkinter import *
from random import *
from tkinter.font import *

answer_list = []

def enter_run(event):
    ok_btn.invoke()

def enter_frnd():
    cpu_try.append(_t.get());
    info['text'] = '결과를 알려주세요'
    layout.append(Label(play_frame, text=_t.get()))
    layout[len(layout) - 1].place(x=50 + 100 * ((len(cpu_try) - 1) % 2), y=40 + 20 * ((len(cpu_try) - 1) // 2))
    _t.delete(0, 3);
    ok_btn['command'] = enter_frnd_r


def enter_frnd_r():
    info['text'] = '친구의 숫자를 맞춰보세요'
    a = _t.get()
    layout.append(Label(play_frame, text='{}S {}B'.format(a[0], a[2])));
    layout[len(layout) - 1].place(x=85 + 100 * ((len(cpu_try) - 1) % 2), y=40 + 20 * ((len(cpu_try) - 1) // 2))
    _t.delete(0, 3)  # 입력창 비우기
    ok_btn['command'] = enter_frnd
    if a == '3 0':
        info['text'] = '당신이 정답을 맞췄습니다.'
        ok_btn['text'] = '메뉴선택으로';
        ok_btn['command'] = initialize
        _t['state'] = 'disabled'


def initialize():
    s_cpu_btn['state'] = 'active';
    s_ply_btn['state'] = 'active';
    s_set_btn['state'] = 'active'  # 버튼 활성화
    info['text'] = '선택 대기중...';
    ok_btn['text'] = '확인';
    ok_btn['state'] = 'disabled'
    for i in range(len(layout)):
        layout[i].destroy()
    layout.clear()
    cpu_try.clear()
    answer_cmp.clear()
    answer_list.clear()

def answer_group(result):
    frt, sec, trd = cpu_try[len(cpu_try) - 1]
    answer = set()  # contemporary answer set
    if setting['zero']:
        a = 0
    else:
        a = 1
    if result == (3, 0):  # answer = 3S
        info['text'] = 'CPU가 정답을 맞췄습니다. 컴퓨터 WIN!!'
        ok_btn['text'] = '메뉴선택으로';
        _t['state'] = 'disabled'
        ok_btn['command'] = lambda: initialize()
        return
    elif result == (2, 0):  # 2S 0B
        for i in range(a, 10):
            if i == frt or i == sec or i == trd:
                continue
            answer.add((frt, sec, i))
            answer.add((frt, i, trd))
            answer.add((i, sec, trd))
    elif result == (1, 2):  # 1S 2B
        answer.add((frt, trd, sec))
        answer.add((trd, sec, frt))
        answer.add((sec, frt, trd))
    elif result == (1, 1):  # 1S 1B
        for i in range(a, 10):
            if i == frt or i == sec or i == trd:
                continue
            answer.add((frt, trd, i))
            answer.add((frt, i, sec))
            answer.add((trd, sec, i))
            answer.add((i, sec, frt))
            answer.add((sec, i, trd))
            answer.add((i, frt, trd))
    elif result == (1, 0):  # 1S
        for i in range(a, 10):
            if i == frt or i == sec or i == trd:
                continue
            for j in range(a, 10):
                if j == i or j == frt or j == sec or j == trd:
                    continue
                answer.add((frt, i, j))
                answer.add((i, sec, j))
                answer.add((i, j, trd))
    elif result == (0, 3):  # 3B
        answer.add((sec, trd, frt))
        answer.add((trd, frt, sec))
    elif result == (0, 2):  # 2B
        for i in range(a, 10):
            if i == frt or i == sec or i == trd:
                continue
            answer.add((i, trd, sec))
            answer.add((trd, i, sec))
            answer.add((sec, trd, i))
            answer.add((i, trd, frt))
            answer.add((trd, i, frt))
            answer.add((trd, frt, i))
            answer.add((sec, frt, i))
            answer.add((sec, i, frt))
            answer.add((i, frt, sec))
    elif result == (0, 1):  # 1B
        for i in range(a, 10):
            if i == frt or i == sec or i == trd:
                continue
            for j in range(a, 10):
                if j == i or j == frt or j == sec or j == trd:
                    continue
                answer.add((i, frt, j))
                answer.add((i, j, frt))
                answer.add((sec, i, j))
                answer.add((i, j, sec))
                answer.add((trd, i, j))
                answer.add((i, trd, j))
    elif result == (0, 0):
        for i in range(a, 10):
            if i == frt or i == sec or i == trd:
                continue
            for j in range(a, 10):
                if j == i or j == frt or j == sec or j == trd:
                    continue
                for k in range(a, 10):
                    if k == j or k == i or k == frt or k == sec or k == trd:
                        continue
                    answer.add((i, j, k))
    if len(answer_cmp) == 0:
        answer_cmp.update(answer)
        print(answer_cmp)
    else:
        answer_cmp.intersection_update(answer)
        print(answer_cmp)
    cpu_try.append(choice(list(answer_cmp)))


def answer_group2(result):
    if (setting['max'] == 4 and result == (4, 0)) or (setting['max'] == 3 and result == (3, 0)):  # answer = 4S or 3S
        info['text'] = 'CPU가 정답을 맞췄습니다. 컴퓨터 WIN!!'
        ok_btn['text'] = '메뉴선택으로';
        _t['state'] = 'disabled'
        ok_btn['command'] = lambda: initialize()
        return

    i = 0
    while i != len(answer_list):
        t_st = 0;
        t_bl = 0
        for j in range(setting['max']):
            if cpu_try[-1][j] not in answer_list[i]:  # out
                pass
            elif cpu_try[-1][j] in answer_list[i] and cpu_try[-1][j] == answer_list[i][j]:  # strike
                t_st += 1
            else:  # ball
                t_bl += 1
        if result == (t_st, t_bl):
            i += 1
            continue
        else:
            answer_list.remove(answer_list[i])
    cpu_try.append(choice(answer_list))


def msg(n):   #message
    if n == 1:
        cpu_try.append(make_num())  # 컴퓨터가 사람의 수를 맞추는 시도
        cpu_num[0] = make_num()  # 사람이 맞춰야하는 컴퓨터의 수
        if setting['zero']:
            a = 0
        else:
            a = 1
        if setting['max'] == 4 or setting['dupl']:
            for frt in range(a, 10):
                for sec in range(a, 10):
                    if frt == sec and (not setting['dupl']):
                        continue
                    for trd in range(a, 10):
                        if (trd == frt or trd == sec) and (not setting['dupl']):
                            continue
                        if setting['max'] == 4:
                            for fth in range(a, 10):
                                if (fth == frt or fth == sec or fth == trd) and (not setting['dupl']):
                                    continue
                                answer_list.append((frt, sec, trd, fth))
                        else:
                            answer_list.append((frt, sec, trd))
        print('answer list :', answer_list)
        print('cpu num : ', cpu_num[0])
        s_cpu_btn['state'] = 'disabled';
        s_ply_btn['state'] = 'disabled';
        s_set_btn['state'] = 'disabled'  # 버튼 비활성화
        ok_btn['state'] = 'active';
        _t['state'] = 'normal'  # 입력창 활성화
        ok_btn['command'] = lambda: enter(_t.get())
        layout.append(Message(window, text='''컴퓨터와 대전하기는 플레이어와 컴퓨터가 번갈아가면서 숫자를 제시합니다.
플레이어는 컴퓨터가 맞출, 규칙에 맞는 숫자를 미리 생각해두시기 바랍니다.
플레이어부터 시작하여 숫자를 제시합니다. 플레이어가 제시한 숫자를 보고 컴퓨터가 결과를 알려줄 것입니다.
컴퓨터는 결과를 알려준 후에 숫자를 제시합니다. 플레이어는 컴퓨터가 제시한 숫자를 보고 결과를 알려주셔야 합니다.
결과는 스트리아크의 개수와 볼의 개수를 공백을 두고 입력하여 '스트라이크 볼' 형태로 알려주시면 됩니다.

만약 결과가 1스트라이크 1볼이라면 입력창에 '1 1' 을 입력한 후 확인을 누르면 됩니다.'''
                              , width=690, relief='solid'));
        layout[len(layout) - 1].place(anchor='center', x=350, y=155)

        info['text'] = '당신의 차례 입니다. 추측한 컴퓨터의 숫자를 입력하세요'
        layout.append(Label(play_frame, text='<플레이어1>'));
        layout[len(layout) - 1].place(x=50, y=0)
        layout.append(Label(play_frame, text='<CPU>'));
        layout[len(layout) - 1].place(x=160, y=0)
        layout.append(Label(play_frame, text='회차'));
        layout[len(layout) - 1].place(x=10, y=20)
        layout.append(Label(play_frame, text='입력'));
        layout[len(layout) - 1].place(x=50, y=20)
        layout.append(Label(play_frame, text='결과'));
        layout[len(layout) - 1].place(x=90, y=20)
        layout.append(Label(play_frame, text='입력'));
        layout[len(layout) - 1].place(x=150, y=20)
        layout.append(Label(play_frame, text='결과'));
        layout[len(layout) - 1].place(x=190, y=20)

    elif n == 2:
        ok_btn['command'] = lambda: enter_frnd()
        s_cpu_btn['state'] = 'disabled';
        s_ply_btn['state'] = 'disabled';
        s_set_btn['state'] = 'disabled'  # 버튼 비활성화
        ok_btn['state'] = 'active';
        _t['state'] = 'normal'  # 입력창 활성화
        layout.append(Message(window, text='''사람과 대전하기는 플레이어가 서로 번갈아가면서 숫자를 제시합니다.
플레이어는 서로 맞출, 규칙에 맞는 숫자를 미리 각자 생각해두시기 바랍니다.
플레이어1부터 시작하여 숫자를 제시합니다. 플레이어가 제시한 숫자를 보고 다른 플레이어가 결과를 알려줄 것입니다.
결과는 스트리아크의 개수와 볼의 개수를 공백을 두고 입력하여 '스트라이크 볼' 형태로 알려주시면 됩니다.

만약 결과가 1스트라이크 1볼이라면 입력창에 '1 1' 을 입력한 후 확인을 누르면 됩니다.'''
                              , width=690, relief='solid'));
        layout[len(layout) - 1].place(anchor='center', x=350, y=155)
        info['text'] = '플레이어1의 차례입니다. 시도할 숫자를 입력하세요'
        layout.append(Label(play_frame, text='<플레이어1>'));
        layout[len(layout) - 1].place(x=50, y=0)
        layout.append(Label(play_frame, text='<플레이어2>'));
        layout[len(layout) - 1].place(x=160, y=0)
        layout.append(Label(play_frame, text='회차'));
        layout[len(layout) - 1].place(x=10, y=20)
        layout.append(Label(play_frame, text='입력'));
        layout[len(layout) - 1].place(x=50, y=20)
        layout.append(Label(play_frame, text='결과'));
        layout[len(layout) - 1].place(x=90, y=20)
        layout.append(Label(play_frame, text='입력'));
        layout[len(layout) - 1].place(x=150, y=20)
        layout.append(Label(play_frame, text='결과'));
        layout[len(layout) - 1].place(x=190, y=20)


def enter(a):  #enter 키 활성화 함수... 이런게 생각보다 힘드네...
    _t.delete(0, END)
    S = 0;
    B = 0
    for i in range(setting['max']):
        if int(a[i]) in cpu_num[0]:
            if int(a[i]) == cpu_num[0][i]:
                S += 1
            else:
                B += 1
    layout.append(Label(play_frame, text='{}회'.format(len(cpu_try))))
    layout[len(layout) - 1].place(x=10, y=20 + 20 * len(cpu_try))
    layout.append(Label(play_frame, text=a));
    layout[len(layout) - 1].place(x=50, y=20 + 20 * len(cpu_try))
    layout.append(Label(play_frame, text='{}S {}B'.format(S, B)));
    layout[len(layout) - 1].place(x=85, y=20 + 20 * len(cpu_try))
    if (setting['max'] == 4 and S == 4) or (setting['max'] == 3 and S == 3):  # 사람이 정답을 맞췄을 경우
        info['text'] = '당신이 정답을 맞췄습니다. 플레이어 WIN!!'
        ok_btn['text'] = '메뉴선택으로'
        _t['state'] = 'disabled'
        ok_btn['command'] = lambda: initialize()
    else:
        cpu()


def cpu():
    print('cpu try: ', cpu_try[len(cpu_try) - 1])  # test
    layout.append(Label(play_frame, text="".join(map(str, cpu_try[len(cpu_try) - 1]))));
    layout[len(layout) - 1].place(x=150, y=20 + 20 * len(cpu_try))
    info['text'] = 'CPU에게 결과를 알려주세요.'
    ok_btn['command'] = lambda: enter_r(_t.get())


def enter_r(a):
    _t.delete(0, END)  # 입력창 비우기
    layout.append(Label(play_frame, text='{}S {}B'.format(a[0], a[2])));
    layout[len(layout) - 1].place(x=190, y=20 + 20 * len(cpu_try))
    ok_btn['command'] = lambda: enter(_t.get())
    info['text'] = '당신의 차례 입니다. 추측한 CPU의 숫자를 입력하세요'
    result = tuple(map(int, a.split()))  # send result

    if setting['max'] == 3 and (not setting['dupl']):  # 3자리수에 중복 허용이 안될 경우 => BFS 알고리즘
        answer_group(result)
    else:
        answer_group2(result)


def make_num():
    if setting['zero']:
        a = 0
    else:
        a = 1
    frt = randint(a, 9)
    sec = randint(a, 9)
    while sec == frt and (not setting['dupl']):
        sec = randint(a, 9)
    trd = randint(a, 9)
    while (trd == frt or trd == sec) and (not setting['dupl']):
        trd = randint(a, 9)
    if setting['max'] == 4:
        frth = randint(a, 9)
        while (frth == trd or frth == sec or frth == frt) and (not setting['dupl']):
            frth = randint(a, 9)
    if setting['max'] == 3:
        return (frt, sec, trd)
    else:
        return (frt, sec, trd, frth)


def set_setting():
    s_cpu_btn['state'] = 'disabled';
    s_ply_btn['state'] = 'disabled';
    s_set_btn['state'] = 'disabled'  # 버튼 비활성화
    SetFrame = LabelFrame(text='설정', width=400, height=110, labelanchor='n')
    max_num = IntVar();
    dupl = IntVar();
    zero = IntVar()
    layout.append(SetFrame);
    layout[len(layout) - 1].place(anchor='center', x=350, y=150)
    layout.append(Radiobutton(SetFrame, text='3자리', value=3, variable=max_num))
    layout[len(layout) - 1].place(x=110, y=10)
    if setting['max'] == 3:
        layout[len(layout) - 1].select()
    layout.append(Radiobutton(SetFrame, text='4자리', value=4, variable=max_num))
    layout[len(layout) - 1].place(x=110, y=30)
    if setting['max'] == 4:
        layout[len(layout) - 1].select()
    layout.append(Checkbutton(SetFrame, text='중복허용', variable=dupl))
    layout[len(layout) - 1].place(x=210, y=10)
    if setting['dupl']:
        layout[len(layout) - 1].select()
    layout.append(Checkbutton(SetFrame, text='사용 가능한 숫자에 0을 포함', variable=zero))
    layout[len(layout) - 1].place(x=210, y=30)
    if setting['zero']:
        layout[len(layout) - 1].select()
    layout.append(Button(SetFrame, text='확인', command=lambda: ok_set(max_num.get(), dupl.get(), zero.get())))
    layout[len(layout) - 1].place(anchor='center', x=SetFrame['width'] // 2, y=70)


def ok_set(max_num, dupl, zero):
    setting['max'] = max_num;
    setting['dupl'] = dupl;
    setting['zero'] = zero
    s_cpu_btn['state'] = 'active';
    s_ply_btn['state'] = 'active';
    s_set_btn['state'] = 'active'  # 버튼 활성화
    print(setting)
    for i in range(len(layout) - 1, -1, -1):
        layout[i].destroy()
    layout.clear()


cpu_try = list()
cpu_num = [0]
answer_cmp = set()
layout = list()
setting = {'max': 3, 'dupl': False, 'zero': False}

window = Tk()
window.geometry('700x500')
window.resizable(0, 0)
window.title('인공지능 숫자야구')
# font set
font_title = Font(family="나눔 고딕", size=20, weight='bold')
font_menu = Font(family='나눔 고딕', size=10)
# frame set
menu_frame = Frame(window, relief='solid', width=700, height=300)
menu_frame.pack(expand=True, fill='both')
# title
Label(menu_frame, text='인공지능 숫자야구', font=font_title).pack()
# frame set
select_frame = LabelFrame(menu_frame, width=400, height=50, relief='groove', text='<메뉴>'
                          , labelanchor='n', font=font_menu)
select_frame.pack()
play_frame = LabelFrame(window, text='<Score Board>', relief='groove', labelanchor='n', width=600, height=200)
play_frame.place(anchor='center', x=350, y=380)

# button
s_cpu_btn = Button(select_frame, text='컴퓨터와 대전', command=lambda: msg(1))
s_cpu_btn.place(anchor='center', x=80, y=15)
s_ply_btn = Button(select_frame, text='친구들과 대전', command=lambda: msg(2))
s_ply_btn.place(anchor='center', x=180, y=15)
s_set_btn = Button(select_frame, text='설정', command=lambda: set_setting());
s_set_btn.place(anchor='center', x=260, y=15)
s_quit_btn = Button(select_frame, text='종료', command=lambda: quit());
s_quit_btn.place(anchor='center', x=310, y=15)
# entry
info = Label(window, text='선택 대기중...');
info.place(anchor='center', x=350, y=235)
_t = Entry(window, state='disabled');
_t.place(x=260, y=250)
_t.bind("<Return>", enter_run)
ok_btn = Button(window, text='확인', command=lambda: enter(_t.get()), state='disabled')
ok_btn.place(x=410, y=246)

window.mainloop()