import itertools

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, KFold, cross_val_predict
from sklearn import metrics
from sklearn.tree import export_graphviz
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
import matplotlib.pyplot as plt


from html_parser import save_test_data
from html_parser import save_data


def teach():
    df = pd.read_csv("my_csv.csv")

    X = df[df.columns.difference(['label', 'id', 'class', 'filename', 'el_html'])]
    y = df[['label']]

    xgb = XGBClassifier(use_label_encoder=False)
    xgb.fit(X, y.values.ravel())

    #kfold = KFold(n_splits=10)

    #pred = cross_val_predict(xgb, X, y.values.ravel(), cv=kfold)

    #xg_conf_mat = confusion_matrix(y.values.ravel(), pred)

    return xgb


def predict(xgb):
    df = pd.read_csv("pred.csv")

    X = df[df.columns.difference(['label', 'id', 'class', 'filename', 'el_html'])]

    y_pred = xgb.predict(X)
    y_pred_proba = xgb.predict_proba(X)

    df['label'] = y_pred
    for i in range(len(y_pred_proba[0])):
        df['proba_' + str(i)] = y_pred_proba[:, i]

    df.to_csv("result.csv", mode='w', index=False)

    return df


def teach_and_predict():

    df = pd.read_csv("my_csv.csv")
    #df = df.sample(frac=1)

    X = df[df.columns.difference(['label', 'id', 'class', 'filename', 'el_html'])]
    y = df[['label']]

    xgb = XGBClassifier(use_label_encoder=False)
    kfold = KFold(n_splits=10)

    pred = cross_val_predict(xgb, X, y.values.ravel(), cv=kfold)

    print(pred)

    xg_conf_mat = confusion_matrix(y.values.ravel(), pred)

    print(xg_conf_mat)

    plt.figure(dpi=100)
    plot_confusion_matrix(xg_conf_mat, classes=['nav', 'header', 'footer'], normalize=True,
                          title='XGBoost')
    plt.show()

    #export_graphviz(
    #    tree,
    #    out_file="myTreeName.dot",
    #    feature_names=list(X.columns),
    #    class_names=['nav', 'header', 'footer'],
    #    filled=True,
    #    rounded=True)


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def get_best_proba(df):
    labels = list(set(df['label']))

    for label in labels:
        proba_rows = df.loc[df['label'] == label]
        print(proba_rows.iloc[proba_rows['proba_' + str(label)].argmax()].values.ravel())


#save_test_data()
save_data("https://www.artlebedev.ru/tools/")
trained_xgb = teach()
df = predict(trained_xgb)
get_best_proba(df)

#teach_and_predict()
