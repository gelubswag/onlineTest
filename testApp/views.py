from django.shortcuts import render, redirect
from testApp.models import Subject, SubjTest, Question, UserTest, UserAnswer, Option
from testApp.forms import SubjectForm, TestForm, QuesttForm, OptForm
from django.contrib.auth import decorators
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from datetime import datetime
import random


def testpage(request):
    return render(request, "test.html")


def main(request):

    context = {
        "pageTitle": "Дисциплины",
        "subjects": Subject.objects.all().order_by("name"),
    }
    return render(request, "test/main.html", context)


@staff_member_required
def addSubject(request):
    if not (request.user.is_staff):
        return
    if request.method == "GET":
        context = {"pageTitle": "Добавить дисциплину", "form": SubjectForm()}
        return render(request, "test/subjectForm.html", context)
    else:
        try:
            subj = request.POST["name"]
            subj = Subject.objects.create(name=subj)
            return redirect("testApp:main")
        except Exception as err:
            context = {
                "pageTitle": "Добавить дисциплину",
                "subjects": Subject.objects.all().order_by("name"),
                "err": err,
                "form": SubjectForm(),
            }
            return render(request, "test/subjectForm.html", context)


@staff_member_required
def deleteSubject(request, subId):
    if not (request.user.is_staff):
        return redirect("testApp:main")
    try:
        subj = Subject.objects.filter(id=subId).all()[0]
        subj.delete()
    except:
        pass

    return redirect("testApp:main")


@decorators.login_required
def detailsSubject(request, subId):
    if not request.user.is_authenticated:
        return redirect("logauth:log")
    subj = Subject.objects.filter(id=subId).all()[0]
    tests = SubjTest.objects.filter(subj=subj).all()
    context = {"pageTitle": subj.name, "tests": tests, "subject": subj}
    return render(request, "test/subjectDetails.html", context)


@staff_member_required
def changeSubject(request, subId):
    if not request.user.is_authenticated:
        return redirect("logauth:log")
    if not (request.user.is_staff):
        return redirect("testApp:main")
    if request.method == "GET":
        subj = Subject.objects.filter(id=subId).all()[0]
        context = {"pageTitle": "Изменить название", "form": SubjectForm(instance=subj)}
        return render(request, "test/subjectForm.html", context)
    else:
        subj = Subject.objects.filter(id=subId).all()[0]
        subj.name = request.POST["name"]
        subj.save()
        return redirect("testApp:main")


##################################################### TEST


@staff_member_required
def addTest(request, subId):
    if not request.user.is_authenticated:
        return redirect("logauth:log")
    if not (request.user.is_staff):
        return redirect("testApp:main")
    if request.method == "GET":
        context = {"pageTitle": "Добавить тест", "form": TestForm()}
        return render(request, "test/subjectForm.html", context)
    else:
        subj = Subject.objects.filter(id=subId).all()[0]
        test = SubjTest.objects.create(
            subj=subj,
            name=request.POST["name"],
            questions_num=request.POST["questions_num"],
            test_questions_num = request.POST["test_questions_num"]
        )
        test.save()
        return redirect("testApp:detailsSubject", subId=subId)


@staff_member_required
def deleteTest(request, subId, testId):
    if not (request.user.is_staff):
        return redirect("testApp:detailsSubject", subId=subId)
    try:
        test = SubjTest.objects.filter(id=testId).all()[0]
        test.delete()
    except:
        pass

    return redirect("testApp:detailsSubject", subId=subId)


@staff_member_required
def changeTest(request, subId, testId):
    if not request.user.is_authenticated:
        return redirect("logauth:log")
    if not (request.user.is_staff):
        return redirect("testApp:main")
    if request.method == "GET":
        test = SubjTest.objects.filter(id=testId).all()[0]
        context = {"pageTitle": "Изменить тест", "form": TestForm(instance=test)}
        return render(request, "test/subjectForm.html", context)
    else:
        subj = Subject.objects.filter(id=subId).all()[0]
        test = SubjTest.objects.filter(id=testId).all()[0]
        test.name = request.POST["name"]
        test.questions_num = request.POST["questions_num"]
        test.test_questions_num = request.POST["test_questions_num"]
        test.save()
        return redirect("testApp:detailsSubject", subId=subId)


