import sys
import time
sys.path.append("..")
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import baseline.baseline_config as config
import baseline.baseline_utils as utils

def svm_model(is_pac=False,n=0.9):
    start = time.time()
    features = np.load(config.feature_path)
    label = np.load(config.label_path)
   #features, label = utils.under_sampling(features, label)
    x_train, x_test, y_train, y_test = train_test_split(features, label, test_size=0.1, shuffle=True,
                                                  random_state=config.random_seed)
    if(is_pac):
        x_train,x_text=utils.pca_components_analysis(n,x_train,x_test)
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)
    estimator = SVC()
    estimator.fit(x_train, y_train)
    accuracy = estimator.score(x_test, y_test)
    end = time.time()
    print("准确率是:{}, 消耗时间是:{}s".format(accuracy, int(end - start)))
    return accuracy


if __name__ == '__main__':
    svm_model(is_pac=False)

