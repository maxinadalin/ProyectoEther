import { combineReducers } from "redux";
import web3 from "./web3";
import alert from "./alert";
import user from "./user";

export default combineReducers({
web3,
alert,
user
});