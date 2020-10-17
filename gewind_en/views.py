from .models import Coordinates,ProjectInfo,Color, Uploadfile
from extra_views import CreateWithInlinesView, InlineFormSet
from gewind_en.kmz_generator import main_run
from django.http import HttpResponse, HttpResponseNotFound
import mimetypes
from django.views import generic
from .models import Uploadfile

class About(generic.TemplateView):
    template_name= 'gewind_en/about.html'

class Example(generic.ListView):
    model = Uploadfile
    ordering = ['file']

class Top(generic.TemplateView):
    template_name= 'gewind_en/top.html'

class Howto(generic.TemplateView):
    template_name= 'gewind_en/howto.html'

class CoordinateFormView(InlineFormSet):
    model = Coordinates
    fields = ('turbine_name','lon','lat')
    factory_kwargs={'can_delete':False,'extra':10}

class ProjectInfoFormsetView(CreateWithInlinesView):
    model = ProjectInfo
    fields = ('proj_id', 'color', 'heading',
              'hub_height', 'blade_length','appearance','paint_it_black')
    inlines = [CoordinateFormView,]
    template_name = "gewind_en/projectinfo_formset.html"
    slug_field = 'id'
    success_url = "dl/{id}/"

def dl(request, slug):
    print(f'ProjectInfo id:{slug}')

    #-----Uncomment when the color has a problem
    # print(Color.objects.all().values())
    #-----

    proj_info_dic = ProjectInfo.objects.all().values().filter(id=slug)
    pro_id_id=proj_info_dic[0]['id']

    proj_id = proj_info_dic[0]['proj_id']
    coor_info_dic = Coordinates.objects.all().values().filter(export_id=pro_id_id)

    #----- Uncomment when the input data has a problem
    # print(proj_info_dic)
    # print(coor_info_dic )
    #-----

    color = proj_info_dic[0]['color_id']
    heading = proj_info_dic[0]['heading']
    random_rotation = proj_info_dic[0]['appearance']
    paint_it_black = proj_info_dic[0]['paint_it_black']  # 10/05
    hub_height = proj_info_dic[0]['hub_height']
    roter_radius_input = proj_info_dic[0]['blade_length']

    lon_ls = []
    lat_ls = []
    turbine_num_ls = []

    for dic in coor_info_dic:
        if dic['turbine_name']=="":
            turbine_num_ls.append("WT")
        else:
            turbine_num_ls.append(dic['turbine_name'])

        lon_ls.append(dic['lon'])
        lat_ls.append(dic['lat'])

    main_run.main_run_all(roter_radius_input,lon_ls,lat_ls,hub_height,heading,random_rotation,color,turbine_num_ls,slug,proj_id,paint_it_black)#10/05

    fl_path = './tmp/' #Heroku対応
    filename = f'output_{slug}.kmz'
    file_location = f'{fl_path}{filename}'

    try:
        '''
        Use 'rb' instead of 'r' for open()
        Source: https://stackoverflow.com/questions/19459300/how-to-serve-downloadable-zip-file-in-django
        '''
        kmz_file = open(file_location, 'rb')
        mime_type, _ = mimetypes.guess_type(file_location) #mime_type is application/vnd.google-earth.kmz
        response = HttpResponse(kmz_file, content_type=mime_type)
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response

#----ToDo: Check----
# def download(request,path):
#     file_path=os.path.join(settings.MEDIA_ROOT,path)
#     print('!!!!')
#     print(file_path)
#     print('!!!!')
#     if os.path.exists(file_path):
#         with open(file_path,'rb')as fh:
#             response=HttpResponse(fh.read(),content_type="application/file")
#             response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
#             return response
#     raise Http404


#----ToDo: Check----
# class Thanks(generic.TemplateView):
#     model = ProjectInfo
#     slug_field = 'proj_id'
#     extra_context = {'proj_id': '<str:slug>'}
#     template_name='gewind_en/thanks.html'

#----ToDo: Check----
# def index(request):
#     ExampleFormSet=modelformset_factory(Coordinates,
#                                         fields=('turbine_name','lon','lat','proj_id'),
#                                         extra=10)
#     if request.method=='POST':
#         form = ExampleFormSet(request.POST)
#         instances = form.save(commit=False)
#         for instance in instances:
#             instance.save()
#     # querysetによって表示するデータの種類をコントロールする。
#     form = ExampleFormSet(queryset=Coordinates.objects.none())
#     return render(request,'gewind_en/coordinates_form.html',{'form':form})

#----ToDo: Check----
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST)#, request.FILES)
#         if form.is_valid():
#             instance = Uploadfile(file_field=request.FILES['file'])
#             instance.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

