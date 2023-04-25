import Header from "./Header/Header";
import {Outlet} from "react-router-dom";

const Layout = () => {
    return (
        <>
            <header>
                <Header/>
            </header>
            <Outlet/>
            <footer> 2022</footer>
        </>
    )
}

export {Layout}