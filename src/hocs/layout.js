import { connect } from "react-redux";
import NavBar from "../components/navigation/navBar";
import Footer from "../components/navigation/footer";
import { get_network_id, loadWeb3 } from "../redux/actions/web3";
import { useEffect } from "react";
import { get_my_user_details } from "../redux/actions/user";

function Layout({ children, loadWeb3, get_network_id, my_user, get_my_user_details}) {
  if (window.ethereum) {
    window.ethereum.on("chainChanged", handleChainChanged);
    function handleChainChanged(_chainId) {
        // We recommend reloading the page, unless you must do otherwise
        window.location.reload();
    }
}

useEffect(() => {
    const fetchData = async () => {
        if (localStorage.getItem("account")) {
          loadWeb3();
          my_user ? <></>:get_my_user_details()
        }

    };
    fetchData();

    if (window.ethereum) {
        get_network_id();
    }
}, []);

  return (
    <div>
      <NavBar />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">{children}</div>
      </div>
      <Footer/>
    </div>
  );
}

const mapStateToProps = state =>({
  my_user: state.user.my_user
  })
  
  export default connect(mapStateToProps, {
      loadWeb3,
      get_network_id,
      get_my_user_details,
})(Layout);
