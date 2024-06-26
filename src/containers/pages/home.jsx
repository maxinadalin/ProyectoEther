import { connect } from "react-redux";
import Layout from "../../hocs/layout";
import { useEffect } from "react";
import Regression_lineal from "../../components/home/home"




function Home({

}) {
    
useEffect (() =>{

},[])

  return (
    <Layout>
      <Regression_lineal/>
    </Layout>
  );
}

const mapStateToProps = (state) => ({

});

export default connect(mapStateToProps, {
  
})(Home);
