
def main_run_all(roter_radius_input,lon_ls,lat_ls,hub_height,heading,random_rotation,color,turbine_num_ls,slug,proj_id,paint_it_black):
    print("-----Start: main_run_all-----")

    from gewind.kmz_generator.modules import makekmz

    roter_radius=roter_radius_input/60
    path='gewind/kmz_generator/'

    makekmz.change_kml(lon_ls, lat_ls, hub_height, roter_radius, heading, random_rotation,path,slug,paint_it_black)
    makekmz.change_color(color,path,slug,paint_it_black)
    makekmz.make_kml(turbine_num_ls,path,proj_id,slug)
    makekmz.make_kmz(slug,path)

    #----ToDo：ローカル環境ではshutil.rmtreeが[Errno 13] Permission deniedになる。----
    makekmz.delete_tmp_files(slug)  # herokuのメモリ節約のため
    #-----------

    print("-----End: main_run_all-----")