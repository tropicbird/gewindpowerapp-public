def change_kml(lon_ls,lat_ls,hub_height,roter_radius,heading,random_rotation,path,slug,paint_it_black):
    print('Start: change_kml')

    import numpy as np
    import os
    import random

    l = ['<roll>0</roll>', '<roll>120</roll>', '<roll>240</roll>']

    base_folder=path+"base_txt/"
    new_folder = f"./tmp/{slug}/{path}new_txt/"  # heroku対応9/30
    os.makedirs(new_folder)

    if paint_it_black:
        txt_files = ['blade_3set_pib.txt', 'hub.txt', 'nacelle.txt']
    else:
        txt_files=['blade_3set.txt','hub.txt','nacelle.txt']

    for file_name in txt_files:
        for i, (lon, lat) in enumerate(zip(lon_ls,lat_ls)):
            with open(base_folder+file_name, encoding="utf-8") as f:
                data_lines = f.read()

            # 文字列置換
            data_lines = data_lines.replace('<longitude>XXX</longitude>', f'<longitude>{lon}</longitude>')
            data_lines = data_lines.replace('<latitude>XXX</latitude>', f'<latitude>{lat}</latitude>')
            data_lines = data_lines.replace('<altitude>XXX</altitude>', f'<altitude>{hub_height}</altitude>')
            data_lines = data_lines.replace('<heading>XXX</heading>', f'<heading>{heading}</heading>')

            if file_name=='hub.txt':
                data_lines = data_lines.replace('<z>XXX</z>', f'<z>{hub_height}</z>')
            if file_name=='blade_3set.txt' or file_name=='blade_3set_pib.txt':
                data_lines = data_lines.replace('<z>XXX</z>', f'<z>{roter_radius}</z>')
                if random_rotation:
                    rotation = (np.random.rand(1)*120)[0]#360以上は全て0になるため
                    random.shuffle(l)
                    data_lines = data_lines.replace(l[0], f'<roll>{rotation}</roll>')
                    data_lines = data_lines.replace(l[1], f'<roll>{rotation+120}</roll>')
                    data_lines = data_lines.replace(l[2], f'<roll>{rotation+240}</roll>')

            num=str(i).rjust(3, '0')
            with open(new_folder+num+file_name, mode="w", encoding="utf-8") as f:
                f.write(data_lines)

    print('End: change_kml')

def change_color(color,path,slug,paint_it_black):
    print('Start: change_color')

    import os

    colors={1:"0.75 0.75 0.75 1", #Gray
            2:"0 0 0 1", #Black
            3: "1 1 1 1", #White
            4:"1 0 0 1", #Red
            5:"0 1 0 1", #Green
            6:"0 0 1 1", #Blue
            7:"1 1 0 1", #Yellow
            8:"0.90 0.90 0.90 1"} #White Gray

    if paint_it_black:
        dae_files = ['hub.dae',
                     'blade.dae',
                     'nacelle.dae',
                     'blade_paint_it_black_bottom.dae']
    else:
        dae_files = ['hub.dae',
                     'blade.dae',
                     'nacelle.dae']
    base_folder=path+"base_dae/"
    output_folder =f"./tmp/{slug}/{path}output_base/files/"
    os.makedirs(output_folder)

    for file_name in dae_files:
        with open(base_folder+file_name, encoding="utf-8") as f:
            data_lines = f.read()

        # 文字列置換
        data_lines = data_lines.replace('<color sid="diffuse">1 1 1 1</color>', f'<color sid="diffuse">{colors[color]}</color>')

        with open(output_folder+file_name, mode="w", encoding="utf-8") as f:
            f.write(data_lines)

    if paint_it_black:
        from shutil import copyfile
        copyfile(base_folder+'blade_paint_it_black_top.dae', output_folder+'blade_paint_it_black_top.dae')

    print('End: change_color')

def make_kml(turbine_num_ls,path,proj_id,slug):
    print('Start: make_kml')

    import os
    location = f"./tmp/{slug}/{path}new_txt/"

    for dirname, _, filenames in os.walk(location):
        pass
    filenames.sort()

    base_folder = path+'base_txt/'
    output_folder = f"./tmp/{slug}/{path}output_base/"

    combined_output_turbine_lines=''

    with open(base_folder+'output.txt',encoding="utf-8") as f:
        output_lines=f.read()

    for j, turbine_num in enumerate(turbine_num_ls):
        with open(base_folder+'output_turbine.txt',encoding="utf-8") as f:
            output_turbine_lines=f.read()

        each_turbine = ''
        for file_name in filenames[j*3:j*3+3]:
            with open(location+file_name, encoding="utf-8") as f:
                data_lines = f.read()
            each_turbine+=data_lines
        output_turbine_lines = output_turbine_lines.replace('INSERT_PLACEMARK_HERE', each_turbine)
        output_turbine_lines = output_turbine_lines.replace('TURBINE_NAME', turbine_num)
        combined_output_turbine_lines+=output_turbine_lines

    # 文字列置換
    output_lines = output_lines.replace('PROJ_ID_HERE', proj_id)
    output_lines = output_lines.replace('INSERT_PLACEMARK_HERE', combined_output_turbine_lines)

    with open(output_folder+'output.kml', mode="w", encoding="utf-8") as f:
        f.write(output_lines)
    print('End: make_kml')

def make_kmz(slug,path):
    print('Start: make_kmz')

    import shutil
    import os

    shutil.make_archive(f"./tmp/output_{slug}", 'zip',
                        root_dir=f"./tmp/{slug}/{path}output_base")

    old_file_name = f"./tmp/output_{slug}.zip"
    new_file_name = f"./tmp/output_{slug}.kmz"

    try:
        os.rename(old_file_name,new_file_name)
    except Exception as e:
        print(e)
        os.remove(new_file_name)
        os.rename(old_file_name,new_file_name)

    print('End: make_kmz')

def delete_tmp_files(slug):
    print('Start: delete_tmp_files')

    import time
    import shutil

    time.sleep(1)

    try:
        shutil.rmtree(f'./tmp/{slug}/')  # heroku対応9/30
        print(f'tmp/{slug}/ are deleted!')
    except Exception as e:
        print(e)
        print('tmp file is not deleted!!')

    print('End: delete_tmp_files')