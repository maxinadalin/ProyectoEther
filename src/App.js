
import './/assets/styles/index.css';
import { Provider } from 'react-redux';
import store from './store';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Error404 from './containers/pages/error404';
import Home from './containers/pages/home';
import SignIn from "./containers/pages/login"
import Profile from './containers/pages/perfil';

function App() {
  return (
<Provider store={store}>
<Router>
    
<Routes>
  <Route path='*' element={<Error404/>}/>
  <Route path='/' element={<Home/>}/>
 

  <Route path='/Login-Register' element={<SignIn/>}/>

  <Route path='/perfil/:user_account' element={<Profile/>}/>

</Routes>
    </Router>
</Provider>
  );
}

export default App;