@decorators.login_required
def detailsTest(request, subId, testId):
    test = SubjTest.objects.filter(id=testId).all()[0]
    questions = Question.objects.filter(test=test).all()
    context = {
        "pageTitle": test.name,
        "subject": test.subj,
        "test": test,
    }
    if not request.user.is_staff:
        usertest = UserTest.objects.filter(
            user=request.user, test=test, isFinished=False
        ).all()
        if not usertest:

            usertest = UserTest.objects.create(
                test=test,
                user=request.user,
                time_start=datetime.now().isoformat(),
            )
            pool = usertest.make_question_pool()

            opts = Option.objects.filter(
                quest=Question.objects.filter(id=usertest.question_pool[0]).all()[0]
            )
            for opt in opts:
                UserAnswer.objects.create(
                    quest=Question.objects.filter(id=usertest.question_pool[0]).all()[
                        0
                    ],
                    test=usertest,
                    user=request.user,
                    opt=opt,
                    answer=False,
                ).save()
                usertest = UserTest.objects.filter(
                    user=request.user, test=test, isFinished=False
                ).all()[0]
                return redirect(
                    "testApp:detailsQuest",
                    subId=subId,
                    testId=testId,
                    questId=usertest.question_pool[0],
                )
        else:
            usertest = usertest[0]
        return redirect(
            "testApp:detailsQuest",
            subId=subId,
            testId=testId,
            questId=usertest.question_pool[0],
        )
    else:
        if not questions:
            for i in range(test.questions_num):
                Question.objects.create(test=test).save()
        context["questions"] = enumerate(Question.objects.filter(test=test).all())

    if not request.user.is_authenticated:
        return redirect("logauth:log")

    return render(request, "test/testDetails.html", context)


@decorators.login_required
def detailsQuest(request, subId, testId, questId):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect("logauth:log")

        test = SubjTest.objects.filter(id=testId).all()[0]
        question = Question.objects.filter(id=questId).all()[0]
        context = {
            "pageTitle": test.name,
            "questions": enumerate(Question.objects.filter(test=test).all()),
            "question": question,
            "test": test,
            "subject": test.subj,
            "form": QuesttForm(instance=question),
            "userAnswers": UserAnswer.objects.filter(quest=questId),
            "options": Option.objects.filter(quest=questId),
            "right_num": len(Option.objects.filter(quest=questId, isRight=True)),
        }
        if not (request.user.is_staff):
            usertest = UserTest.objects.filter(
                isFinished=False, user=request.user, test=test
            ).all()[0]
            context["user_ans_opts"] = [
                i.opt.id
                for i in UserAnswer.objects.filter(
                    quest=questId, answer=True, test=usertest
                )
            ]

            if UserAnswer.objects.filter(quest=questId):
                for i in UserAnswer.objects.filter(quest=questId):
                    if i.answer:
                        context[f"{i.opt}"] = True
            else:
                for i in Option.objects.filter(quest=questId):
                    UserAnswer.objects.create(
                        quest=Question.objects.get(id=questId),
                        test=usertest,
                        user=request.user,
                        opt=i,
                        answer=False,
                    ).save()

            if questId == usertest.question_pool[-1]:
                context["is_last"] = True
        return render(request, "test/questionDetails.html", context)
    else:
        if request.user.is_staff:
            question = Question.objects.filter(id=questId).all()[0]
            try:
                question.image = request.FILES["image"]
            except:
                pass
            question.text = request.POST["text"]
            question.optionsNum = request.POST["optionsNum"]
            question.weight = request.POST["weight"]
            question.imageURL = request.POST["imageURL"]
            opts = Option.objects.filter(quest=question).all()
            if len(opts) > int(question.optionsNum):
                Option.objects.filter().delete()
            while len(opts) < int(question.optionsNum):
                Option.objects.create(quest=question).save()
                opts = Option.objects.filter(quest=question).all()
            question.save()
            return redirect(
                "testApp:changeOpts", subId=subId, testId=testId, questId=questId
            )
        else:
            ####DO
            test = UserTest.objects.filter(
                test=SubjTest.objects.filter(id=testId).all()[0],
                user=request.user,
                isFinished=0,
            )[0]
            question = Question.objects.filter(id=questId).all()[0]
            opts = Option.objects.filter(quest=question).all()
            for opt in opts:
                answer = UserAnswer.objects.filter(
                    test=test, quest=questId, user=request.user, opt=opt
                ).all()
                if not (answer):
                    answer = UserAnswer.objects.create(
                        test=test, quest=question, user=request.user, opt=opt
                    )
                    answer.save()
                else:
                    answer = answer[0]
                isRight = request.POST.get(f"isRight{opt.id}")
                if isRight:
                    isRight = True
                else:
                    isRight = False
                answer.answer = isRight
                answer.save()
            if not ("last" in request.POST):
                return redirect(
                    "testApp:detailsQuest",
                    subId=subId,
                    testId=testId,
                    questId=test.question_pool[test.question_pool.index(questId) + 1],
                )
            else:
                return redirect("testApp:finishTest", testId=testId)


