import { connect } from "react-redux";
import Layout from "../../hocs/layout";
import { useEffect } from "react";
import Profile from "../../components/profile/profile"




function Perfil({

}) {
    
useEffect (() =>{

},[])

  return (
    <Layout>
<Profile/>
    </Layout>
  );
}

const mapStateToProps = (state) => ({

});

export default connect(mapStateToProps, {
  
})(Perfil);
