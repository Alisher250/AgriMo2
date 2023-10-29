import argparse
import time
from pathlib import Path
import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random
import pygame
import os
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel
import psycopg2

# Configuration from your Django settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'f31GBd5cBb1-gF26Ccgc*G6g3B353gf-',
        'HOST': 'monorail.proxy.rlwy.net',
        'PORT': '22467',
    }
}

def update_record(value, name):
    try:
        conn = psycopg2.connect(
            dbname=DATABASES['default']['NAME'],
            user=DATABASES['default']['USER'],
            password=DATABASES['default']['PASSWORD'],
            host=DATABASES['default']['HOST'],
            port=DATABASES['default']['PORT']
        )
        cursor = conn.cursor()
        cursor.execute("UPDATE main_statistics SET value = %s WHERE name = %s", (value, name))
        conn.commit()
        print("Record updated successfully.")
    except psycopg2.Error as e:
        print("Error: Unable to update record")
        print(e)
    finally:
        if conn:
            conn.close()

def detect(save_img=False):
    source, weights, view_img, save_txt, imgsz, trace = opt.source, opt.weights, opt.view_img, opt.save_txt, opt.img_size, not opt.no_trace
    save_img = not opt.nosave and not source.endswith('.txt')
    webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(
        ('rtsp://', 'rtmp://', 'http://', 'https://'))
    save_dir = Path(increment_path(Path(opt.project) / opt.name, exist_ok=opt.exist_ok)) 
    (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  
    set_logging()
    device = select_device(opt.device)
    half = False
    if(device.type != 'cpu'):
        compute_capability = torch.cuda.get_device_capability(device=device)    
        half = (device.type != 'cpu') and (compute_capability[0] >= 8)  
    model = attempt_load(weights, map_location=device)  
    stride = int(model.stride.max())
    imgsz = check_img_size(imgsz, s=stride) 
    if trace:
        model = TracedModel(model, device, opt.img_size)
    if half:
        model.half()
    classify = False
    if classify:
        modelc = load_classifier(name='resnet101', n=2) 
        modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model']).to(device).eval()
    vid_path, vid_writer = None, None
    if webcam:
        view_img = check_imshow()
        cudnn.benchmark = True
        dataset = LoadStreams(source, img_size=imgsz, stride=stride)
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride)
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  
    old_img_w = old_img_h = imgsz
    old_img_b = 1
    t0 = time.time()
    counter_beans_angular_leafspot = 0
    ссbeans_angular_leafspot = 0
    counter_beans_rust = 0
    ссbeans_rust = 0
    counter_strawberry_angular_leafspot = 0
    ссstrawberry_angular_leafspot = 0
    counter_strawberry_anthracnose_fruit_rot = 0
    ссstrawberry_anthracnose_fruit_rot = 0
    counter_strawberry_blossom_blight = 0
    ссstrawberry_blossom_blight = 0
    counter_strawberry_gray_mold = 0
    ссstrawberry_gray_mold = 0
    counter_strawberry_leaf_spot = 0
    ссstrawberry_leaf_spot = 0
    counter_strawberry_powdery_mildew_fruit = 0
    ссstrawberry_powdery_mildew_fruit = 0
    counter_strawberry_powdery_mildew_leaf = 0
    ссstrawberry_powdery_mildew_leaf = 0
    counter_tomato_blight = 0
    ссtomato_blight = 0
    counter_tomato_leaf_mold = 0
    cctomato_leaf_mold = 0
    counter_tomato_spider_mites = 0
    ссtomato_spider_mites = 0

    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float() 
        img /= 255.0 
        if img.ndimension() == 3:
            img = img.unsqueeze(0)
        if device.type != 'cpu' and (old_img_b != img.shape[0] or old_img_h != img.shape[2] or old_img_w != img.shape[3]):
            old_img_b = img.shape[0]
            old_img_h = img.shape[2]
            old_img_w = img.shape[3]
            for i in range(3):
                model(img, augment=opt.augment)[0]
        t1 = time_synchronized()
        with torch.no_grad():
            pred = model(img, augment=opt.augment)[0]
        t2 = time_synchronized()
        pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes, agnostic=opt.agnostic_nms)
        t3 = time_synchronized()

        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        for i, det in enumerate(pred):
            if webcam:
                p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), dataset.count
            else:
                p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 0)

            p = Path(p)
            save_path = str(save_dir / p.name)
            txt_path = str(save_dir / 'labels' / p.stem) + ('' if dataset.mode == 'image' else f'_{frame}') 
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]] 

            if len(det):
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum() 
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, " 
                for *xyxy, conf, cls in reversed(det):
                    if save_txt: 
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()
                        line = (cls, *xywh, conf) if opt.save_conf else (cls, *xywh) 
                        with open(txt_path + '.txt', 'a') as f:
                            f.write(('%g ' * len(line)).rstrip() % line + '\n')
                    if save_img or view_img: 
                        label = f'{names[int(cls)]} {conf:.2f}'
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=1)

                        if "Tomato_Spider_Mites" in str(label):
                            counter_tomato_spider_mites += 1
                        if "Tomato_Leaf_Mold" in str(label):
                            counter_tomato_leaf_mold += 1
                        if "Tomato_Blight" in str(label):
                            counter_tomato_blight += 1
                        if "Strawberry_Powdery_Mildew_Leaf" in str(label):
                            counter_strawberry_powdery_mildew_leaf += 1
                        if "Beans_Angular_LeafSpot" in str(label):
                            counter_beans_angular_leafspot += 1
                        if "Beans_Rust" in str(label):
                            counter_beans_rust += 1
                        if "Strawberry_Angular_LeafSpot" in str(label):
                            counter_strawberry_angular_leafspot += 1
                        if "Strawberry_Anthracnose_Fruit_Rot" in str(label):
                            counter_strawberry_anthracnose_fruit_rot += 1
                        if "Strawberry_Blossom_Blight" in str(label):
                            counter_strawberry_blossom_blight += 1
                        if "Strawberry_Gray_Mold" in str(label):
                            counter_strawberry_gray_mold += 1
                        if "Strawberry_Leaf_Spot" in str(label):
                            counter_strawberry_leaf_spot += 1
                        if "Strawberry_Powdery_Mildew_Fruit" in str(label):
                            counter_strawberry_powdery_mildew_fruit += 1

                        if counter_tomato_spider_mites > 50:
                            counter_tomato_spider_mites = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            ссtomato_spider_mites += 1
                            print(ссtomato_spider_mites)
                            update_record(ссtomato_spider_mites, 1)

                        if counter_tomato_leaf_mold > 50:
                            counter_tomato_leaf_mold = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            cctomato_leaf_mold += 1
                            print(cctomato_leaf_mold)
                            update_record(cctomato_leaf_mold, 2)


                        if counter_tomato_blight > 50:
                            counter_tomato_blight = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            ссtomato_blight += 1
                            print(ссtomato_blight)
                            update_record(ссtomato_blight, 3)

                        if counter_strawberry_powdery_mildew_leaf > 50:
                            counter_strawberry_powdery_mildew_leaf = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            ссstrawberry_powdery_mildew_leaf += 1
                            print(ссstrawberry_powdery_mildew_leaf)
                            update_record(counter_strawberry_powdery_mildew_leaf, 4)


                        if counter_beans_angular_leafspot > 50:
                            counter_beans_angular_leafspot = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            ссbeans_angular_leafspot += 1
                            print(ссbeans_angular_leafspot)
                            update_record(counter_beans_angular_leafspot, 5)


                        if counter_beans_rust > 50:
                            counter_beans_rust = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            ссbeans_rust += 1
                            print(ссbeans_rust)
                            update_record(ссbeans_rust, 6)


                        if counter_strawberry_angular_leafspot > 50:
                            counter_strawberry_angular_leafspot = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            ссstrawberry_angular_leafspot += 1
                            update_record(ссstrawberry_angular_leafspot, 7)


                        if counter_strawberry_anthracnose_fruit_rot > 50:
                            counter_strawberry_anthracnose_fruit_rot = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            ссstrawberry_anthracnose_fruit_rot += 1
                            print(ссstrawberry_anthracnose_fruit_rot)
                            update_record(ссstrawberry_anthracnose_fruit_rot, 8)


                        if counter_strawberry_blossom_blight > 50:
                            counter_strawberry_blossom_blight = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            ссstrawberry_blossom_blight += 1
                            print(ссstrawberry_blossom_blight)
                            update_record(ссstrawberry_blossom_blight, 9)


                        if counter_strawberry_gray_mold > 50:
                            counter_strawberry_gray_mold = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            ссstrawberry_gray_mold += 1
                            print(ссstrawberry_gray_mold)
                            update_record(ссstrawberry_gray_mold, 10)


                        if counter_strawberry_leaf_spot > 50:
                            counter_strawberry_leaf_spot = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            ссstrawberry_leaf_spot += 1
                            print(ссstrawberry_leaf_spot)
                            update_record(ссstrawberry_leaf_spot, 11)


                        if counter_strawberry_powdery_mildew_fruit > 50:
                            counter_strawberry_powdery_mildew_fruit = 0
                            pygame.mixer.init()
                            pygame.mixer.music.load('yawn.wav')
                            pygame.mixer.music.play()
                            ссstrawberry_powdery_mildew_fruit += 1
                            print(ссstrawberry_powdery_mildew_fruit)
                            update_record(ссstrawberry_powdery_mildew_fruit, 12)

            print(f'{s}Done. ({(1E3 * (t2 - t1)):.1f}ms) Inference, ({(1E3 * (t3 - t2)):.1f}ms) NMS')
            if view_img:
                cv2.imshow(str(p), im0)
                cv2.waitKey(1)  
            if save_img:
                if dataset.mode == 'image':
                    cv2.imwrite(save_path, im0)
                    print(f" The image with the result is saved in: {save_path}")
                else:  
                    if vid_path != save_path:
                        vid_path = save_path
                        if isinstance(vid_writer, cv2.VideoWriter):
                            vid_writer.release() 
                        if vid_cap:
                            fps = vid_cap.get(cv2.CAP_PROP_FPS)
                            w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                            h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        else: 
                            fps, w, h = 30, im0.shape[1], im0.shape[0]
                            save_path += '.mp4'
                        vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                    vid_writer.write(im0)
    if save_txt or save_img:
        s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ''
    print(f'Done. ({time.time() - t0:.3f}s)')
    cv2.destroyWindow('Q')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fp16', type=bool, default=False, help="Use float16 (Some GPUs only)")
    parser.add_argument('--weights', nargs='+', type=str, default='yolov7.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='inference/images', help='source') 
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--no-trace', action='store_true', help='don`t trace model')
    opt = parser.parse_args()
    print(opt)
    with torch.no_grad():
        if opt.update: 
            for opt.weights in ['yolov7.pt']:
                detect()
                strip_optimizer(opt.weights)
        else:
            detect()