@staff_member_required
def changeQuest(request, subId, testId, questId):
    question = Question.objects.filter(id=questId).all()[0]
    try:
        question.image = request.POST["image"]
    except:
        pass
    question.text = request.POST["text"]
    question.optionsNum = request.POST["optionsNum"]
    question.weight = request.POST["weight"]
    question.imageURL = request.POST["imageURL"]
    options = Option.objects.filter(quest=question).all()
    if len(opts) > question.optionsNum:
        Option.objects.filter().delete()
    while len(opts) < question.optionsNum:
        Option.objects.create(quest=question).save()
        opts = Option.objects.filter(quest=question).all()
    question.save()
    return redirect("testApp:detailsQuest", subId=subId, testId=testId, questId=questId)


@staff_member_required
def changeOpts(request, subId, testId, questId):
    if request.method == "GET":
        if request.user.is_staff:
            question = Question.objects.filter(id=questId).all()[0]
            # try:
            #     question.image = request.FILES["image"]
            # except:
            #     pass
            # question.text = request.POST["text"]
            # question.optionsNum = request.POST["optionsNum"]
            # question.weight = request.POST["weight"]
            # question.save()
        if not request.user.is_authenticated:
            return redirect("logauth:log")
        test = SubjTest.objects.filter(id=testId).all()[0]
        question = Question.objects.filter(id=questId).all()[0]
        opts = Option.objects.filter(quest=question).all()
        if len(opts) > question.optionsNum:
            Option.objects.filter().delete()
        while len(opts) < question.optionsNum:
            Option.objects.create(quest=question).save()
            opts = Option.objects.filter(quest=question).all()
        opts = Option.objects.filter(quest=question).all()
        optsforms = [OptForm(instance=i) for i in opts]
        context = {
            "pageTitle": test.name,
            "questions": enumerate(Question.objects.filter(test=test).all()),
            "question": question,
            "test": test,
            "subject": test.subj,
            "opts": optsforms,
            "optinstnace": Option.objects.filter(quest=question).all(),
        }
        return render(request, "test/optionDetails.html", context)
    else:
        ids = [opt.id for opt in Option.objects.filter(quest=questId)]
        for i in ids:
            image = request.FILES.get(f"image{i}")
            text = request.POST.get(f"text{i}")
            isRight = request.POST.get(f"isRight{i}")
            imageURL = request.POST.get(f"imageURL{i}")
            if isRight:
                isRight = True
            else:
                isRight = False

            opt = Option.objects.filter(id=i).all()[0]
            if image:
                opt.image = image
            opt.text = text
            opt.isRight = isRight
            opt.imageURL = imageURL
            opt.save()
        test = SubjTest.objects.filter(id=testId).all()[0]
        question = Question.objects.filter(id=questId).all()[0]
        opts = Option.objects.filter(quest=question).all()
        optsforms = [OptForm(instance=i) for i in opts]
        context = {
            "pageTitle": test.name,
            "questions": enumerate(Question.objects.filter(test=test).all()),
            "question": question,
            "test": test,
            "subject": test.subj,
            "opts": optsforms,
            "optinstnace": Option.objects.filter(quest=question).all(),
        }
        return render(request, "test/optionDetails.html", context)


@decorators.login_required()
def finishTest(request, testId):
    test = UserTest.objects.filter(
        test=testId, user=request.user, isFinished=False
    ).all()
    if test:
        test = test[0]
    else:
        return redirect("testApp:detailsTest", testId=testId)
    questions = [Question.objects.filter(id=i).all()[0] for i in test.question_pool]
    total_score = 0
    max_score = 0
    for question in questions:
        question_right = question.weight
        max_score += question_right
        user_answers = UserAnswer.objects.filter(
            user=request.user, test=test, quest=question
        ).all()
        if user_answers:
            for user_ans in user_answers:

                if user_ans.answer != user_ans.opt.isRight:
                    question_right = 0
                    break
        else:
            question_right = 0

        total_score += question_right
    test.points = total_score
    test.time_end = datetime.now().isoformat()
    test.isFinished = True
    test.save()
    context = {
        "user_test": test,
        "max_score": max_score,
        "percentage": round(test.points / max_score * 100, 2),
    }
    return render(request, "test/finishTest.html", context)


@decorators.login_required
def user_stat(request):
    if not request.user.is_staff:
        user_tests = UserTest.objects.filter(user=request.user, isFinished=True).all()[
            ::-1
        ]
    else:
        user_tests = UserTest.objects.filter(isFinished=True).all()[::-1]
    tests = list(enumerate(user_tests))
    max_scores = []
    for test in user_tests:
        questions = Question.objects.filter(test=test.test).all()
        max_score = 0
        for question in questions:
            question_right = question.weight
            max_score += question_right
        max_scores += [max_score]

    context = {"tests": list(zip(user_tests, max_scores))}

    return render(request, "test/userDetails.html", context)
