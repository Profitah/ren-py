# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image bg_night = "./images/bg/bg_night.jpeg"
image chg_N = "./images/chara/Neumann.jpeg"
image chg_T = "./images/chara/Turing.jpeg"
image chg_W = "./images/chara/Wozniak.jpeg"
image chg_cg = "./images/chara/cg.jpeg"

# 게임에서 사용할 캐릭터를 정의합니다.
define skhu = Character('회대군', color="#970000")
define N = Character('폰 노이만', color="#6d8a6d")
define T = Character('엘런 튜링', color="#3442df")
define W = Character('워즈니악', color="#c8ffc8") 
define cg = Character('교수님', color="#c8ffc8") 

define narrator = Character(None, kind=nvl)

# 이미지 위치를 중앙으로 이동시키는 변환을 정의합니다.
transform move_center:
    yalign 0.5 
    xalign 0.5  

# 여기에서부터 게임이 시작합니다.
label start:
    scene bg_night
    show chg_cg at move_center

    nvl clear
    narrator "{fast}\n제목 : 인물연구\n과목명 : 운영체제\n학번 : 202012164\n이름 : 이윤아\n제출일 : 2024년 5월 23일"
    nvl clear
    hide chg_cg

# 여기에 선택지를 추가합니다.
#1. title 2. 폰노이만 3. 엘런튜링 4. 스티브 워즈니악 5. epilogue
    menu:
        "1. title":
            jump title
        "2. 폰 노이만":
            jump Neumann
        "3. 엘런 튜링":
            jump Turing
        "4. 스티브 워즈니악":
            jump Wozniak
        "5. epilogue":
            jump epilogue

label title: 
    scene bg_night 
    skhu "운영체제 A+을 받기 위해 공부를 하겠어.."

    show chg_cg at move_center
    cg "안녕하세요. 착교 TV입니다. 오늘은 운영체제에 대해 알아보겠습니다..."

    skhu "헉.. 잠들었다ㅠㅠ"

    # 화면을 검정색으로 전환
    scene black with dissolve
    pause 2  # 2초간 검정 화면 유지

    # 다시 배경사진으로 전환
    scene bg_night with dissolve

    jump start

# 폰 노이만에 대한 퀴즈
label Neumann:
    show chg_N at move_center
    N "안녕, 나는 폰 노이만이야. 컴퓨터 과학자이자 수학자이지."
    N "첫 번째 퀴즈를 시작할게. 중앙처리장치(CPU), 메모리, 프로그램으로 구성된 컴퓨터 시스템을 만들었어."
    N "그것의 이름은 뭘까?"

    menu:
        "폰 노이만 아키텍처":
            jump Neumann_correct1
        "폰 노이만 머신":
            jump Neumann_correct1
        "폰 노이만 시스템":
            jump Neumann_incorrect1

label Neumann_correct1:
    N "정답이야! 내가 만든 컴퓨터 시스템은 '폰 노이만 아키텍처'라고 불리지."
    jump Neumann_quiz2

label Neumann_incorrect1:
    N "아쉽지만, 그건 정답이 아니야. 내가 만든 시스템은 '폰 노이만 아키텍처'라고 불려."
    jump Neumann_quiz2

label Neumann_quiz2:
    N "두 번째 퀴즈를 낼게. 내가 만든 아키텍처의 중요한 특징 중 하나는 무엇일까?"

    menu:
        "프로그램 내장 방식":
            jump Neumann_correct2
        "다중 프로세싱":
            jump Neumann_incorrect2
        "병렬 처리":
            jump Neumann_incorrect2

label Neumann_correct2:
    N "정답이야! '폰 노이만 아키텍처'의 중요한 특징 중 하나는 '프로그램 내장 방식'이지."
    jump Neumann_quiz3

label Neumann_incorrect2:
    N "아쉽지만, 그건 정답이 아니야. 정답은 '프로그램 내장 방식'이야."
    jump Neumann_quiz3

label Neumann_quiz3:
    N "마지막 퀴즈야. 내가 기여한 분야 중 하나는 무엇일까?"

    menu:
        "양자 컴퓨팅":
            jump Neumann_incorrect3
        "선형대수학":
            jump Neumann_incorrect3
        "게임 이론":
            jump Neumann_correct3

label Neumann_correct3:
    N "정답이야! 내가 기여한 분야 중 하나는 '게임 이론'이지."
    hide chg_N
    jump start

label Neumann_incorrect3:
    N "아쉽지만, 그건 정답이 아니야. 정답은 '게임 이론'이야."
    hide chg_N
    jump start

