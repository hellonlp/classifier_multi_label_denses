# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:23:12 2018

@author: cm
"""



import os
import sys
pwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(pwd)
from classifier_multi_label_textcnn.utils import load_vocabulary


class Hyperparamters:
    # Train parameters
    num_train_epochs = 20
    print_step = 100
    batch_size = 8#64           
    summary_step = 10
    num_saved_per_epoch = 3
    max_to_keep = 100
    logdir = 'logdir/CML_Denses'
    file_save_model = 'model/CML_Denses'
    inference_model = 'CML_Denses'
    
    # Train/Test data
    data_dir = os.path.join(pwd,'data')
    train_data = 'train_onehot.csv'
    test_data = 'test_onehot.csv'    
    
    
    # Load vocabulcary dict
    dict_id2label,dict_label2id = load_vocabulary(os.path.join(pwd,'data','vocabulary_label.txt') )
    label_vocabulary = list(dict_id2label.values())

    # Optimization parameters
    warmup_proportion = 0.1    
    use_tpu = None
    do_lower_case = True    
    learning_rate = 5e-5     

    
    # Sequence and Label
    sequence_length = 60
    num_labels = len(list(dict_id2label))    
        
    # ALBERT
    model = 'albert_small_zh_google'
    bert_path = os.path.join(pwd,model)
    vocab_file = os.path.join(pwd,model,'vocab_chinese.txt')
    init_checkpoint = os.path.join(pwd,model,'albert_model.ckpt')
    saved_model_path = os.path.join(pwd,'model')    
    
   
    
    
    
    
    
    


    
    