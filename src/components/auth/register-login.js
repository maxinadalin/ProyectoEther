import { connect } from "react-redux"
import {Navigate} from 'react-router-dom'
import { loginWeb3 } from "../../redux/actions/web3";
import {
    ChevronRightIcon,
    ChevronDownIcon,
    MailIcon,
} from "@heroicons/react/24/solid";
import LoadingFullWidth from "../loader/loadingFullwidth";

  
 function SignUpSignIn({ loading, loginWeb3, account}) {
    return (
  <>
  <div className="text-center">
                <p className="mt-8 text-xl font-gilroy-bold dark:text-dark-txt text-gray-900 sm:text-2xl sm:tracking-tight lg:text-3xl">
                    Login con Web3
                </p>
                <p className="max-w-xl my-5 mx-auto text-xl dark:text-dark-txt text-gray-500">
                    Conecte con uno de nuestros proveedores de billeteras.
                </p>
            </div>

            {!loading ? (
                <div className="bg-white dark:bg-dark-main hover:dark:bg-dark-second hover:bg-gray-50 shadow overflow-hidden sm:rounded-md">
                    <ul role="list" className="divide-y divide-gray-200">
                        <li>
                            <div
                                onClick={() => {
                                    loginWeb3();
                                }}
                                className="block  transition duration-300 ease-in-out cursor-pointer"
                            >
                                <div className="flex items-center px-4 py-4 sm:px-6">
                                    <div className="min-w-0 flex-1 flex items-center">
                                        <div className="flex-shrink-0">
                                            <img
                                                className="h-12 w-12 rounded-full"
                                                src="https://cdn.iconscout.com/icon/free/png-256/free-metamask-2728406-2261817.png?f=webp"
                                                alt=""
                                            />
                                        </div>
                                        <div className="min-w-0 flex-1 px-4 md:grid md:grid-cols-2 md:gap-4">
                                            <div>
                                                <p className="text-sm font-medium dark:text-dark-txt text-gray-800 truncate">
                                                    Metamask
                                                </p>
                                            </div>
                                            <div className="hidden md:block">
                                                <div>
                                                    <span className="inline-flex items-center px-3 py-0.5 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
                                                        Popular
                                                    </span>
                                                </div>
                                            </div>
                                        </div>
                                        <div>
                                            <ChevronRightIcon
                                                className="h-5 w-5 text-gray-400"
                                                aria-hidden="true"
                                            />
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
            ) : (
                <LoadingFullWidth />
            )}
            <br />
  </>
    )
  }

  const mapStateToProps = (state) => ({
    account: state.web3.account,
    loading: state.web3.loading,

  })
  
  export default connect (mapStateToProps,{
    loginWeb3,
  })(SignUpSignIn)