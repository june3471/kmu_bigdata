from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Boards, Board_menu, File
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'all_board'
    model = Boards
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        q = self.request.GET.get("search",'')
        if q != '':
            context['search_result'] = q
            return context
        else:
            context['search_result'] = ''
            return context

    def get_queryset(self):
        board_list = Boards.objects.all()
        board_menus = Board_menu.objects.all()
        if self.request.GET.get('search'):
            q_string = self.request.GET.get('search')
            if q_string != '':
                board_list = self.model.objects.filter(b_title__icontains = q_string)
            else:
                board_list = self.model.objects.all()
        return board_list

def index(request):
    context = {}

    q = request.GET.get('search','')


    board_list = Boards.objects.all()
    board_menus = Board_menu.objects.all().order_by('b_order')

    if q:
        q_string = request.GET.get('search')
        if q_string != '':
            board_list = Boards.objects.filter(b_title__icontains=q_string)
            context['search_result'] = q
        else:
            board_list = Boards.objects.all()

    context['all_board'] = board_list
    context['board_menu'] = board_menus
    return render(request, 'pages/index.html', context)

def menu(request, b_type):
    context = {}
    q = request.GET.get('search','')

    b_menu_id = Board_menu.objects.filter(b_type = b_type)
    board_menus = Board_menu.objects.all().order_by('b_order')
    files = File.objects.all()
    context['board_menu'] = board_menus

    if b_type != '':
        board_list = Boards.objects.filter(b_type = b_menu_id[0].id)
    else:
        board_list = Boards.objects.all()
    context['all_board'] = board_list
    context['all_file'] = files
    context['real_all_board'] = Boards.objects.all()

    if q:
        q_string = request.GET.get('search')

        if q_string != '':
            board_list = Boards.objects.filter(b_title__icontains=q_string, b_type=b_menu_id[0].id)

            files = File.objects.filter(f_title__icontains=q_string)
            context['search_result'] = q
            context['all_board'] = board_list
            context['all_file'] = files
    #데이터셋 쿼리 부분


    if board_list:
        context['b_id'] = board_list[0].b_type
    if b_type == 'intro':
        return render(request, 'pages/intro.html', context)
    elif b_type == 'rapidminer':
        return render(request, 'pages/rapidminer.html', context)
    elif b_type == 'tableau':
        return render(request, 'pages/tableau.html', context)
    elif b_type == 'deeplearning':
        return render(request, 'pages/deeplearning.html', context)
    elif b_type == 'R':
        return render(request, 'pages/R.html', context)
    elif b_type == 'data':
        return render(request, 'pages/data.html', context)



def detail(request, b_type ,id):
    board_menus = Board_menu.objects.all().order_by('b_order')

    context = {}
    context['board_menu'] = board_menus
    context['real_all_board'] = Boards.objects.all()


    if b_type == 'data':
        files = get_object_or_404(File, pk=id)
        context['files'] = files
        return render(request, 'pages/detail.html', context)
    else:
        board = get_object_or_404(Boards, pk=id)
        context['board'] = board
        return render(request, 'pages/detail.html', context)

