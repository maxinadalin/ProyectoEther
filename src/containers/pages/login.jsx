import { connect } from "react-redux";
import Layout from "../../hocs/layout";
import { useEffect } from "react";
import SignUpSignIn from "../../components/auth/register-login"




function SignIn({

}) {
    
useEffect (() =>{

},[])

  return (
    <Layout>
<SignUpSignIn/>
    </Layout>
  );
}

const mapStateToProps = (state) => ({

});

export default connect(mapStateToProps, {
  
})(SignIn);
