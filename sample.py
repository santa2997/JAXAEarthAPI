from jaxa.earth import je

dlim = ["2024-01-04T00:00:00", "2024-01-05T23:59:00"]
ppu = 20
bbox = [129, 30, 133, 35]

data = je.ImageCollection("JAXA.G-Portal_GCOM-C.SGLI_standard.L3-LST.daytime.v3_global_daily", ssl_verify=True)\
        .filter_date(dlim=dlim)\
        .filter_resolution(ppu=ppu)\
        .filter_bounds(bbox=bbox)\
        .select("LST")\
        .get_images()

img = je.ImageProcess(data).show_images()