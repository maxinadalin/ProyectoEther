import { connect } from "react-redux";
import  {get_lineal_regression} from "../../redux/actions/ml"
import { useEffect } from "react";
import { Scatter } from 'react-chartjs-2';
import 'chart.js/auto';

function Regression_lineal({
    get_lineal_regression,
    lineal_regression
}){
    useEffect(()=> {
       const fetchData = async () =>{
        get_lineal_regression()

       };
       fetchData()
    },[])
      // Verificar que lineal_regression y sus propiedades no sean null o undefined
      if (!lineal_regression || !lineal_regression.x_train || !lineal_regression.y_train) {
        return <div>No hay datos de regresión lineal disponibles.</div>;
    }

    const x_train = lineal_regression.x_train;
    const y_train = lineal_regression.y_train;
    const y_train_predict = lineal_regression.y_train_predict

    console.log('regression_lineal:', lineal_regression);

     // Construir el objeto data para el gráfico de dispersión
     const data = x_train.map((value, index) => ({
        x: value,
        y: y_train[index], // Asumiendo que x_train y y_train tienen la misma longitud
    }));

         // Construir el objeto data para el gráfico de dispersión
         const data2 = x_train.map((value, index) => ({
            x: value,
            y: y_train_predict[index], // Asumiendo que x_train y y_train tienen la misma longitud
        }))
        ;

     const datos = {
    label: 'prediccion de sueldos en base a los años de experiencia',
    data: data2,
    backgroundColor: 'rgb(54, 162, 235)',
    type: 'line' // Tipo de gráfico para este dataset
};


    const chartData = {
        datasets: [{
            label: 'sueldos en base a la experiencia',
            data:data, // Pasamos los datos como prop
            backgroundColor: 'rgb(255, 99, 132)'
        },
        datos // Agregamos el dataset de línea al arreglo de datasets
        ],
    };

    const chartConfig = {
        type: 'scatter',
        data: chartData,
        options: {
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom'
                }
            }
        }
    };








    return(
        <>
   
            <div>
                <Scatter data={chartData} options={chartConfig.options} />
            </div>
</>
    )
}

const mapStateToProps = (state) => ({
    lineal_regression: state.ml.lineal_regression
})

export default connect(mapStateToProps,{
    get_lineal_regression
})(Regression_lineal)