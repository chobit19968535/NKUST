"""
Retrain the YOLO model for your own dataset.
"""
# =============================================================================
# Plot Model
# =============================================================================
from keras.utils import plot_model
import os
os.environ["PATH"] += os.pathsep + 'C://Program Files (x86)//Graphviz2.38//bin//'
# =============================================================================
# Creat_Ground_Truth to fuck my ass

# =============================================================================


# =============================================================================
# Import
# =============================================================================
import numpy as np
import keras.backend as K
from keras.layers import Input, Lambda
from keras.models import Model
from keras.optimizers import Adam, SGD, Nadam, RMSprop
from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau, EarlyStopping

from yolo3.model import preprocess_true_boxes, yolo_body, tiny_yolo_body, yolo_loss
from yolo3.utils import get_random_data
import gc



def _main(i):
    flip, max_boxes, jitter, hue, sat, val, iou, leaky = i
    annotation_path = 'annotation_train.txt'
    classes_path = 'classes.txt'
    anchors_path = 'yolo_anchors.txt'
    class_names = get_classes(classes_path)
    num_classes = len(class_names)
    anchors = get_anchors(anchors_path)

    input_shape = (480,640) # multiple of 32, hw

    is_tiny_version = len(anchors)==6 # default setting
    if is_tiny_version:
        model = create_tiny_model(input_shape, anchors, num_classes,
            freeze_body=2, weights_path='model_data/tiny_yolo_weights.h5')
    else:
        weights_path = 'Models/leaky' + leaky + '_320.h5'
        print(weights_path)
        model = create_model(input_shape, anchors, num_classes,
            freeze_body=2, weights_path = weights_path, iou = iou) # make sure you know what you freeze

    logging = TensorBoard(log_dir=log_dir)
    #ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}-train_loss{train_loss:.3f}.h5',
        #monitor='train_loss', save_weights_only=True, save_best_only=True, period=3)
    checkpoint = ModelCheckpoint(log_dir + 'ep{epoch:03d}.h5',
        monitor='val_loss', save_weights_only=True, save_best_only=True, period=2)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, verbose=1)
    early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=25, verbose=1)

    val_split = 0
    with open(annotation_path) as f:
        lines = f.readlines()
    with open('annotation_val.txt') as f:
        val_lines = f.readlines()
    np.random.seed(426)
    np.random.shuffle(lines)
    num_val = int(len(lines)*val_split)
    num_train = len(lines) - num_val
    
