"""
Configuration for training SiamFC and tracking evaluation
Written by Heng Fan
"""


class Config:
    def __init__(self):
        # parameters for training
        self.pos_pair_range = 100
        self.num_pairs = 5.32e4
        self.val_ratio = 0.1
        self.num_epoch = 50
        self.batch_size = 8
        self.examplar_size = 127
        self.instance_size = 255
        self.sub_mean = 0
        self.train_num_workers = 16  # number of threads to load data when training
        self.val_num_workers = 8
        self.stride = 8
        self.rPos = 16
        self.rNeg = 0
        self.label_weight_method = "balanced"

        self.lr = 1e-2               # learning rate of SGD
        self.momentum = 0.9          # momentum of SGD
        self.weight_decay = 5e-4     # weight decay of optimizator
        self.step_size = 1           # step size of LR_Schedular
        self.gamma = 0.8685          # decay rate of LR_Schedular

        # parameters for tracking (SiamFC-3s by default)
        self.num_scale = 3
        self.scale_step = 1.0375
        self.scale_penalty = 0.9745
        self.scale_LR = 0.59
        self.response_UP = 16
        self.windowing = "cosine"
        self.w_influence = 0.176

        self.video = "bird1_1"
        self.visualization = 0
        self.bbox_output = True
        self.bbox_output_path = "./tracking_result_OTB-100/"

        self.context_amount = 0.5
        self.scale_min = 0.2
        self.scale_max = 5
        self.score_size = 17

        # path to your trained model
        self.net_base_path = "/home/deeplearning/tian/siam-torch/Train/model"
        self.net_S_path = "/home/deeplearning/tian/siam-torch/Train/modelS"
        # path to your sequences (sequence should be in OTB format)
        self.seq_base_path = "/home/deeplearning/tian/siam-torch/data/OTB-100"
        # which model to use
        self.net = "SiamFC_51_model.pth"
        self.netS='SiamFC_30_model.pth'