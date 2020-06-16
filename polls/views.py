from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, Http404
from analysis.word.word_dictionary import get_worddictionary
from analysis.utils.util import upload_files, read_text


def index(request):
    return render(request, 'polls/index.html')


@csrf_exempt
def analysis(request):
    if request.method == "POST":
        # input json parameter

        run_type = request.POST['type']

        text = request.POST['context']
        stopWord = request.POST['stopWordList']
        stopWordList = stopWord.split('^')
        count = int(request.POST['countKeyWord'])

        if run_type == "wordCount":
            word_dict, cloud_path = get_worddictionary(text, additional_stop_word=stopWordList, count=count)
        else:
            word_dict, cloud_path = get_worddictionary(text, additional_stop_word=stopWordList, count=count)

        context = {
            'dictList': word_dict,
            'cloudPath': cloud_path
        }
        return JsonResponse(context)

    else:
        context = {'text', 'get_form'}

        return JsonResponse(context)


@csrf_exempt
def upload(request):
    if request.method == "POST":
        result = False

        try:
            file = request.FILES['files']
            ext = file.name.split('.').pop()

            dir_path = upload_files()

            idx = 0
            new_file = '%s.%s' % (idx, ext)

            destination = open(dir_path + new_file, 'wb+')

            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()

            text = read_text(dir_path+new_file, 'utf-8')

            result = True
        except:
            raise Http404

        context = {
            "result": result,
            "text"  : text  ,
        }

        return JsonResponse(context)
