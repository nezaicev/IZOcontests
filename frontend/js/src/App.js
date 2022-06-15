import './App.css';
import React from "react";
import {Route, Routes, Link, BrowserRouter} from 'react-router-dom'
import GalleryPageVP from "./pages/VP/GalleryPageVP";

const App = () => {

    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path='/frontend/vp/' element={<GalleryPageVP/>}/>
                </Routes>

            </BrowserRouter>
        </>


    );
}
export default App