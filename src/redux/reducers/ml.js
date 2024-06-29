import {
    GET_LINEAL_REGRESSION_SUCCESS,
GET_LINEAL_REGRESSION_FAIL,
GET_LOGIC_REGRESSION_SUCCESS,
GET_LOGIC_REGRESSION_FAIL
} from "../actions/types";
const initialState = {
    lineal_regression:null,
    logic_regression:null
};


export default function ml(state = initialState, action) {
    const { type, payload } = action;

    switch (type) {
        case GET_LINEAL_REGRESSION_SUCCESS:
            return {
                ...state,
                lineal_regression: payload,
            };
            case GET_LOGIC_REGRESSION_SUCCESS:
            return {
                ...state,
                logic_regression: payload,
            };
        case GET_LINEAL_REGRESSION_FAIL:
            return {
                ...state,
                lineal_regression: null,
            };
            case GET_LOGIC_REGRESSION_FAIL:
                return {
                    ...state,
                    logic_regression: null,
                };
        default:
            return state;
    }
}