# 엘런 튜링에 대한 퀴즈
label Turing:
    show chg_T at move_center
    T "나는 엘런 튜링, 수학자이자 컴퓨터 과학자야. 첫 번째 퀴즈를 시작할게."
    T "나는 현대 컴퓨팅의 기초가 되는 개념을 개발했어. 그것은 무엇일까?"

    menu:
        "튜링 머신":
            jump Turing_correct1
        "튜링 테스트":
            jump Turing_incorrect1
        "튜링 완전성":
            jump Turing_incorrect1

label Turing_correct1:
    T "정답이야! 나는 '튜링 머신' 개념을 개발했어."
    jump Turing_quiz2

label Turing_incorrect1:
    T "아쉽지만, 그건 정답이 아니야. 정답은 '튜링 머신'이야."
    jump Turing_quiz2

label Turing_quiz2:
    T "두 번째 퀴즈를 낼게. 내가 제안한 인공지능의 기초가 되는 테스트는 무엇일까?"

    menu:
        "튜링 테스트":
            jump Turing_correct2
        "차분기":
            jump Turing_incorrect2
        "퍼지 논리":
            jump Turing_incorrect2

label Turing_correct2:
    T "정답이야! 내가 제안한 테스트는 '튜링 테스트'야."
    jump Turing_quiz3

label Turing_incorrect2:
    T "아쉽지만, 그건 정답이 아니야. 정답은 '튜링 테스트'야."
    jump Turing_quiz3

label Turing_quiz3:
    T "마지막 퀴즈야. 내가 기여한 분야 중 하나는 무엇일까?"

    menu:
        "양자 컴퓨팅":
            jump Turing_incorrect3
        "암호 해독":
            jump Turing_correct3
        "그래픽스":
            jump Turing_incorrect3

label Turing_correct3:
    T "정답이야! 내가 기여한 분야 중 하나는 '암호 해독'이지."
    hide chg_T
    jump start

label Turing_incorrect3:
    T "아쉽지만, 그건 정답이 아니야. 정답은 '암호 해독'이야."
    hide chg_T
    jump start

# 스티브 워즈니악에 대한 퀴즈
label Wozniak:
    show chg_W at move_center
    W "안녕, 나는 애플의 공동 창립자인 워즈니악이야. 첫 번째 퀴즈를 시작할게."
    W "내가 설계한 첫 번째 개인용 컴퓨터는 무엇일까?"

    menu:
        "애플 I":
            jump Wozniak_correct1
        "애플 II":
            jump Wozniak_incorrect1
        "애플 III":
            jump Wozniak_incorrect1

label Wozniak_correct1:
    W "정답이야! 내가 설계한 첫 번째 개인용 컴퓨터는 '애플 I'이야."
    jump Wozniak_quiz2

label Wozniak_incorrect1:
    W "아쉽지만, 그건 정답이 아니야. 정답은 '애플 I'이야."
    jump Wozniak_quiz2

label Wozniak_quiz2:
    W "두 번째 퀴즈를 낼게. 내가 만든 컴퓨터 중 성공적으로 상업화된 모델은 무엇일까?"

    menu:
        "애플 I":
            jump Wozniak_incorrect2
        "애플 II":
            jump Wozniak_correct2
        "애플 III":
            jump Wozniak_incorrect2

label Wozniak_correct2:
    W "정답이야! 성공적으로 상업화된 모델은 '애플 II'야."
    jump Wozniak_quiz3

label Wozniak_incorrect2:
    W "아쉽지만, 그건 정답이 아니야. 정답은 '애플 II'야."
    jump Wozniak_quiz3

label Wozniak_quiz3:
    W "마지막 퀴즈야. 내가 기여한 분야 중 하나는 무엇일까?"

    menu:
        "양자 컴퓨팅":
            jump Wozniak_incorrect3
        "그래픽스":
            jump Wozniak_incorrect3
        "개인용 컴퓨터 혁명":
            jump Wozniak_correct3

label Wozniak_correct3:
    W "정답이야! 내가 기여한 분야 중 하나는 '개인용 컴퓨터 혁명'이지."
    hide chg_W
    jump start

label Wozniak_incorrect3:
    W "아쉽지만, 그건 정답이 아니야. 정답은 '개인용 컴퓨터 혁명'이야."
    hide chg_W
    jump start

label epilogue:
    scene bg_night
    skhu "비록 잠들었지만 유익한 시간을 보낸 것 같다."
    skhu "앞으로도 더 열심히 공부해야지!"

    menu:
        "1. title":
            jump title
        "2. 폰 노이만":
            jump Neumann
        "3. 엘런 튜링":
            jump Turing
        "4. 스티브 워즈니악":
            jump Wozniak
        "5. epilogue":
            jump epilogue

return
