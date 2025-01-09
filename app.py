from flask import Flask, render_template, request

app = Flask(__name__)

# 问卷问题
survey_questions = [
    {"id": 1, "question": "你对当下生活有何想说的话？", "type": "text"},
    {"id": 2, "question": "你每天的工作/学习时长是多少小时？", "type": "number"},
    {"id": 3, "question": "你对未来五年有什么期待？", "type": "text"},
    {"id": 4, "question": "你觉得当前最大的压力是什么？", "type": "text"},
    {"id": 5, "question": "你平时最喜欢的放松方式是什么？", "type": "radio", "options": ["运动", "看剧", "玩游戏", "睡觉", "其他"]}
]

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        return render_template('thank_you.html')
    return render_template('survey.html', questions=survey_questions)

app = app.wsgi_app 