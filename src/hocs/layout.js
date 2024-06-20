import { connect } from "react-redux";
import NavBar from "../components/navigation/navBar";

function Layout({ children }) {
  return (
    <div>
      <NavBar />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">{children}</div>
      </div>
    </div>
  );
}

const mapStateToProps = (state) => ({});

export default connect(mapStateToProps, {})(Layout);
