from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import os

# importacion de librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# importar dataset para el preprocesamiento
# path = os.path.join(settings.BASE_DIR,"apps/ml/helpers/preprocesamiento/Data.csv")
 


class PreProcesamientoView(APIView):
    def get(self,request,format=None):
        path = os.path.join(settings.BASE_DIR,"apps/ml/helpers/preprocesamiento/Data.csv")
        dataset = pd.read_csv(path)
        x = dataset.iloc[:,17:21].values    
        y = dataset.iloc[:,-2].values
        print(x)
        print(y)
        # Con esto lo que hago es reemplazar todos los datos faltantes por el promedio
        from sklearn.impute import SimpleImputer
        impute = SimpleImputer(missing_values=np.nan, strategy='mean')
        impute.fit(x[:,1:4])
        x[:,1:4]= impute.transform(x[:,1:4])
        # print(x)
        
        
        from sklearn.impute import SimpleImputer
        y = y.reshape(-1, 1)
        y_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
        y_imputer.fit(y)
        y = y_imputer.transform(y)
        print(y)
        
        
        # One hot encoding(lo que hace es que los paises tomas datos binarios)
        from sklearn.compose import ColumnTransformer
        from sklearn.preprocessing import OneHotEncoder
        # en esta primera colimna transformamos la primer columna en codigos onehot y le decimos quie las demas no las toque
        ct = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough")
    #    transformamos en un array lo que le pasamos 
        x = np.array(ct.fit_transform(x))   
        # print(x)
        
        # en el caso que tampies quisieramos encodiar la variable y aplicamos este codigo
        # from sklean.preprocessing import LabelEncoder
        # le = LabelEncoder()
        # y = le.fit_transform(y)     
        
        # en este paso vamos a separar nuestros datos asi podemos trabajarlos
        from sklearn.model_selection import train_test_split
        # este requiere 4 parametros
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 1)
        # print(x_train)
        # print(x_test)
        # print(y_train)
        # print(y_test)
        
        # el siguiente paso es escalar todos los datos asi tienen la misma escalabilidad
        from sklearn.preprocessing import StandardScaler
        sc=StandardScaler()
        x_test[:,3:] = sc.fit_transform(x_test[:,3:])
        x_train[:,3:] = sc.fit_transform(x_train[:,3:])
        print(x_train)
        print(x_test)
        return Response({"data":"data"},status=status.HTTP_200_OK)


class RegresionLinealView(APIView):
    def get (self,request,format=None):
        path = os.path.join(settings.BASE_DIR,"apps/ml/helpers/preprocesamiento/Data.csv")
        dataset = pd.read_csv(path)
        x = dataset.iloc[:,-2].values  
        y = dataset.iloc[:,-3].values
        # print(x)
        # print(y)
        
        # ahora necesitamos sacar los nan
        from sklearn.impute import SimpleImputer
        x = x.reshape(-1,1 ) 
        y = y.reshape(-1,1 ) 
        impute = SimpleImputer(missing_values=np.nan, strategy='mean')
        impute.fit(x)
        x = impute.transform(x)
        impute.fit(y)
        y = impute.transform(y)
        # print(x)
        # print(y)
        
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.2, random_state = 1)
        # print(x_train)
        # print(x_test)
        # print(y_train)
        # print(y_test)
        
        # AHORA IMPORTANTE LO QUE HACEMOS ES TRAER AL ALGORITMO DE REGRESION LINEAL Y LO ENTRENAMOS 
        from sklearn.linear_model import LinearRegression
        lr = LinearRegression()
        lr.fit(x_train,y_train)
        
        y_prediccion = lr.predict(x_test)
        
        
        # Visualizando datos de entrenamiento
        # Visualizar set de Entrenamiento
        # plt.scatter(x_train, y_train, color = 'red')
        # plt.plot(x_train, lr.predict(x_train), color = 'blue')
        # plt.title('Salary vs Experience (Training set)')
        # plt.xlabel('Years of Experience')
        # plt.ylabel('Salary')
        # plt.show()

        x_train_str = x_train.flatten().tolist()
        x_test_str = x_test.flatten().tolist()
        y_train_str = y_train.flatten().tolist()
        y_test_str = y_test.flatten().tolist()
        regresor_predict_str = lr.predict(x_train).flatten().tolist()
        
        print(f"el resultado de la prediccion es {y_prediccion}")
        
        
        return Response ({'x_train':x_train_str,
            'x_test':x_test_str,
            'y_train':y_train_str,
            'y_test':y_test_str,
            'y_train_predict':regresor_predict_str,
            'title_train':'Salary vs Experience (Training set)',
            'xlabel_train':'Years of Experience',
            'ylabel_train':'Salary'},status = status.HTTP_200_OK)
        

class ClassificacionView(APIView):
    def get(self,request,format=None):
        print("va todo bien")
    
        return Response({"mensaje":"todo bien por ahora"}, status = status.HTTP_200_OK)