#    with open('train.txt', 'w') as f:
#        [f.write(l) for l in lines[ :num_train]]  
#    
#    with open('val.txt', 'w') as f:
#        [f.write(l) for l in lines[num_train : ]]

    # Train with frozen layers first, to get a stable loss.
    # Adjust num epochs to your dataset. This step is enough to obtain a not bad model.
    if True:
        model.compile(optimizer=SGD(lr = 1e-3, momentum = 0.5), loss={
            # use custom yolo_loss Lambda layer.
            'yolo_loss': lambda y_true, y_pred: y_pred})

        batch_size = 35
        print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
        history_freeze = model.fit_generator(data_generator_wrapper(lines[:num_train], batch_size, input_shape, anchors, num_classes, flip, max_boxes, jitter, hue, sat, val),
                steps_per_epoch=max(1, num_train//batch_size),
                validation_data=data_generator_wrapper(val_lines, batch_size, input_shape, anchors, num_classes, flip, max_boxes, jitter, hue, sat, val),
                validation_steps=max(1, num_val//batch_size),
                epochs=80,
                initial_epoch=0,
                callbacks=[logging, checkpoint])
        model.save_weights(log_dir + 'trained_weights_stage_1.h5')

    # Unfreeze and continue training, to fine-tune.
    # Train longer if the result is not good.
    if True:
        for i in range(len(model.layers)):
            model.layers[i].trainable = True
        model.compile(optimizer=SGD(lr = 1e-3, momentum = 0.5), loss={'yolo_loss': lambda y_true, y_pred: y_pred}) # recompile to apply the change
        print('Unfreeze all of the layers.')

        batch_size = 4 # note that more GPU memory is required after unfreezing the body
        print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
        history_unfreeze = model.fit_generator(data_generator_wrapper(lines[:num_train], batch_size, input_shape, anchors, num_classes,flip, max_boxes, jitter, hue, sat, val),
            steps_per_epoch=max(1, num_train//batch_size),
            validation_data=data_generator_wrapper(val_lines, batch_size, input_shape, anchors, num_classes, flip, max_boxes, jitter, hue, sat, val),
            validation_steps=max(1, num_val//batch_size),
            epochs=100,
            initial_epoch=80,
            callbacks=[logging, checkpoint, reduce_lr, early_stopping])
        model.save_weights(log_dir + 'trained_weights_final.h5')
        plot_model(model, log_dir + 'Yolov3.png')
        return([history_freeze, history_unfreeze])
        

    # Further training if needed.


def get_classes(classes_path):
    '''loads the classes'''
    with open(classes_path) as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names

def get_anchors(anchors_path):
    '''loads the anchors from a file'''
    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = [float(x) for x in anchors.split(',')]
    return np.array(anchors).reshape(-1, 2)


def create_model(input_shape, anchors, num_classes, load_pretrained=True, freeze_body=2,
            weights_path='model_data/yolo_weights.h5', iou = 0.0005):
    '''create the training model'''
    K.clear_session() # get a new session
    image_input = Input(shape=(None, None, 3))
    h, w = input_shape
    num_anchors = len(anchors)

    y_true = [Input(shape=(h//{0:32, 1:16, 2:8}[l], w//{0:32, 1:16, 2:8}[l], \
        num_anchors//3, num_classes+5)) for l in range(3)]

    model_body = yolo_body(image_input, num_anchors//3, num_classes)
    print('Create YOLOv3 model with {} anchors and {} classes.'.format(num_anchors, num_classes))

    if load_pretrained:
        model_body.load_weights(weights_path, by_name=True, skip_mismatch=True)
        print('Load weights {}.'.format(weights_path))
        if freeze_body in [1, 2]:
            # Freeze darknet53 body or freeze all but 3 output layers.
            num = (185, len(model_body.layers)-3)[freeze_body-1]
            for i in range(num): model_body.layers[i].trainable = False
            print('Freeze the first {} layers of total {} layers.'.format(num, len(model_body.layers)))

    model_loss = Lambda(yolo_loss, output_shape=(1,), name='yolo_loss',
        arguments={'anchors': anchors, 'num_classes': num_classes, 'ignore_thresh': iou})(
        [*model_body.output, *y_true])
    model = Model([model_body.input, *y_true], model_loss)

    return model

def create_tiny_model(input_shape, anchors, num_classes, load_pretrained=True, freeze_body=2,
            weights_path='model_data/tiny_yolo_weights.h5'):
    '''create the training model, for Tiny YOLOv3'''
    K.clear_session() # get a new session
    image_input = Input(shape=(None, None, 3))
    h, w = input_shape
    num_anchors = len(anchors)

    y_true = [Input(shape=(h//{0:32, 1:16}[l], w//{0:32, 1:16}[l], \
        num_anchors//2, num_classes+5)) for l in range(2)]

    model_body = tiny_yolo_body(image_input, num_anchors//2, num_classes)
    print('Create Tiny YOLOv3 model with {} anchors and {} classes.'.format(num_anchors, num_classes))

    if load_pretrained:
        model_body.load_weights(weights_path, by_name=True, skip_mismatch=True)
        print('Load weights {}.'.format(weights_path))
        if freeze_body in [1, 2]:
            # Freeze the darknet body or freeze all but 2 output layers.
            num = (20, len(model_body.layers)-2)[freeze_body-1]
            for i in range(num): model_body.layers[i].trainable = False
            print('Freeze the first {} layers of total {} layers.'.format(num, len(model_body.layers)))

    model_loss = Lambda(yolo_loss, output_shape=(1,), name='yolo_loss',
        arguments={'anchors': anchors, 'num_classes': num_classes, 'ignore_thresh': 0.7})(
        [*model_body.output, *y_true])
    model = Model([model_body.input, *y_true], model_loss)
    return model

def data_generator(annotation_lines, batch_size, input_shape, anchors, num_classes, flip, max_boxes, jitter, hue, sat, val):
    '''data generator for fit_generator'''
    n = len(annotation_lines)
    i = 0
    while True:
        image_data = []
        box_data = []
        for b in range(batch_size):
            if i==0:
                np.random.shuffle(annotation_lines)
            image, box = get_random_data(annotation_lines[i], input_shape, random=True, flip = flip, max_boxes = max_boxes, jitter = jitter, hue = hue, sat = sat, val = val)
            image_data.append(image)
            box_data.append(box)
            i = (i+1) % n
        image_data = np.array(image_data)
        box_data = np.array(box_data)
        y_true = preprocess_true_boxes(box_data, input_shape, anchors, num_classes)
        yield  [image_data, *y_true], np.zeros(batch_size) 

def data_generator_wrapper(annotation_lines, batch_size, input_shape, anchors, num_classes, flip, max_boxes, jitter, hue, sat, val):
    n = len(annotation_lines)
    if n==0 or batch_size<=0: return None
    return data_generator(annotation_lines, batch_size, input_shape, anchors, num_classes, flip, max_boxes, jitter, hue, sat, val)



def plot(history):
    # =============================================================================
    #                   Plot Training Information
    # =============================================================================
    import matplotlib.pyplot as plt
    #define filepath parms
    name = ['freezy', 'unfreezy']
    for index, info in enumerate(history):
        loss_trend_graph_path = log_dir + "loss_" + name[index] + ".jpg" 
        print("Now,we start drawing the loss trends graph...")
        #summarize history for accuracy 
        fig = plt.figure(1)
        plt.plot(info.history["loss"])  
        #plt.plot(history.history["val_acc"])  
        plt.title("Model Loss_" + name[index])  
        plt.ylabel("loss")  
        plt.xlabel("epoch")  
        plt.legend(["train"],loc="upper left")  
        plt.savefig(loss_trend_graph_path) 
        plt.close(1)

    print("We are done, everything seems OK...")

if __name__ == '__main__':
    # Exp 1~18
    exp_list = [
#                ["True", 20, 0.3, 0.1, 0.5, 0.5, 0.5, "005"],   #01
#                ["True", 20, 0.55, 0.4, 1.5, 1.5, 0.3, "010"],  #02
#                ["True", 20, 0.8, 0.7, 2.5, 2.5, 0.7, "020"],   #03
#                ["True", 40, 0.3, 0.1, 1.5, 1.5, 0.7, "020"],   #04
#                ["True", 40, 0.55, 0.4, 2.5, 2.5, 0.5, "005"],  #05
#                ["True", 40, 0.8, 0.7, 0.5, 0.5, 0.3, "010"],   #06
#                ["True", 60, 0.3, 0.4, 0.5, 2.5, 0.3, "020"],   #07
#                ["True", 60, 0.55, 0.7, 1.5, 0.5, 0.7, "005"],  #08
#                ["True", 60, 0.8, 0.1, 2.5, 1.5, 0.5, "010"],   #09
#                ["False", 20, 0.3, 0.7, 2.5, 1.5, 0.3, "005"],  #10
#                ["False", 20, 0.55, 0.1, 0.5, 2.5, 0.7, "010"], #11
#                ["False", 20, 0.8, 0.4, 1.5, 0.5, 0.5, "020"],  #12
                ["False", 40, 0.3, 0.4, 2.5, 0.5, 0.7, "010"],  #13
#                ["False", 40, 0.55, 0.7, 0.5, 1.5, 0.5, "020"], #14
#                ["False", 40, 0.8, 0.1, 1.5, 2.5, 0.3, "005"],  #15
#                ["False", 60, 0.3, 0.7, 1.5, 2.5, 0.5, "010"],  #16
#                ["False", 60, 0.55, 0.1, 2.5, 0.5, 0.3, "020"], #17
#                ["False", 60, 0.8, 0.4, 0.5, 1.5, 0.7, "005"],  #18                
                ]
    for index, val in enumerate(exp_list):
        index += 13 # shift exps
        log_dir_tmp = 'logs/320_uniform_exp' + str(index)
        for j in range(3):
            log_dir = log_dir_tmp + '_y' + str(j+1) + '/'
            print("Now running exp: {} ".format(log_dir))
            history = _main(val)
            plot(history)
            K.clear_session()
            gc.collect()
            del history
